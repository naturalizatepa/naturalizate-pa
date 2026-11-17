#!/usr/bin/env python3
"""
Genera la «Guía completa de naturalización panameña» de Naturalízate.pa
como un único archivo HTML autosuficiente (tipografías y logotipos embebidos).

Uso:  python3 build_guia_completa.py
Salida: guia-naturalizacion-completa.html
"""
import base64
import pathlib

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "guia-naturalizacion-completa.html"


def b64(path: pathlib.Path) -> str:
    return base64.b64encode(path.read_bytes()).decode("ascii")


FONT_INTER = b64(ROOT / "fonts/inter-latin-wght-normal.woff2")
FONT_PLAYFAIR = b64(ROOT / "fonts/playfair-display-latin-wght-normal.woff2")
FONT_PLAYFAIR_IT = b64(ROOT / "fonts/playfair-display-latin-wght-italic.woff2")
LOGO_NAVY = b64(ROOT / "svg/logo-principal-navy.svg")
LOGO_WHITE = b64(ROOT / "svg/logo-principal-blanco.svg")

SITE = "https://naturalizatepa.github.io/naturalizate-pa/"
WA = "https://wa.me/50762557583?text="
WA_TEXT = (
    "Hola%2C%20le%C3%AD%20la%20Gu%C3%ADa%20completa%20de%20naturalizaci%C3%B3n"
    "%20y%20quiero%20precalificar%20mi%20caso."
)

HTML = r"""<!DOCTYPE html>
<html lang="es-PA">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Naturalización panameña: guía completa 2026 | Naturalízate.pa</title>
<meta name="description" content="Guía completa de la naturalización panameña: vías y tiempos de residencia, requisitos documentales, solvencia 2 de 3, las cuatro fases ante el Estado, honorarios y errores que cuestan años. Lic. Alfonso Villarreal." />
<meta name="robots" content="index, follow" />
<meta name="author" content="Lic. Alfonso Villarreal · Naturalízate.pa" />
<meta name="theme-color" content="#0D1B2A" />
<link rel="canonical" href="__SITE__guia-naturalizacion-completa.html" />

<meta property="og:type" content="article" />
<meta property="og:locale" content="es_PA" />
<meta property="og:site_name" content="Naturalízate.pa" />
<meta property="og:title" content="Naturalización panameña: guía completa 2026" />
<meta property="og:description" content="Vías y tiempos, requisitos, solvencia 2 de 3, las cuatro fases ante el Estado y los errores que cuestan años. Por el Lic. Alfonso Villarreal." />
<meta property="og:url" content="__SITE__guia-naturalizacion-completa.html" />
<meta property="og:image" content="__SITE__og-image.png" />
<meta name="twitter:card" content="summary_large_image" />

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "Article",
      "headline": "Naturalización panameña: guía completa 2026",
      "description": "Vías y tiempos de residencia, requisitos documentales, regla de solvencia 2 de 3, las cuatro fases ante el Estado y los errores que cuestan años.",
      "inLanguage": "es-PA",
      "datePublished": "2026-11-17",
      "dateModified": "2026-11-17",
      "author": {
        "@type": "Person",
        "name": "Alfonso Villarreal",
        "jobTitle": "Abogado fundador",
        "worksFor": { "@type": "Organization", "name": "Naturalízate.pa" }
      },
      "publisher": {
        "@type": "Organization",
        "name": "Naturalízate.pa",
        "url": "__SITE__"
      },
      "mainEntityOfPage": "__SITE__guia-naturalizacion-completa.html"
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {"@type":"Question","name":"¿Basta tener la Cédula E para naturalizarme?","acceptedAnswer":{"@type":"Answer","text":"No por sí sola. La Cédula E acredita su condición migratoria, pero la ley exige además los cinco años de residencia, el arraigo, la conducta y la integración."}},
        {"@type":"Question","name":"¿Desde cuándo se cuentan los cinco años?","acceptedAnswer":{"@type":"Answer","text":"El período se cuenta por la residencia permanente mantenida en Panamá. Por reciprocidad, El Salvador requiere 1 año; Argentina, Colombia, Ecuador, España, Honduras, México, Nicaragua y Perú, 2 años; Uruguay, 3 años."}},
        {"@type":"Question","name":"¿Cuánto cuesta naturalizarse en Panamá?","acceptedAnswer":{"@type":"Answer","text":"Los honorarios del despacho son fijos y por escrito: $3,800 en la modalidad Esencial y $5,500 en la Integral, con pago fraccionado. Las tasas del Estado, apostillas y traducciones se detallan por separado antes de iniciar."}},
        {"@type":"Question","name":"¿Qué exige el examen de naturalización?","acceptedAnswer":{"@type":"Answer","text":"Conocimientos de español, historia, geografía, gobierno y cultura de Panamá. No superarlo retrasa el proceso."}},
        {"@type":"Question","name":"¿Puedo perder mi nacionalidad de origen?","acceptedAnswer":{"@type":"Answer","text":"La jura de naturalización incluye renunciar a la nacionalidad de origen. Además, quien adquiere voluntariamente otra nacionalidad puede perder la panameña (artículo 14 de la Constitución)."}},
        {"@type":"Question","name":"¿Cuánto tarda el proceso completo?","acceptedAnswer":{"@type":"Answer","text":"Depende de la carga del Tribunal Electoral y del Órgano Ejecutivo y de la integridad del expediente. El plazo habitual del despacho es de 19 a 22 meses con expediente íntegro."}},
        {"@type":"Question","name":"¿Necesito un abogado en Panamá?","acceptedAnswer":{"@type":"Answer","text":"Sí. La solicitud de naturalización se presenta mediante abogado ante el Tribunal Electoral; el acompañamiento profesional es parte del trámite."}},
        {"@type":"Question","name":"¿Qué pasa si mi caso no califica?","acceptedAnswer":{"@type":"Answer","text":"Se lo indicamos por escrito en la consulta inicial, con su fundamento, y no le proponemos el trámite."}}
      ]
    }
  ]
}
</script>

<style>
  /* ===== Brand Book v3.0 · tipografías de marca embebidas (archivo autosuficiente) ===== */
  @font-face {
    font-family: "Inter"; font-style: normal; font-weight: 100 900; font-display: swap;
    src: url(data:font/woff2;base64,__FONT_INTER__) format("woff2");
  }
  @font-face {
    font-family: "Playfair Display"; font-style: normal; font-weight: 400 900; font-display: swap;
    src: url(data:font/woff2;base64,__FONT_PLAYFAIR__) format("woff2");
  }
  @font-face {
    font-family: "Playfair Display"; font-style: italic; font-weight: 400 900; font-display: swap;
    src: url(data:font/woff2;base64,__FONT_PLAYFAIR_IT__) format("woff2");
  }

  :root {
    --navy: #0D1B2A; --navy-deep: #060F17; --navy-2: #1B3A57; --navy-soft: #15293E;
    --white: #FFFFFF;
    --g50: #F8F9FA; --g100: #F1F3F5; --g200: #E9ECEF; --g300: #DEE2E6;
    --g400: #ADB5BD; --g600: #5C6772; --g700: #495057; --g900: #212529;
    --wa-solid: #0F7A40; --wa-solid-hover: #0B6332;
    --serif: "Playfair Display", Georgia, "Times New Roman", serif;
    --sans: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    --measure: 748px;
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }
  body {
    font-family: var(--sans); color: var(--g700); background: #fff;
    line-height: 1.72; font-size: 17px; -webkit-font-smoothing: antialiased;
  }
  img { max-width: 100%; display: block; }
  a { color: var(--navy-2); text-decoration-color: rgba(27,58,87,.35); text-underline-offset: 3px; }
  a:hover { color: var(--navy); text-decoration-color: var(--navy); }
  strong { color: var(--navy); font-weight: 600; }
  em { font-style: italic; }

  .wrap { max-width: 1040px; margin: 0 auto; padding: 0 28px; }
  .measure { max-width: var(--measure); }
  .center { margin-left: auto; margin-right: auto; }

  /* ============ barra superior + navegación ============ */
  .topbar { background: var(--navy-deep); color: rgba(255,255,255,.78); font-size: .78rem; letter-spacing: .2px; }
  .topbar .wrap { display: flex; justify-content: space-between; gap: 14px; flex-wrap: wrap; padding-top: 9px; padding-bottom: 9px; }
  .topbar strong { color: #fff; font-weight: 600; }
  .topbar a { color: #fff; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,.35); }
  .topbar a:hover { border-color: #fff; }

  .nav { position: sticky; top: 0; z-index: 90; background: rgba(255,255,255,.97); backdrop-filter: blur(10px); border-bottom: 1px solid var(--g200); }
  .nav .wrap { display: flex; align-items: center; justify-content: space-between; height: 68px; gap: 20px; }
  .nav-logo { display: block; width: 172px; flex-shrink: 0; }
  .nav-links { display: flex; align-items: center; gap: 22px; }
  .nav-links a { font-size: .87rem; font-weight: 500; color: var(--g700); text-decoration: none; }
  .nav-links a:hover { color: var(--navy); }
  .nav-cta { background: var(--navy); color: #fff !important; padding: 10px 18px; border-radius: 6px; font-size: .85rem; font-weight: 600; white-space: nowrap; }
  .nav-cta:hover { background: var(--navy-2); }
  .cta-short { display: none; }
  @media (max-width: 900px) { .nav-links a:not(.nav-cta) { display: none; } .nav-logo { width: 148px; } }
  @media (max-width: 560px) {
    .nav .wrap { height: 62px; gap: 12px; }
    .nav-logo { width: 130px; }
    .nav-cta { padding: 9px 13px; font-size: .8rem; }
    .cta-long { display: none; }
    .cta-short { display: inline; }
    .topbar { font-size: .71rem; }
    .topbar .wrap { gap: 3px; padding-top: 7px; padding-bottom: 7px; }
    .progress { top: 62px; }
  }

  .progress { height: 2px; background: var(--g200); position: sticky; top: 68px; z-index: 89; }
  .progress span { display: block; height: 2px; width: 0; background: var(--navy); }

  /* ============ portada ============ */
  .hero { background: linear-gradient(158deg, var(--navy-deep) 0%, var(--navy) 58%, var(--navy-2) 100%); color: #fff; padding: 64px 0 72px; }
  .hero-logo { width: 208px; margin-bottom: 40px; }
  .kicker { display: inline-flex; align-items: center; gap: 12px; font-size: .72rem; font-weight: 600; letter-spacing: 2.6px; text-transform: uppercase; color: var(--g400); margin-bottom: 22px; }
  .kicker::before { content: ""; width: 30px; height: 1px; background: var(--g400); }
  .hero h1 { font-family: var(--serif); font-weight: 600; font-size: clamp(2.05rem, 5vw, 3.15rem); line-height: 1.14; letter-spacing: -.6px; max-width: 820px; margin-bottom: 22px; }
  .hero h1 em { font-style: italic; font-weight: 400; color: #C9D3DC; }
  .hero .lead { font-size: 1.09rem; color: rgba(255,255,255,.84); max-width: 660px; margin-bottom: 28px; }
  .byline { display: flex; flex-wrap: wrap; align-items: center; gap: 10px 18px; font-size: .84rem; color: rgba(255,255,255,.66); border-top: 1px solid rgba(255,255,255,.14); padding-top: 20px; max-width: 660px; }
  .byline strong { color: #fff; font-weight: 600; }
  .byline .dot { width: 4px; height: 4px; border-radius: 50%; background: rgba(255,255,255,.4); }
  .hero-cta { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 30px; }

  .btn { display: inline-flex; align-items: center; justify-content: center; gap: 9px; padding: 14px 24px; border-radius: 6px; font-family: var(--sans); font-size: .93rem; font-weight: 600; text-decoration: none; border: 1.5px solid transparent; transition: background .18s ease, color .18s ease, transform .18s ease, border-color .18s ease; }
  .btn-white { background: #fff; color: var(--navy); }
  .btn-white:hover { background: var(--g100); color: var(--navy); transform: translateY(-1px); }
  .btn-navy { background: var(--navy); color: #fff; }
  .btn-navy:hover { background: var(--navy-2); color: #fff; transform: translateY(-1px); }
  .btn-outline-w { background: transparent; color: #fff; border-color: rgba(255,255,255,.45); }
  .btn-outline-w:hover { border-color: #fff; background: rgba(255,255,255,.08); color: #fff; }
  .btn-wa { background: var(--wa-solid); border-color: var(--wa-solid); color: #fff; }
  .btn-wa:hover { background: var(--wa-solid-hover); border-color: var(--wa-solid-hover); color: #fff; transform: translateY(-1px); }

  /* ============ índice ============ */
  .toc { background: var(--g50); border-bottom: 1px solid var(--g200); padding: 44px 0 48px; }
  .toc-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0 44px; margin-top: 22px; }
  .toc a { display: flex; gap: 14px; align-items: baseline; padding: 13px 0; border-bottom: 1px solid var(--g200); text-decoration: none; color: var(--g700); font-size: .95rem; }
  .toc a:hover { color: var(--navy); }
  .toc a span:first-child { font-family: var(--serif); font-style: italic; font-size: 1.05rem; color: var(--g400); min-width: 22px; }
  .toc a:hover span:first-child { color: var(--navy); }
  .eyebrow { font-size: .72rem; font-weight: 700; letter-spacing: 2.6px; text-transform: uppercase; color: var(--g600); }
  @media (max-width: 760px) { .toc-grid { grid-template-columns: 1fr; gap: 0; } }

  /* ============ artículo ============ */
  main { padding: 62px 0 20px; }
  .article > * { max-width: var(--measure); margin-left: auto; margin-right: auto; }
  .article > .wide { max-width: 900px; }

  .article p { margin-bottom: 20px; }
  .article p.intro-first::first-letter {
    font-family: var(--serif); float: left; font-size: 3.5rem; line-height: .86;
    padding: 6px 12px 0 0; color: var(--navy); font-weight: 600;
  }

  .sec { margin-top: 74px; }
  .sec-head { margin-bottom: 26px; }
  .sec-head .num {
    display: inline-flex; align-items: center; gap: 12px;
    font-size: .72rem; font-weight: 700; letter-spacing: 2.4px; text-transform: uppercase; color: var(--g600); margin-bottom: 14px;
  }
  .sec-head .num::before { content: ""; width: 26px; height: 1px; background: var(--navy); }
  .sec h2, .sec-head h2 {
    font-family: var(--serif); font-weight: 600; color: var(--navy);
    font-size: clamp(1.55rem, 3.4vw, 2.05rem); line-height: 1.24; letter-spacing: -.3px;
  }
  .sec h2 em { font-style: italic; font-weight: 400; color: var(--navy-2); }
  .sec h3 { font-family: var(--serif); font-weight: 600; font-size: 1.28rem; color: var(--navy); line-height: 1.32; margin: 44px auto 14px; }
  .sec h4 { font-family: var(--sans); font-weight: 700; font-size: .98rem; color: var(--navy); margin-bottom: 6px; letter-spacing: .1px; }

  ul.clean, ol.clean { list-style: none; margin: 0 auto 22px; max-width: var(--measure); }
  ul.clean li, ol.clean li { position: relative; padding: 10px 0 10px 30px; border-bottom: 1px solid var(--g200); font-size: .97rem; }
  ul.clean li:last-child, ol.clean li:last-child { border-bottom: none; }
  ul.clean li::before { content: "—"; position: absolute; left: 0; color: var(--navy); font-weight: 600; }
  ul.check li::before { content: "✓"; color: var(--navy); font-weight: 700; }
  ol.clean { counter-reset: c; }
  ol.clean li { padding-left: 34px; }
  ol.clean li::before { counter-increment: c; content: counter(c) "."; position: absolute; left: 0; top: 10px; font-family: var(--serif); font-style: italic; color: var(--navy); font-size: 1rem; }

  /* tablas */
  .table-wrap { margin: 26px auto 28px; max-width: 900px; border: 1px solid var(--g200); border-radius: 8px; overflow-x: auto; -webkit-overflow-scrolling: touch; }
  table { width: 100%; border-collapse: collapse; font-size: .93rem; background: #fff; min-width: 520px; }
  thead th { background: var(--navy); color: #fff; text-align: left; font-size: .7rem; letter-spacing: 1.4px; text-transform: uppercase; font-weight: 600; padding: 13px 20px; }
  td, tbody th { padding: 14px 20px; border-bottom: 1px solid var(--g200); text-align: left; vertical-align: top; }
  tbody th { font-weight: 600; color: var(--navy); font-size: .93rem; }
  tbody tr:nth-child(even) { background: var(--g50); }
  tbody tr:last-child th, tbody tr:last-child td { border-bottom: none; }
  td.num-cell { font-variant-numeric: tabular-nums; white-space: nowrap; }
  .t-small { font-size: .84rem; color: var(--g600); }

  /* llamados */
  .callout { margin: 30px auto; max-width: var(--measure); border-radius: 8px; padding: 24px 26px; border: 1px solid var(--g200); background: var(--g50); border-left: 3px solid var(--navy); font-size: .95rem; }
  .callout .label { display: block; font-size: .7rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; color: var(--g600); margin-bottom: 8px; }
  .callout p { margin-bottom: 12px; }
  .callout p:last-child { margin-bottom: 0; }
  .callout.warn { background: #FBF7F0; border-color: #EADFC8; border-left-color: #8A6A2F; }
  .callout.warn .label { color: #8A6A2F; }

  .quote { margin: 40px auto; max-width: var(--measure); padding: 4px 0 4px 24px; border-left: 2px solid var(--navy); font-family: var(--serif); font-style: italic; font-size: 1.16rem; line-height: 1.6; color: var(--navy); }
  .quote cite { display: block; margin-top: 12px; font-family: var(--sans); font-style: normal; font-size: .8rem; letter-spacing: .4px; color: var(--g600); }

  /* tarjetas de requisitos / solvencia */
  .cards-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin: 28px auto; max-width: 900px; }
  .cards-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 18px; margin: 28px auto; max-width: 900px; }
  .card { background: #fff; border: 1px solid var(--g200); border-top: 3px solid var(--navy); border-radius: 0 0 8px 8px; padding: 24px 22px; }
  .card .step { font-family: var(--serif); font-style: italic; font-size: 1.5rem; color: var(--g400); line-height: 1; margin-bottom: 10px; }
  .card h4 { font-family: var(--serif); font-weight: 600; font-size: 1.05rem; color: var(--navy); margin-bottom: 10px; line-height: 1.3; }
  .card p, .card li { font-size: .9rem; }
  .card ul { list-style: none; }
  .card ul li { padding: 7px 0 7px 20px; position: relative; border-bottom: 1px solid var(--g200); }
  .card ul li:last-child { border-bottom: none; }
  .card ul li::before { content: "·"; position: absolute; left: 6px; color: var(--navy); font-weight: 700; }
  @media (max-width: 780px) { .cards-3, .cards-2 { grid-template-columns: 1fr; } }
  /* En pantallas grandes, tablas y rejillas respiran por fuera de la columna de lectura */
  @media (min-width: 1020px) {
    .cards-3, .cards-2, .table-wrap { width: 900px; max-width: 900px; margin-left: calc((var(--measure) - 900px) / 2); margin-right: 0; }
  }

  /* fases */
  .phase { border-left: 2px solid var(--g200); padding: 0 0 6px 28px; margin: 0 auto 34px; max-width: var(--measure); position: relative; }
  .phase::before { content: ""; position: absolute; left: -7px; top: 6px; width: 12px; height: 12px; border-radius: 50%; background: #fff; border: 2px solid var(--navy); }
  .phase .ph-meta { display: flex; flex-wrap: wrap; align-items: baseline; gap: 8px 14px; margin-bottom: 8px; }
  .phase .ph-n { font-family: var(--serif); font-style: italic; font-size: 1.05rem; color: var(--navy); }
  .phase .ph-time { font-size: .68rem; font-weight: 700; letter-spacing: 1.6px; text-transform: uppercase; color: var(--g600); border: 1px solid var(--g300); border-radius: 20px; padding: 3px 11px; }
  .phase h3 { margin: 0 0 8px; font-size: 1.22rem; }
  .phase p { font-size: .96rem; margin-bottom: 12px; }
  .phase p:last-child { margin-bottom: 0; }

  /* honorarios */
  .price { border: 1px solid var(--g200); border-radius: 10px; padding: 30px 26px; display: flex; flex-direction: column; position: relative; }
  .price.featured { border: 2px solid var(--navy); box-shadow: 0 18px 44px rgba(13,27,42,.09); }
  .price .tag { position: absolute; top: -12px; right: 20px; background: var(--navy); color: #fff; font-size: .66rem; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; padding: 5px 13px; border-radius: 20px; }
  .price h4 { font-family: var(--serif); font-size: 1.16rem; font-weight: 600; color: var(--navy); margin-bottom: 2px; }
  .price .amount { font-family: var(--serif); font-size: 2.5rem; font-weight: 700; color: var(--navy); line-height: 1.1; margin: 10px 0 2px; }
  .price .amount small { font-family: var(--sans); font-size: .76rem; font-weight: 400; color: var(--g600); display: block; letter-spacing: .3px; }
  .price ul { list-style: none; margin: 16px 0 0; }
  .price li { font-size: .9rem; padding: 8px 0 8px 24px; position: relative; border-bottom: 1px solid var(--g200); }
  .price li:last-child { border-bottom: none; }
  .price li::before { content: "✓"; position: absolute; left: 0; color: var(--navy); font-weight: 700; }

  /* FAQ */
  .faq { margin: 26px auto 0; max-width: var(--measure); border-top: 1px solid var(--g200); }
  .faq details { border-bottom: 1px solid var(--g200); }
  .faq summary { cursor: pointer; list-style: none; padding: 20px 44px 20px 0; position: relative; font-weight: 600; color: var(--navy); font-size: 1rem; line-height: 1.45; }
  .faq summary::-webkit-details-marker { display: none; }
  .faq summary::after { content: "+"; position: absolute; right: 6px; top: 50%; transform: translateY(-50%); font-family: var(--sans); font-weight: 400; font-size: 1.35rem; color: var(--g400); }
  .faq details[open] summary::after { content: "–"; }
  .faq .answer { padding: 0 40px 22px 0; font-size: .96rem; color: var(--g700); }
  .faq .answer p { margin-bottom: 12px; }
  .faq .answer p:last-child { margin-bottom: 0; }

  /* autor */
  .author { background: var(--g50); border: 1px solid var(--g200); border-radius: 8px; padding: 28px; display: flex; gap: 22px; align-items: center; margin: 56px auto 0; max-width: var(--measure); }
  .author .seal { width: 76px; flex-shrink: 0; font-family: var(--serif); font-weight: 600; font-size: 1.7rem; color: #fff; background: var(--navy); border-radius: 50%; aspect-ratio: 1; display: grid; place-items: center; letter-spacing: -.5px; }
  .author h4 { font-family: var(--serif); font-size: 1.1rem; color: var(--navy); margin-bottom: 2px; }
  .author .role { font-size: .74rem; font-weight: 700; letter-spacing: 1.8px; text-transform: uppercase; color: var(--g600); margin-bottom: 8px; }
  .author p { font-size: .9rem; margin: 0; }
  @media (max-width: 620px) { .author { flex-direction: column; text-align: center; } }

  .sources { margin: 46px auto 0; max-width: var(--measure); border-top: 1px solid var(--g200); padding-top: 22px; }
  .sources h4 { font-size: .72rem; font-weight: 700; letter-spacing: 2.2px; text-transform: uppercase; color: var(--g600); margin-bottom: 12px; }
  .sources ul { list-style: none; font-size: .86rem; color: var(--g600); }
  .sources li { padding: 5px 0 5px 18px; position: relative; }
  .sources li::before { content: "§"; position: absolute; left: 0; color: var(--g400); }

  .disclaimer { margin: 40px auto 0; max-width: var(--measure); font-size: .82rem; color: var(--g600); line-height: 1.65; }

  /* CTA final */
  .final { background: linear-gradient(158deg, var(--navy-deep) 0%, var(--navy) 55%, var(--navy-2) 100%); color: #fff; padding: 72px 0; margin-top: 66px; }
  .final .wrap { max-width: 860px; }
  .final .eyebrow { color: var(--g400); }
  .final h2 { font-family: var(--serif); font-weight: 600; font-size: clamp(1.7rem, 4vw, 2.4rem); line-height: 1.2; margin: 14px 0 16px; letter-spacing: -.4px; }
  .final h2 em { font-style: italic; font-weight: 400; color: #C9D3DC; }
  .final p { color: rgba(255,255,255,.82); max-width: 580px; margin-bottom: 28px; }
  .final .hero-cta { margin-top: 0; }
  .final .fine { font-size: .8rem; color: rgba(255,255,255,.55); margin-top: 22px; margin-bottom: 0; }

  footer { background: var(--navy-deep); color: rgba(255,255,255,.66); padding: 52px 0 34px; font-size: .85rem; }
  footer .fgrid { display: grid; grid-template-columns: 1.4fr 1fr 1fr; gap: 34px; }
  footer .flogo { width: 190px; margin-bottom: 18px; }
  footer h5 { color: #fff; font-size: .72rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 14px; }
  footer a { color: rgba(255,255,255,.82); text-decoration: none; }
  footer a:hover { color: #fff; text-decoration: underline; }
  footer ul { list-style: none; }
  footer li { padding: 5px 0; }
  footer .fnote { border-top: 1px solid rgba(255,255,255,.12); margin-top: 34px; padding-top: 22px; font-size: .78rem; color: rgba(255,255,255,.5); line-height: 1.65; }
  @media (max-width: 800px) { footer .fgrid { grid-template-columns: 1fr; gap: 26px; } }

  a:focus-visible, summary:focus-visible, .btn:focus-visible { outline: 2px solid var(--navy); outline-offset: 3px; }
  .hero a:focus-visible, .final a:focus-visible { outline-color: #fff; }

  @media (prefers-reduced-motion: reduce) {
    html { scroll-behavior: auto; }
    .btn { transition: none; }
  }

  @media (max-width: 640px) {
    body { font-size: 16px; }
    .byline { gap: 4px 12px; }
    .byline .dot { display: none; }
    main { padding-top: 46px; }
    .sec { margin-top: 56px; }
    .hero { padding: 46px 0 52px; }
    .hero-logo { width: 168px; margin-bottom: 30px; }
    .author { padding: 22px; }
  }

  /* ============ impresión / PDF ============ */
  @media print {
    .topbar, .nav, .progress, .hero-cta, .final, .toc, .byline .dot { display: none !important; }
    body { font-size: 10.5pt; color: #111; line-height: 1.55; }
    .wrap { max-width: none; padding: 0; }
    .article > * { max-width: none; }
    .hero { background: #fff !important; color: #000; padding: 0 0 14px; border-bottom: 2px solid #0D1B2A; }
    .hero-logo { filter: invert(1) brightness(.2); width: 140px; margin-bottom: 18px; }
    .hero h1 { color: #0D1B2A; font-size: 25pt; max-width: none; }
    .hero h1 em { color: #1B3A57; }
    .hero .lead { color: #222; max-width: none; }
    .byline { color: #444; border-top: 1px solid #ccc; padding-top: 12px; }
    .byline strong { color: #000; }
    a { color: #000; text-decoration: none; }
    .sec { margin-top: 22px; page-break-inside: auto; }
    .sec-head, .sec h3, .article h3 { page-break-after: avoid; }
    .sec h2 { font-size: 17pt; }
    .sec h3 { font-size: 12.5pt; margin-top: 20px; }
    .table-wrap {
      width: auto !important; max-width: 100% !important;
      margin: 12px 0 16px !important; overflow: visible; border: 1px solid #ccc;
    }
    table { min-width: 0; font-size: 9pt; }
    thead { display: table-header-group; }
    tbody tr, .callout, .card, .price, .phase, .faq details, .quote, .author { page-break-inside: avoid; }
    .cards-3, .cards-2 { width: auto !important; max-width: 100% !important; margin: 12px 0 16px !important; gap: 10px; }
    .card, .price { padding: 14px 14px; }
    .faq details .answer { display: block !important; }
    .faq { max-width: none; }
    .final { display: none !important; }
    footer { background: #fff; color: #333; border-top: 1px solid #ccc; padding-top: 14px; }
    footer h5, footer a { color: #000; }
    footer .flogo { filter: invert(1) brightness(.2); width: 150px; }
    footer .fnote { color: #555; }
    .disclaimer { font-size: 8pt; }
  }
</style>
</head>
<body>

<div class="topbar">
  <div class="wrap">
    <span><strong>Naturalízate.pa</strong> · Scotia Plaza, Piso 7. Av. Federico Boyd, Panamá</span>
    <span>WhatsApp <a href="__WA__" target="_blank" rel="noopener">+507 6255-7583</a> · Lun–Vie 8:00 a.m. – 5:00 p.m.</span>
  </div>
</div>

<header class="nav">
  <div class="wrap">
    <a class="nav-logo" href="__SITE__" aria-label="Naturalízate.pa — inicio">
      <img src="data:image/svg+xml;base64,__LOGO_NAVY__" alt="Naturalízate.pa" width="172" height="23" />
    </a>
    <nav class="nav-links" aria-label="Navegación de la guía">
      <a href="#fundamentos">Fundamentos</a>
      <a href="#etapas">Proceso</a>
      <a href="#costos">Honorarios</a>
      <a href="#preguntas">Preguntas</a>
      <a class="nav-cta" href="__WA__" target="_blank" rel="noopener"><span class="cta-long">Precalificar mi caso</span><span class="cta-short">Precalificar</span></a>
    </nav>
  </div>
</header>
<div class="progress" aria-hidden="true"><span id="bar"></span></div>

<section class="hero">
  <div class="wrap">
    <img class="hero-logo" src="data:image/svg+xml;base64,__LOGO_WHITE__" alt="Naturalízate.pa" width="208" height="28" />
    <div class="kicker">Guía completa · Actualizada en noviembre de 2026</div>
    <h1>Naturalización panameña: de la Cédula&nbsp;E a la <em>nacionalidad</em></h1>
    <p class="lead">Las vías reales, los requisitos documentales que el expediente exige, las cuatro fases ante el Estado, los tiempos que conviene prever y las decisiones que hay que tomar antes de firmar un poder. Escrita desde la práctica del despacho, no desde el folleto.</p>
    <div class="byline">
      <span>Por <strong>Lic. Alfonso Villarreal</strong>, abogado fundador</span>
      <span class="dot"></span>
      <span>Naturalízate.pa · Ciudad de Panamá</span>
      <span class="dot"></span>
      <span>Lectura de 14 minutos</span>
    </div>
    <div class="hero-cta">
      <a class="btn btn-white" href="__WA__" target="_blank" rel="noopener">Precalificar mi caso · 60 seg</a>
      <a class="btn btn-outline-w" href="#contenido">Ver el contenido</a>
    </div>
  </div>
</section>

<section class="toc" id="contenido" aria-label="Índice de la guía">
  <div class="wrap">
    <div class="eyebrow">Índice</div>
    <div class="toc-grid">
      <a href="#introduccion"><span>·</span><span>Introducción: la decisión y el método</span></a>
      <a href="#fundamentos"><span>1</span><span>Fundamentos legales y quién califica</span></a>
      <a href="#requisitos"><span>2</span><span>Requisitos documentales y solvencia</span></a>
      <a href="#etapas"><span>3</span><span>Las cuatro fases del proceso</span></a>
      <a href="#costos"><span>4</span><span>Costos, honorarios y qué no incluyen</span></a>
      <a href="#beneficios"><span>5</span><span>Qué cambia cuando se es panameño</span></a>
      <a href="#errores"><span>6</span><span>Errores que cuestan años</span></a>
      <a href="#preguntas"><span>7</span><span>Preguntas frecuentes</span></a>
    </div>
  </div>
</section>

<main>
  <div class="wrap">
    <article class="article">

      <section id="introduccion">
        <div class="sec-head">
          <div class="num">Introducción</div>
          <h2>Un acto soberano, no un <em>trámite automático</em></h2>
        </div>
        <p class="intro-first">Convertirse en ciudadano de un país que no es el de nacimiento es una de las decisiones jurídicas más importantes que una persona puede tomar. En Panamá, ese camino tiene nombre técnico —naturalización— y un documento que lo formaliza: la <strong>Carta de Naturaleza</strong>. No es un derecho que se active solo por cumplir años de residencia: es una facultad del Estado, que se ejerce a través de un procedimiento reglado, documentado y discrecional.</p>
        <p>Por eso esta guía no empieza por los papeles, sino por lo que la ley exige y por el orden en que conviene hacer las cosas. La mayoría de los expedientes que se retrasan no fallan por falta de mérito: fallan por un documento vencido, una ausencia no declarada, una solvencia mal acreditada o un examen subestimado. Cada uno de esos puntos es evitable, y evitarlos es exactamente el trabajo previo del abogado.</p>
        <p>La guía está pensada para residentes permanentes con Cédula E que ya cumplen —o están por cumplir— el tiempo de residencia, y para quienes desean entender el proceso completo antes de comprometer tiempo y dinero.</p>

        <div class="callout">
          <span class="label">Cómo leer esta guía</span>
          <p>Describimos el marco legal vigente y la práctica del despacho. No prometemos resultados: la decisión final corresponde al Estado panameño. Cada caso se evalúa con sus propios documentos, y ninguna guía —tampoco esta— sustituye una revisión profesional del expediente.</p>
        </div>
      </section>

      <section class="sec" id="fundamentos">
        <div class="sec-head">
          <div class="num">01 · Elegibilidad</div>
          <h2>Fundamentos legales y quién <em>califica</em></h2>
        </div>
        <p>La naturalización panameña se rige por la <strong>Constitución Política de la República de Panamá</strong> —artículos 9 a 14— y por la legislación y la práctica administrativa que la desarrollan. De ese bloque normativo salen tres preguntas que conviene responder por escrito, con documentos en mano, antes de presentar cualquier solicitud: cuál es la vía aplicable, cuándo se cumple el tiempo de residencia y si el arraigo se sostiene.</p>

        <h3>1.1 · Las tres vías y el tiempo de residencia exigido</h3>
        <p>El requisito central es el tiempo de <strong>residencia permanente ininterrumpida y comprobada</strong> en el territorio nacional, acreditada con la cédula de residente permanente (Cédula E). La ley contempla tres caminos:</p>

        <div class="table-wrap">
          <table>
            <caption class="t-small" style="text-align:left;padding:12px 20px 0;caption-side:top;">Vías de naturalización y residencia mínima exigida</caption>
            <thead>
              <tr><th scope="col">Vía</th><th scope="col">A quién aplica</th><th scope="col">Residencia mínima</th></tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">Requisitos generales</th>
                <td>Residentes permanentes en general.</td>
                <td class="num-cell">5 años</td>
              </tr>
              <tr>
                <th scope="row">Reciprocidad</th>
                <td>Nacionales de países con convenio o tratado de reciprocidad con Panamá.</td>
                <td>
                  <strong>1 año:</strong> El Salvador.<br />
                  <strong>2 años:</strong> Argentina, Colombia, Ecuador, España, Honduras, México, Nicaragua y Perú.<br />
                  <strong>3 años:</strong> Uruguay.
                </td>
              </tr>
              <tr>
                <th scope="row">Vínculo familiar</th>
                <td>Casados con nacional panameño/a, o con hijos de padre o madre panameños.</td>
                <td class="num-cell">3 años</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="callout">
          <span class="label">Punto de partida del cómputo</span>
          <p>El tiempo se cuenta desde la <strong>residencia permanente</strong>. La fecha de emisión de la Cédula E suele reflejarla, pero si hubo cambios de categoría migratoria, interrupciones o periodos fuera del país, manda el historial migratorio completo. Ese cómputo se verifica con las constancias en mano, no de memoria.</p>
        </div>

        <h3>1.2 · Requisitos de fondo</h3>
        <p>Además del tiempo de residencia, el solicitante debe sostener ante la autoridad un perfil completo. Estos son los seis frentes que se evalúan:</p>

        <ul class="check clean" style="max-width:var(--measure);">
          <li><strong>Mayoría de edad.</strong> El trámite es personal; los menores deben esperar a cumplirla.</li>
          <li><strong>Renuncia a la nacionalidad de origen.</strong> La jura incluye la renuncia. Panamá no reconoce, en principio, la doble nacionalidad; existen convenios bilaterales y reglas propias en cada país de origen que conviene revisar antes de iniciar.</li>
          <li><strong>Solvencia económica.</strong> Medios de vida lícitos y demostrables: declaraciones de renta, cartas bancarias, cartas de trabajo, fichas del seguro social, propiedades o inversiones.</li>
          <li><strong>Conocimiento cívico.</strong> Dominio del español y conocimientos de historia, geografía, gobierno y cultura de Panamá, verificados en el examen de naturalización.</li>
          <li><strong>Conducta y solvencia moral.</strong> Antecedentes penales limpios en Panamá y en los países donde haya residido en los últimos años.</li>
          <li><strong>Arraigo real.</strong> Vida efectiva en Panamá: residencia continua, vínculos patrimoniales, laborales y familiares, cumplimiento de obligaciones fiscales y de seguridad social.</li>
        </ul>

        <p>Hay un punto que suele subestimarse: la naturalización exige que el solicitante <em>haga vida en Panamá</em>. Tener la residencia permanente vigente y, a la vez, pasar la mayor parte del año fuera del país es una contradicción que el expediente no puede explicar por sí solo. Si su situación es esa, conviene ordenarla antes de presentar.</p>

        <blockquote class="quote">«No asumimos expedientes que no cumplan la ley. Cuando procedemos, lo hacemos con la convicción de quien comprende que cada decisión migratoria afecta el rumbo completo de una vida.»<cite>Lic. Alfonso Villarreal</cite></blockquote>
      </section>

      <section class="sec" id="requisitos">
        <div class="sec-head">
          <div class="num">02 · Expediente</div>
          <h2>Requisitos documentales y la regla de <em>solvencia</em></h2>
        </div>
        <p>El expediente es la parte del proceso que más control tiene el solicitante y la que más tiempo ahorra cuando se hace bien. La regla práctica es simple: ningún documento se presenta sin haber sido verificado dos veces —vigencia, forma de emisión, autenticación y traducción cuando corresponde.</p>

        <h3>2.1 · Documentos que integran el expediente</h3>
        <p>La composición exacta depende de cada caso, pero el núcleo documental es este:</p>

        <div class="table-wrap">
          <table>
            <thead>
              <tr><th scope="col">Documento</th><th scope="col">Detalle que suele fallar</th></tr>
            </thead>
            <tbody>
              <tr><th scope="row">Cédula E vigente y su copia autenticada</th><td>Se presenta vencida o sin autenticación notarial.</td></tr>
              <tr><th scope="row">Resolución de residencia permanente</th><td>Copia sin autenticar; datos que no coinciden con la cédula.</td></tr>
              <tr><th scope="row">Antecedentes penales de Panamá</th><td>Emitido fuera del plazo de vigencia exigido.</td></tr>
              <tr><th scope="row">Antecedentes penales del exterior</th><td>Sin apostilla, sin legalización consular o sin traducción oficial al español.</td></tr>
              <tr><th scope="row">Certificación de movimientos migratorios</th><td>Ausencias que el expediente no explica ni documenta.</td></tr>
              <tr><th scope="row">Pruebas de solvencia económica (2 de 3)</th><td>Documentos que no están dirigidos a la autoridad correcta o con firmas sin autenticar.</td></tr>
              <tr><th scope="row">Paz y salvo de la DGI</th><td>Solicitado al final, cuando debía tramitarse al inicio.</td></tr>
              <tr><th scope="row">Certificado de nacimiento y, si aplica, de matrimonio</th><td>Sin traducción oficial ni apostilla del país emisor.</td></tr>
              <tr><th scope="row">Pasaporte de origen</th><td>Próximo a vencer o sin legalización ante consulado.</td></tr>
              <tr><th scope="row">Fotografías recientes tamaño pasaporte</th><td>Formato o vestimenta que no cumple el requisito.</td></tr>
              <tr><th scope="row">Poder notarial al abogado</th><td>Redactado con facultades insuficientes para actuar en todas las fases.</td></tr>
            </tbody>
          </table>
        </div>

        <div class="callout warn">
          <span class="label">Documentos extranjeros</span>
          <p>Todo documento emitido fuera de Panamá debe estar <strong>apostillado</strong> conforme al Convenio de La Haya o <strong>legalizado por vía consular</strong>, y los que estén en otro idioma requieren <strong>traducción oficial al español</strong>. Este es el rubro que más retrasa expedientes, porque depende de terceros en otro país: se inicia primero, no al final.</p>
        </div>

        <h3>2.2 · Solvencia económica: basta con dos de tres pruebas</h3>
        <p>La regla es clara y no exige presentar las tres opciones: se eligen <strong>dos (2) de las tres pruebas</strong> documentales. Conviene escoger las que su situación real pueda sostener sin fabricar nada.</p>

        <div class="cards-3">
          <div class="card">
            <div class="step">01</div>
            <h4>Declaración de renta</h4>
            <ul>
              <li>De los <strong>dos últimos períodos fiscales</strong> anteriores a la presentación</li>
              <li>Con certificado de recepción ante la DGI</li>
              <li>Firmada por Contador Público Autorizado y autenticada por notario</li>
              <li>Si es copia, debidamente notariada</li>
            </ul>
          </div>
          <div class="card">
            <div class="step">02</div>
            <h4>Carta bancaria</h4>
            <ul>
              <li>Dirigida al <strong>Servicio Nacional de Migración</strong></li>
              <li>De <strong>cuatro cifras medias</strong> en adelante</li>
              <li>Firmada y con sello fresco del banco</li>
              <li>Vigencia máxima de <strong>30 días</strong> al presentarse</li>
            </ul>
          </div>
          <div class="card">
            <div class="step">03</div>
            <h4>Carta de trabajo + ficha CSS</h4>
            <ul>
              <li>Dirigida al <strong>Servicio Nacional de Migración</strong></li>
              <li>Firmada por el representante legal o empleador autorizado</li>
              <li>Con <strong>ficha actualizada</strong> de la Caja de Seguro Social</li>
            </ul>
          </div>
        </div>

        <p>Si el solicitante es dependiente familiar —por ejemplo, ama de casa o estudiante— puede aplicar presentando <strong>carta de responsabilidad notariada</strong> junto con dos de las tres pruebas de su garante responsable.</p>
      </section>

      <section class="sec" id="etapas">
        <div class="sec-head">
          <div class="num">03 · Proceso</div>
          <h2>Las cuatro fases ante el <em>Estado</em></h2>
        </div>
        <p>El trámite avanza por entidades distintas, cada una con su propio ritmo. Conocer la secuencia evita dos errores frecuentes: exigirle al proceso una velocidad que no tiene y descuidar el expediente justo cuando depende de una respuesta que no se está vigilando.</p>

        <div class="phase">
          <div class="ph-meta"><span class="ph-n">Fase I</span><span class="ph-time">4 – 8 semanas</span></div>
          <h3>Evaluación y armado del expediente</h3>
          <p>Antes de presentar, se audita la viabilidad: antigüedad de la Cédula E, continuidad de la residencia, arraigo, solvencia y antecedentes. Se confecciona la lista personalizada de documentos, se redacta el poder notarial y se arma el legajo con revisión folio por folio.</p>
          <p>En esta fase se decide si conviene presentar ahora o regularizar primero. Es la etapa más barata del proceso y la que más años ahorra.</p>
        </div>

        <div class="phase">
          <div class="ph-meta"><span class="ph-n">Fase II</span><span class="ph-time">6 – 12 meses</span></div>
          <h3>Radicación y trámite ante Migración</h3>
          <p>Se presenta formalmente la solicitud mediante abogado, con el expediente completo en original y copias autenticadas, y se cubren los aranceles correspondientes. El solicitante recibe un número de expediente para seguimiento y puede ser convocado a entrevista personal.</p>
          <p>Durante estos meses el expediente se verifica. Cualquier requerimiento debe atenderse dentro del plazo: una solicitud sin respuesta puede demorar el trámite meses o, en el peor escenario, cerrarlo.</p>
        </div>

        <div class="phase">
          <div class="ph-meta"><span class="ph-n">Fase III</span><span class="ph-time">6 – 10 meses</span></div>
          <h3>Tribunal Electoral y examen de naturalización</h3>
          <p>Superada la etapa anterior, el caso pasa al <strong>Tribunal Electoral</strong>, donde se evalúa el conocimiento cívico. El examen cubre español, historia, geografía, gobierno y cultura de Panamá, y puede complementarse con una entrevista.</p>
          <p>La preparación no es un formalismo. Un examen no superado retrasa el proceso completo y consume una convocatoria. Prepararse con tiempo, con material adecuado y con simulacros es parte del trabajo, no un extra.</p>
        </div>

        <div class="phase">
          <div class="ph-meta"><span class="ph-n">Fase IV</span><span class="ph-time">6 – 14 meses</span></div>
          <h3>Resolución, juramentación e inscripción</h3>
          <p>Aprobado el expediente, se emite la <strong>Carta de Naturaleza</strong> y se coordina la juramentación ante la Gobernación. La jura es un acto solemne: allí se declara lealtad a Panamá y se formaliza la renuncia a la nacionalidad de origen cuando corresponde.</p>
          <p>Después de la jura se inscriben la <strong>cédula panameña</strong> ante el Tribunal Electoral y se solicita el <strong>pasaporte panameño</strong>. La Modalidad Integral del despacho acompaña también esta etapa posterior.</p>
        </div>

        <div class="callout">
          <span class="label">Plazo total de referencia</span>
          <p>Con un expediente íntegro, el plazo habitual del despacho es de <strong>19 a 22 meses</strong>. No es una promesa: es una estimación basada en la carga del Tribunal Electoral y del Órgano Ejecutivo. Con requerimientos evitables, el plazo se extiende sin límite previsible.</p>
        </div>
      </section>

      <section class="sec" id="costos">
        <div class="sec-head">
          <div class="num">04 · Inversión</div>
          <h2>Costos, honorarios y <em>qué no incluyen</em></h2>
        </div>
        <p>Un proceso de casi dos años debe empezar con una cifra cierta. Los honorarios del despacho son <strong>fijos y por escrito</strong>, con pago fraccionado contra avance de fases. Lo que varía —y conviene saber desde el primer día— son los gastos del Estado y los documentos emitidos en el exterior.</p>

        <div class="cards-2">
          <div class="price">
            <h4>Modalidad <span style="font-style:italic;font-weight:400;">Esencial</span></h4>
            <div class="amount">$3,800<small>honorarios totales · pago fraccionado</small></div>
            <ul>
              <li>Evaluación y revisión jurídica del caso</li>
              <li>Integración y presentación del expediente</li>
              <li>Seguimiento ante el Tribunal Electoral</li>
              <li>Preparación para entrevista y examen</li>
              <li>Comunicación directa con el abogado</li>
            </ul>
          </div>
          <div class="price featured">
            <span class="tag">Recomendada</span>
            <h4>Modalidad <span style="font-style:italic;font-weight:400;">Integral</span></h4>
            <div class="amount">$5,500<small>delegación total · pago fraccionado</small></div>
            <ul>
              <li>Todo lo incluido en la Modalidad Esencial</li>
              <li>Coordinación de poderes y cartas poder</li>
              <li>Gestión notarial y legalizaciones completas</li>
              <li>Acompañamiento posterior a la jura (cédula y pasaporte)</li>
              <li>Recursos y apelaciones si el Tribunal lo requiere</li>
              <li>Prioridad en agenda y respuesta</li>
            </ul>
          </div>
        </div>

        <h3>4.1 · Gastos que no son honorarios</h3>
        <div class="table-wrap">
          <table>
            <thead>
              <tr><th scope="col">Rubro</th><th scope="col">Qué cubre</th><th scope="col">Cómo se maneja</th></tr>
            </thead>
            <tbody>
              <tr><th scope="row">Tasas y aranceles del Estado</th><td>Timbres, derechos, certificaciones y publicaciones oficiales.</td><td>Se detallan por escrito y se cubren según se causen.</td></tr>
              <tr><th scope="row">Documentos del exterior</th><td>Apostillas, legalizaciones consulares y traducciones oficiales.</td><td>Variables según el país emisor; se presupuestan al inicio.</td></tr>
              <tr><th scope="row">Gestiones notariales</th><td>Poderes, autenticaciones y cartas de responsabilidad.</td><td>Incluidas en la Modalidad Integral; en la Esencial las asume el cliente.</td></tr>
            </tbody>
          </table>
        </div>

        <div class="callout warn">
          <span class="label">Señal de alerta</span>
          <p>Desconfíe de quien ofrece un precio irrealmente bajo o un resultado garantizado. En este trámite no existe la vía rápida: un expediente mal armado cuesta más —en tiempo y en dinero— que uno revisado antes de presentar. Nuestro orden es siempre el mismo: <strong>primero la viabilidad, después el compromiso</strong>. La precalificación y la consulta inicial son gratuitas; no se paga nada antes de evaluar el caso.</p>
        </div>
      </section>

      <section class="sec" id="beneficios">
        <div class="sec-head">
          <div class="num">05 · Beneficios</div>
          <h2>Qué cambia cuando se es <em>panameño</em></h2>
        </div>
        <p>La nacionalidad no equivale a una residencia mejorada: cambia la relación jurídica con el país. Estos son los efectos concretos que evalúan quienes deciden iniciar.</p>

        <ul class="clean check">
          <li><strong>Derechos políticos plenos.</strong> Votar y ser postulado para cargos públicos, salvo las excepciones constitucionales.</li>
          <li><strong>Profesiones y cargos reservados.</strong> Acceder a actividades que la Constitución reserva a los panameños, como la abogacía, la medicina o la ingeniería, y a cargos del sector público.</li>
          <li><strong>Pasaporte panameño.</strong> Acceso sin visa o con visa a la llegada a más de 140 países y territorios, según los índices internacionales de pasaportes.</li>
          <li><strong>Permanencia incondicional.</strong> Se termina la dependencia de la residencia permanente y de los trámites migratorios recurrentes, como la renovación de permisos de trabajo.</li>
          <li><strong>Acceso educativo.</strong> Programas de becas y de cooperación internacional reservados a nacionales, y matrícula en universidades públicas en las condiciones del país.</li>
          <li><strong>Oportunidades económicas.</strong> Programas de apoyo a emprendedores panameños, contratación pública sin restricciones y acceso a crédito en condiciones locales.</li>
          <li><strong>Beneficios familiares.</strong> Los hijos nacidos después de la naturalización son panameños, y los procesos migratorios de familiares directos se simplifican.</li>
        </ul>

        <p>Hay un beneficio que no aparece en las listas y que suele ser el decisivo: la certeza. Dejar de estar sujeto a la renovación de una condición migratoria, a una fecha de vencimiento y a la autoridad de un trámite periódico.</p>
      </section>

      <section class="sec" id="errores">
        <div class="sec-head">
          <div class="num">06 · Riesgos</div>
          <h2>Los errores que cuestan <em>años</em>, no semanas</h2>
        </div>
        <p>Casi todos los expedientes que se complican caen en uno de estos cinco patrones. Ninguno requiere mala fe: basta la prisa o la información de segunda mano.</p>

        <ol class="clean">
          <li><strong>Interrumpir la residencia efectiva.</strong> Ausencias prolongadas o no justificadas contradicen el arraigo exigido. La residencia permanente puede estar vigente y, aun así, el expediente no explicar por sí solo por qué la vida transcurre fuera de Panamá.</li>
          <li><strong>Presentar documentos vencidos o mal autenticados.</strong> Una cédula a punto de expirar, un antecedente penal fuera de plazo, una carta bancaria con más de 30 días o una traducción sin sello oficial devuelven el expediente a la casilla de salida.</li>
          <li><strong>Subestimar el examen de naturalización.</strong> Evalúa español, historia, geografía, gobierno y cultura. No superarlo no es un detalle administrativo: retrasa el proceso completo.</li>
          <li><strong>Omitir o falsificar información.</strong> Ocultar un antecedente o un historial migratorio complejo puede ocasionar el rechazo inmediato, y compromete cualquier intento posterior.</li>
          <li><strong>Contratar sin evaluación previa.</strong> Aceptar un trámite sin auditar la viabilidad es pagar por una incertidumbre. Un expediente no se arma por partes ni sobre la marcha.</li>
        </ol>

        <div class="callout">
          <span class="label">La regla de oro</span>
          <p>El expediente se arma en un solo sentido: <strong>primero la viabilidad, después el compromiso</strong>. Si un caso no procede, decirlo por escrito —y con fundamento— es parte del trabajo profesional, no una pérdida de oportunidad.</p>
        </div>
      </section>

      <section class="sec" id="preguntas">
        <div class="sec-head">
          <div class="num">07 · Dudas</div>
          <h2>Preguntas <em>frecuentes</em></h2>
        </div>

        <div class="faq">
          <details>
            <summary>¿Basta tener la Cédula E para naturalizarme?</summary>
            <div class="answer"><p>No por sí sola. La Cédula E acredita su condición migratoria, pero la ley exige además los cinco años de residencia, el arraigo, la conducta y la integración. Su antigüedad es el punto de partida de la evaluación, no la garantía del resultado.</p></div>
          </details>
          <details>
            <summary>¿Desde cuándo se cuentan los cinco años?</summary>
            <div class="answer">
              <p>El período se cuenta por la residencia permanente mantenida en Panamá. La fecha de emisión de la cédula suele reflejarla, pero si hubo cambios de categoría o interrupciones, el historial migratorio manda.</p>
              <p><strong>Excepción por reciprocidad:</strong> los nacionales de El Salvador requieren 1 año; los de Argentina, Colombia, Ecuador, España, Honduras, México, Nicaragua y Perú, 2 años; y los de Uruguay, 3 años.</p>
            </div>
          </details>
          <details>
            <summary>¿Cuánto cuesta naturalizarse en Panamá?</summary>
            <div class="answer"><p>Los honorarios del despacho son fijos y por escrito: <strong>$3,800</strong> en la Modalidad Esencial y <strong>$5,500</strong> en la Integral, ambas con pago fraccionado contra avance de fases. Las tasas del Estado, apostillas, legalizaciones y traducciones se detallan por separado antes de iniciar, para que la cifra final no le sorprenda a mitad de camino.</p></div>
          </details>
          <details>
            <summary>¿Qué exige el examen del Tribunal Electoral?</summary>
            <div class="answer"><p>Conocimientos de español, historia, geografía, gobierno y cultura de Panamá. Es un requisito serio: no superarlo retrasa el proceso. Conviene prepararse con tiempo y material adecuado antes de la convocatoria.</p></div>
          </details>
          <details>
            <summary>¿Puedo perder mi nacionalidad de origen?</summary>
            <div class="answer"><p>La jura de naturalización incluye renunciar a la nacionalidad de origen. Además, el panameño naturalizado que adquiere voluntariamente otra nacionalidad puede perder la panameña (artículo 14 de la Constitución). Verifique también las reglas de su país de origen: algunos admiten la doble nacionalidad por convenio y otros la rechazan al recibir la renuncia.</p></div>
          </details>
          <details>
            <summary>¿Necesito un abogado en Panamá?</summary>
            <div class="answer"><p>Sí. La solicitud de naturalización se presenta mediante abogado ante el Tribunal Electoral. El acompañamiento profesional es parte del trámite, no un servicio opcional.</p></div>
          </details>
          <details>
            <summary>¿Cuánto tarda el proceso completo?</summary>
            <div class="answer"><p>Depende de la carga del Tribunal Electoral y del Órgano Ejecutivo, y de la integridad del expediente. Nuestro plazo habitual es de <strong>19 a 22 meses</strong>. No prometemos plazos: los estimamos por escrito después de revisar su caso.</p></div>
          </details>
          <details>
            <summary>¿La consulta inicial tiene algún costo?</summary>
            <div class="answer"><p>No. La precalificación y la consulta inicial son gratuitas y sin compromiso. Recibe un veredicto de viabilidad por escrito en 48 horas hábiles. Solo si su caso procede y usted decide continuar aplican honorarios fijos por escrito, con pago fraccionado.</p></div>
          </details>
          <details>
            <summary>¿Puedo pagar los honorarios por partes?</summary>
            <div class="answer"><p>Sí. Ambas modalidades contemplan pago fraccionado contra avance de fases, acordado por escrito desde el inicio. Lo que no varía es el monto total: honorarios fijos, sin cargos posteriores no pactados.</p></div>
          </details>
          <details>
            <summary>¿Qué pasa si el Tribunal emite un requerimiento o niega mi caso?</summary>
            <div class="answer"><p>Nuestra pre-auditoría documental existe justamente para evitarlo. Si el Tribunal emite un requerimiento subsanable, la Modalidad Integral incluye la preparación de los recursos procedentes sin honorarios adicionales. La decisión del Estado no se promete; el rigor técnico, sí.</p></div>
          </details>
          <details>
            <summary>¿Qué ocurre si mi caso no califica?</summary>
            <div class="answer"><p>Se lo indicamos por escrito en la consulta inicial, con su fundamento, y no le proponemos el trámite. Usted conserva el informe con la ruta de lo que debería regularizar antes de intentarlo.</p></div>
          </details>
        </div>
      </section>

      <section class="sec" id="cierre">
        <div class="sec-head">
          <div class="num">Cierre</div>
          <h2>El primer paso no es el formulario: es <em>saber si procede</em></h2>
        </div>
        <p>La naturalización panameña es un proceso largo y perfectamente ordenable. La diferencia entre un expediente que avanza y uno que se estanca casi nunca está en el mérito del solicitante, sino en la preparación: documentos vigentes, solvencia bien acreditada, residencia consistente, examen preparado y un seguimiento constante de cada etapa.</p>
        <p>Si ya cuenta con Cédula E y quiere saber si su caso se sostiene, el punto de partida es una evaluación previa, por escrito y sin costo. Es también la forma más honesta de empezar: antes de invertir en un trámite, saber si conviene hacerlo.</p>

        <div class="author">
          <div class="seal" aria-hidden="true">AV</div>
          <div>
            <h4>Lic. Alfonso Villarreal</h4>
            <div class="role">Abogado fundador · Naturalízate.pa</div>
            <p>Especialista en derecho migratorio panameño. Su práctica se concentra en la naturalización de residentes permanentes: evaluación de viabilidad, constitución del expediente y acompañamiento hasta la jura y la cédula. Scotia Plaza, Piso 7. Av. Federico Boyd, Ciudad de Panamá.</p>
          </div>
        </div>

        <div class="sources">
          <h4>Fuentes y verificación</h4>
          <ul>
            <li>Constitución Política de la República de Panamá, artículos 9 a 14.</li>
            <li>Servicio Nacional de Migración — requisitos y trámites migratorios.</li>
            <li>Tribunal Electoral — cedulación y examen de naturalización.</li>
            <li>Dirección General de Ingresos — paz y salvo y declaraciones de renta.</li>
            <li>Caja de Seguro Social — ficha de asegurado.</li>
            <li>Índices internacionales de pasaportes, para la referencia de movilidad.</li>
          </ul>
        </div>

        <p class="disclaimer">Aviso legal: esta guía es de carácter general y no constituye asesoría legal para un caso particular. Naturalízate.pa es una práctica jurídica privada, independiente de cualquier entidad del Estado panameño. La decisión de naturalización corresponde soberanamente al Estado a través del Tribunal Electoral y del Órgano Ejecutivo. No se garantizan resultados. Los plazos y montos citados son estimaciones de referencia y se confirman por escrito tras evaluar cada expediente. Contenido actualizado en noviembre de 2026.</p>
      </section>

    </article>
  </div>

  <section class="final">
    <div class="wrap">
      <div class="eyebrow">Consulta inicial gratuita · 60 segundos</div>
      <h2>¿Su caso sostiene una solicitud? <em>Conviene saberlo antes de invertir.</em></h2>
      <p>Precalificación en un minuto, veredicto de viabilidad por escrito y una conversación directa con el abogado. Sin costo y sin compromiso.</p>
      <div class="hero-cta">
        <a class="btn btn-white" href="__SITE__" target="_blank" rel="noopener">Precalificar mi caso</a>
        <a class="btn btn-wa" href="__WA__" target="_blank" rel="noopener">Hablar por WhatsApp</a>
      </div>
      <p class="fine">Sin pagos por adelantado. Solo si su caso procede y usted decide continuar aplican honorarios fijos por escrito.</p>
    </div>
  </section>
</main>

<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <img class="flogo" src="data:image/svg+xml;base64,__LOGO_WHITE__" alt="Naturalízate.pa" width="190" height="25" />
        <p style="max-width:34ch;">Derecho migratorio especializado en Panamá. Discreción, rigor jurídico y acompañamiento integral hasta la jura de nacionalidad.</p>
      </div>
      <div>
        <h5>Contacto</h5>
        <ul>
          <li><a href="__WA__" target="_blank" rel="noopener">WhatsApp · +507 6255-7583</a></li>
          <li><a href="mailto:Villarreallawyers@proton.me">Villarreallawyers@proton.me</a></li>
          <li>Scotia Plaza, Piso 7.<br />Av. Federico Boyd, Panamá</li>
          <li>Lun–Vie · 8:00 a.m. – 5:00 p.m.</li>
        </ul>
      </div>
      <div>
        <h5>Enlaces</h5>
        <ul>
          <li><a href="__SITE__">Página principal</a></li>
          <li><a href="__SITE__#honorarios">Honorarios</a></li>
          <li><a href="__SITE__#preguntas">Preguntas frecuentes</a></li>
          <li><a href="__SITE__#precalificar">Precalificar mi caso</a></li>
        </ul>
      </div>
    </div>
    <div class="fnote">
      © 2026 Naturalízate.pa · Lic. Alfonso Villarreal · Scotia Plaza, Piso 7. Av. Federico Boyd, Panamá, Provincia de Panamá.<br />
      Guía informativa de carácter general; no constituye asesoría legal para un caso particular y no garantiza resultados. La información de este sitio no sustituye la consulta con un abogado idóneo.
    </div>
  </div>
</footer>

<script>
  (function () {
    var bar = document.getElementById('bar');
    function update() {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      var pct = max > 0 ? (h.scrollTop || document.body.scrollTop) / max * 100 : 0;
      bar.style.width = Math.min(100, Math.max(0, pct)) + '%';
    }
    document.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
    update();

    /* Al imprimir o guardar como PDF, las respuestas del FAQ se muestran completas */
    window.addEventListener('beforeprint', function () {
      document.querySelectorAll('details').forEach(function (d) {
        if (!d.open) { d.setAttribute('data-was-closed', '1'); d.open = true; }
      });
    });
    window.addEventListener('afterprint', function () {
      document.querySelectorAll('details[data-was-closed]').forEach(function (d) {
        d.open = false; d.removeAttribute('data-was-closed');
      });
    });
  })();
</script>
</body>
</html>
"""

html = (
    HTML.replace("__FONT_INTER__", FONT_INTER)
    .replace("__FONT_PLAYFAIR_IT__", FONT_PLAYFAIR_IT)
    .replace("__FONT_PLAYFAIR__", FONT_PLAYFAIR)
    .replace("__LOGO_NAVY__", LOGO_NAVY)
    .replace("__LOGO_WHITE__", LOGO_WHITE)
    .replace("__WA__", WA + WA_TEXT)
    .replace("__SITE__", SITE)
)

OUT.write_text(html, encoding="utf-8")
print(f"OK → {OUT} ({OUT.stat().st_size/1024:.0f} KB)")
