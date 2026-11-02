import json
from bs4 import BeautifulSoup
from models import Product

def is_challenge_page(html: str, status_code: int = 200) -> bool:
    if status_code == 429: return True
    soup = BeautifulSoup(html or "", "html.parser")
    title = (soup.title.get_text(" ", strip=True).lower() if soup.title else "")
    text = (title + " " + soup.get_text(" ", strip=True)[:5000]).lower()
    markers = ("just a moment", "checking your browser", "verify you are human",
               "cf-chl-", "cloudflare ray id", "attention required! | cloudflare")
    return any(marker in text for marker in markers)

def parse_product(html: str, url: str) -> Product:
    soup = BeautifulSoup(html, "html.parser")
    data = {}
    for tag in soup.select('script[type="application/ld+json"]'):
        try:
            raw = json.loads(tag.string or tag.get_text())
            candidates = raw if isinstance(raw, list) else [raw]
            for item in candidates:
                if isinstance(item, dict) and item.get("@type") == "Product":
                    data = item
                    break
        except (ValueError, TypeError):
            continue
    offers = data.get("offers") or {}
    if isinstance(offers, list): offers = offers[0] if offers else {}
    images = data.get("image") or []
    if isinstance(images, str): images = [images]
    description = data.get("description")
    return Product(
        url=url,
        title=data.get("name") or (soup.title.get_text(" ", strip=True) if soup.title else None),
        brand=(data.get("brand") or {}).get("name") if isinstance(data.get("brand"), dict) else data.get("brand"),
        price=float(offers["price"]) if offers.get("price") not in (None, "") else None,
        currency=offers.get("priceCurrency"),
        sku=data.get("sku"), ean=data.get("gtin13") or data.get("gtin"),
        availability=offers.get("availability"), description=description,
        images=[str(x) for x in images], source="pluspower"
    )
