import httpx
from config import TAVILY_API_KEY

async def search_product(query: str) -> dict:
    if not TAVILY_API_KEY:
        raise RuntimeError("TAVILY_API_KEY is not configured")
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "advanced",
        "topic": "general",
        "max_results": 5,
        "include_answer": False,
        "include_raw_content": False
    }
    async with httpx.AsyncClient(timeout=20) as client:
        response = await client.post("https://api.tavily.com/search", json=payload)
        response.raise_for_status()
        return response.json()
