create table if not exists public.products (
  id uuid primary key default gen_random_uuid(),
  url text not null unique,
  title text,
  brand text,
  price numeric,
  currency text,
  sku text,
  ean text,
  availability text,
  description text,
  ingredients text,
  images jsonb not null default '[]'::jsonb,
  variants jsonb not null default '[]'::jsonb,
  source text not null default 'pluspower',
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);
create index if not exists products_title_idx on public.products using gin (to_tsvector('simple', coalesce(title,'')));
create index if not exists products_sku_idx on public.products (sku);
create index if not exists products_ean_idx on public.products (ean);
