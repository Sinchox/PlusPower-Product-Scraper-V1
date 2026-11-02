from pydantic import BaseModel, HttpUrl
from typing import Optional
class ScrapeRequest(BaseModel):
    url: HttpUrl
class Variant(BaseModel):
    name: Optional[str] = None
    sku: Optional[str] = None
    ean: Optional[str] = None
    price: Optional[float] = None
    availability: Optional[str] = None
class Product(BaseModel):
    url: str
    title: Optional[str] = None
    brand: Optional[str] = None
    price: Optional[float] = None
    currency: Optional[str] = None
    sku: Optional[str] = None
    ean: Optional[str] = None
    availability: Optional[str] = None
    description: Optional[str] = None
    ingredients: Optional[str] = None
    images: list[str] = []
    variants: list[Variant] = []
    source: str = "pluspower"
