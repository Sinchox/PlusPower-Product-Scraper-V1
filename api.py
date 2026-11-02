import csv, io
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from config import CORS_ORIGINS
from models import ScrapeRequest
from scraper import scrape_product, ScrapeBlocked
from database import list_products, save_product

app = FastAPI(title="PlusPower Product Scraper API", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=CORS_ORIGINS, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/health")
def health(): return {"status":"ok"}

@app.get("/products")
def products():
    try: return list_products()
    except Exception as e: raise HTTPException(500, str(e))

@app.post("/scrape")
async def scrape(request: ScrapeRequest):
    try:
        product = await scrape_product(str(request.url))
        saved = save_product(product.model_dump())
        return {"message":"Product extracted and saved", "product":saved}
    except ScrapeBlocked as e: raise HTTPException(429, str(e))
    except RuntimeError as e: raise HTTPException(503, str(e))
    except Exception as e: raise HTTPException(500, str(e))

@app.get("/products.csv")
def export_csv():
    rows = list_products()
    output = io.StringIO()
    fields = ["title","brand","price","currency","sku","ean","availability","url"]
    writer = csv.DictWriter(output, fieldnames=fields, extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows)
    from fastapi.responses import StreamingResponse
    return StreamingResponse(iter([output.getvalue()]), media_type="text/csv", headers={"Content-Disposition":"attachment; filename=pluspower-products.csv"})
