from langchain_aws import ChatBedrock
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

# _llm = ChatBedrock(model="global.anthropic.claude-haiku")
_llm = ChatBedrock(model="anthropic.claude-3-haiku-20240307-v1:0")

@tool
def create_social_media_content(business_name: str, platform: str):
    """Generate social media post content."""
    
    prompt = f"""
Create {platform} post content for {business_name}.
Return only the post content.
"""
    response = _llm.invoke([HumanMessage(content=prompt)])
    return response.content