import httpx
from parser import is_challenge_page, parse_product

class ScrapeBlocked(RuntimeError): pass

async def scrape_product(url: str):
    headers = {"User-Agent": "PlusPowerProductResearch/1.0 (contact: admin@example.com)"}
    async with httpx.AsyncClient(timeout=25, follow_redirects=True, headers=headers) as client:
        response = await client.get(url)
    if response.status_code == 429 or is_challenge_page(response.text, response.status_code):
        raise ScrapeBlocked(f"Access challenge or rate limit detected (HTTP {response.status_code}). Scraping stopped.")
    if response.status_code >= 400:
        raise RuntimeError(f"Source returned HTTP {response.status_code}")
    return parse_product(response.text, str(response.url))
