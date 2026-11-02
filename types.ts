export type Product = {
  id?: string;
  url: string;
  title: string | null;
  brand: string | null;
  price: number | null;
  currency: string | null;
  sku: string | null;
  ean: string | null;
  availability: string | null;
  description: string | null;
  ingredients: string | null;
  images: string[];
  variants: Variant[];
  source: string;
  scraped_at?: string;
};
export type Variant = {
  name: string | null;
  sku: string | null;
  ean: string | null;
  price: number | null;
  availability: string | null;
};
