from supabase import create_client
from dotenv import load_dotenv
import os

# LOAD ENV FILE
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise ValueError("Supabase URL or KEY missing in .env")

supabase = create_client(url, key)