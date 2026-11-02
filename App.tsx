import { useEffect, useState } from 'react';
import { Panel, Stat } from './components';
import type { Product } from './types';
import './styles.css';

const API = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export default function App() {
  const [products, setProducts] = useState<Product[]>([]);
  const [url, setUrl] = useState('');
  const [busy, setBusy] = useState(false);
  const [message, setMessage] = useState('Ready');

  async function refresh() {
    try {
      const response = await fetch(`${API}/products`);
      if (response.ok) setProducts(await response.json());
    } catch { /* API may not be running yet */ }
  }
  useEffect(() => { void refresh(); }, []);

  async function scrape() {
    if (!url.trim()) return;
    setBusy(true); setMessage('Scraping product page…');
    try {
      const response = await fetch(`${API}/scrape`, {
        method:'POST', headers:{'Content-Type':'application/json'},
        body:JSON.stringify({url:url.trim()})
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || 'Scrape failed');
      setMessage(data.message || 'Product processed');
      setUrl('');
      await refresh();
    } catch (error) {
      setMessage(error instanceof Error ? error.message : 'Request failed');
    } finally { setBusy(false); }
  }

  return <main className="shell">
    <header><div><p className="eyebrow">PRODUCT INTELLIGENCE</p><h1>PlusPower Scraper</h1><p className="sub">Product discovery, extraction and catalogue management</p></div><span className="status">● {message}</span></header>
    <div className="stats"><Stat label="Saved products" value={products.length}/><Stat label="Source" value="PlusPower Supplements"/><Stat label="Mode" value="Protected scraping"/></div>
    <Panel title="Add product URL">
      <div className="entry"><input value={url} onChange={e=>setUrl(e.target.value)} placeholder="https://www.pluspowersupplements.com/…"/><button disabled={busy || !url.trim()} onClick={scrape}>{busy?'Working…':'Scrape product'}</button></div>
      <p className="hint">Challenge pages and rate limits are detected. The scraper stops safely instead of attempting to bypass them.</p>
    </Panel>
    <Panel title="Product catalogue">
      <div className="table-wrap"><table><thead><tr><th>Product</th><th>Brand</th><th>Price</th><th>SKU</th><th>Availability</th></tr></thead>
      <tbody>{products.map((p,i)=><tr key={p.id || i}><td>{p.title || '—'}<small>{p.url}</small></td><td>{p.brand || '—'}</td><td>{p.price == null ? '—' : `${p.price} ${p.currency || ''}`}</td><td>{p.sku || '—'}</td><td>{p.availability || '—'}</td></tr>)}
      {!products.length && <tr><td colSpan={5} className="empty">No products saved yet.</td></tr>}</tbody></table></div>
      <a className="export" href={`${API}/products.csv`}>Export CSV ↓</a>
    </Panel>
  </main>;
}
