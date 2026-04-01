# import boto3
# import json
# import base64
# import uuid
# from datetime import datetime
# from langchain_core.tools import tool
# from supabase_client import supabase

# def generate_filename(name, i):
#     return f"{name}_{datetime.now().strftime('%Y%m%d%H%M%S')}_{i}_{uuid.uuid4().hex[:4]}.png"

# @tool
# def generate_logo(business_name: str, count: int = 1):
#     """Generate logos and upload to Supabase storage."""
    
#     client = boto3.client("bedrock-runtime", region_name="us-east-1")
#     urls = []

#     for i in range(count):
#         body = json.dumps({
#             "taskType": "TEXT_IMAGE",
#             "textToImageParams": {
#             #     "text": f"minimal logo for {business_name}, no text"
#             # },
#                     "text": f"""
# Create a modern logo for {business_name}.
# IMPORTANT: The text must be exactly '{business_name}' with correct spelling.
# Use clean typography, light colors, and professional style.
# """
#     },
#             "imageGenerationConfig": {
#                 "height": 512,
#                 "width": 512
#             }
#         })

#         response = client.invoke_model(
#             body=body,
#             modelId="amazon.titan-image-generator-v2:0",
#             accept="application/json",
#             contentType="application/json"
#         )

#         data = json.loads(response["body"].read())
#         image_bytes = base64.b64decode(data["images"][0])

#         filename = generate_filename(business_name, i)

#         # Upload to Supabase
#         supabase.storage.from_("logos").upload(filename, image_bytes)

#         public_url = supabase.storage.from_("logos").get_public_url(filename)
#         urls.append(public_url)

#     return "\n".join(urls)

import boto3
import json
import base64
import uuid
import time
from datetime import datetime
from langchain_core.tools import tool
from supabase_client import supabase

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO


# 🔹 Generate filename
def generate_filename(name, i):
    safe_name = name.replace(" ", "_")
    return f"{safe_name}_{datetime.now().strftime('%Y%m%d%H%M%S')}_{i}_{uuid.uuid4().hex[:4]}.png"


# 🔥 ADD PERFECT TEXT (NO AI MISTAKES)
def add_clean_text(image_bytes, text):
    image = Image.open(BytesIO(image_bytes)).convert("RGBA")

    width, height = image.size

    # 🆕 New canvas with extra space
    new_height = height + 100
    new_image = Image.new("RGBA", (width, new_height), (255, 255, 255, 255))
    new_image.paste(image, (0, 0))

    draw = ImageDraw.Draw(new_image)

    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    # Center text
    bbox = draw.textbbox((0, 0), text.upper(), font=font)
    text_width = bbox[2] - bbox[0]

    x = (width - text_width) // 2
    y = height + 20

    draw.text((x, y), text.upper(), fill="black", font=font)

    output = BytesIO()
    new_image.save(output, format="PNG")
    return output.getvalue()


# 🚀 MAIN TOOL
@tool
def generate_logo(business_name: str, count: int = 1):
    """Generate logos with correct company name (no AI text issues)"""

    client = boto3.client("bedrock-runtime", region_name="us-east-1")

    urls = []

    # 🎨 Different styles → ensures unique logos
    styles = [
        "minimal geometric tech icon",
        "modern abstract IT symbol",
        "corporate consulting icon",
        "futuristic digital symbol",
        "premium luxury brand icon"
    ]

    for i in range(count):

        prompt = f"{styles[i % len(styles)]}, no text, clean, bright colors, professional"

        body = json.dumps({
            "taskType": "TEXT_IMAGE",
            "textToImageParams": {
                "text": prompt
            },
            "imageGenerationConfig": {
                "height": 512,
                "width": 512,
                "seed": uuid.uuid4().int % 100000
            }
        })

        # 🧠 Generate image
        response = client.invoke_model(
            body=body,
            modelId="amazon.titan-image-generator-v2:0",
            accept="application/json",
            contentType="application/json"
        )

        data = json.loads(response["body"].read())
        image_bytes = base64.b64decode(data["images"][0])

        # ✅ ADD PERFECT TEXT (this solves ALL your issues)
        image_bytes = add_clean_text(image_bytes, business_name)

        filename = generate_filename(business_name, i)

        # 🔁 Retry upload (fix random crash)
        for attempt in range(3):
            try:
                supabase.storage.from_("logos").upload(filename, image_bytes)
                break
            except Exception as e:
                if attempt == 2:
                    raise e
                time.sleep(2)

        public_url = supabase.storage.from_("logos").get_public_url(filename)
        urls.append(public_url)

        time.sleep(1)

    return "\n".join(urls)