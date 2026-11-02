import type { ReactNode } from 'react';
export function Panel({title, children}: {title:string; children:ReactNode}) {
  return <section className="panel"><h2>{title}</h2>{children}</section>;
}
export function Stat({label, value}: {label:string; value:string|number}) {
  return <div className="stat"><span>{label}</span><strong>{value}</strong></div>;
}
