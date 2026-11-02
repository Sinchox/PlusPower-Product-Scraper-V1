import os
from dotenv import load_dotenv
load_dotenv()
PLUSPOWER_BASE_URL = os.getenv("PLUSPOWER_BASE_URL", "https://www.pluspowersupplements.com").rstrip("/")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
CORS_ORIGINS = [x.strip() for x in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",") if x.strip()]
