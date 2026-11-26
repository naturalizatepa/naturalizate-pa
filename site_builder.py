"""Generate the publishable static pages from shared brand and navigation markup."""

from html import escape
from pathlib import Path

from pages_content import FAQ, PAGES, WHATSAPP

ROOT = Path(__file__).resolve().parent
GUIDE = "guia.html"
MAP = "https://www.google.com/maps/search/?api=1&amp;query=Scotia+Plaza+Piso+7+Av+Federico+Boyd+Panama"
SITE = "https://naturalizatepa.github.io/naturalizate-pa/"


def nav_link(href, label, active, key):
    current = ' aria-current="page"' if active == key else ""
    return f'<a class="nav-link" href="{href}"{current}>{label}</a>'


def dropdown(href, label, key, active, links, identifier):
    current = ' aria-current="page"' if active == key else ""
    entries = "\n".join(f'<a href="{url}"{extra}>{name}</a>' for url, name, extra in links)
    return f'''<div class="nav-item has-dropdown" data-dropdown>
      <a class="nav-link" href="{href}"{current}>{label}</a>
      <button class="nav-caret" type="button" aria-label="Abrir submenú de {label}" aria-expanded="false" aria-controls="{identifier}">
        <svg viewBox="0 0 12 12" width="12" height="12" aria-hidden="true"><path d="m2 4.5 4 4 4-4" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" /></svg>
      </button>
      <div class="nav-panel" id="{identifier}">{entries}</div>
    </div>'''


def navigation(active):
    services = [
        ("servicios.html#evaluacion", "Evaluación de viabilidad", ""),
        ("servicios.html#expediente", "Preparación del expediente", ""),
        ("servicios.html#representacion", "Representación y seguimiento", ""),
        ("index.html#auditoria", "Auditoría Jurídica de Caso · US$49", ""),
    ]
    information = [
        ("informacion-legal.html#articulos", "Artículos y novedades", ""),
        ("informacion-legal.html#proceso", "Etapas del proceso", ""),
        ("informacion-legal.html#enlaces-oficiales", "Enlaces oficiales", ""),
        (GUIDE, "Guía completa de requisitos", ""),
    ]
    items = [
        nav_link("index.html", "Inicio", active, "inicio"),
        dropdown("servicios.html", "Áreas de práctica", "servicios", active, services, "submenu-servicios"),
        nav_link("vias.html", "Vías de naturalización", active, "vias"),
        nav_link("honorarios.html", "Honorarios", active, "honorarios"),
        nav_link("aviso-legal.html", "Aviso legal", active, "aviso"),
        dropdown("informacion-legal.html", "Información legal", "informacion", active, information, "submenu-informacion"),
        nav_link("verificacion.html", "Verificación", active, "verificacion"),
        nav_link("contacto.html", "Contáctenos", active, "contacto"),
    ]
    return "\n".join(items)


def header(active):
    return f'''<a class="skip-link" href="#contenido">Saltar al contenido</a>
    <header class="site-masthead">
      <div class="shell masthead-inner">
        <div class="utility-row"><span class="utility-locale"><span class="locale-mark" aria-hidden="true">PA</span> Panamá · Español</span><a href="{WHATSAPP}" target="_blank" rel="noopener noreferrer">WhatsApp +507 6255-7583 <span aria-hidden="true">↗</span></a></div>
        <div class="brand-block"><a class="brand-link" href="index.html" aria-label="Naturalízate.pa, página de inicio"><img src="assets/logo-principal-navy.svg" alt="Naturalízate.pa" width="1054" height="140" /></a><p>Oficina legal · Naturalización panameña</p></div>
      </div>
    </header>
    <nav class="site-nav" aria-label="Navegación principal">
      <div class="shell nav-inner">
        <a class="nav-mobile-brand" href="index.html" aria-label="Naturalízate.pa, inicio"><img src="assets/isotipo-n-blanco.svg" alt="" width="105" height="92" /></a>
        <button class="menu-toggle" type="button" aria-label="Abrir menú" aria-expanded="false" aria-controls="nav-links"><span></span><span></span><span></span></button>
        <div class="nav-links" id="nav-links">{navigation(active)}</div>
      </div>
    </nav>'''


SEARCH = '''<div class="search-region">
      <form class="site-search" role="search" id="site-search" autocomplete="off">
        <label for="search-input">Buscar</label>
        <div class="search-field"><input id="search-input" type="search" placeholder="Buscar en el sitio" aria-controls="search-results" /><svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.7" aria-hidden="true"><circle cx="10.8" cy="10.8" r="6.8" /><path d="m16 16 5.1 5.1" stroke-linecap="round" /></svg></div>
      </form>
      <div class="search-results" id="search-results" aria-live="polite" hidden></div>
    </div>'''


HERO = '''<figure class="hero-banner">
      <img src="assets/panama-office.jpg" alt="Imagen ilustrativa de una oficina jurídica con vista a la Ciudad de Panamá" width="1728" height="576" fetchpriority="high" />
      <figcaption>Imagen ilustrativa</figcaption>
    </figure>'''


def footer():
    return f'''<footer class="site-footer shell" id="contacto-pie">
      <div class="footer-columns">
        <section class="footer-form-col" aria-labelledby="footer-form-title">
          <h2 id="footer-form-title">Escríbanos</h2>
          <form class="contact-form footer-form" data-wa-form>
            <label class="visually-hidden" for="footer-name">Nombre</label><input id="footer-name" name="nombre" type="text" placeholder="Nombre" autocomplete="name" required />
            <label class="visually-hidden" for="footer-email">Correo electrónico</label><input id="footer-email" name="correo" type="email" placeholder="Correo electrónico" autocomplete="email" required />
            <label class="visually-hidden" for="footer-message">Mensaje</label><textarea id="footer-message" name="mensaje" placeholder="Mensaje" rows="4" required></textarea>
            <label class="check-line"><input type="checkbox" name="novedades" value="Sí" /> Me interesa recibir novedades legales</label>
            <button class="form-submit" type="submit">Enviar <span aria-hidden="true">→</span></button>
            <p class="form-note" data-form-status role="status">Al enviar, se abrirá WhatsApp con sus datos para que revise y confirme el mensaje. No guardamos datos en esta página.</p>
          </form>
        </section>
        <section class="footer-contact-col" aria-labelledby="footer-contact-title">
          <h2 id="footer-contact-title">Contáctenos</h2>
          <div class="contact-row"><span class="contact-symbol" aria-hidden="true">⌖</span><div><strong>Dirección</strong><address>Scotia Plaza, Piso 7<br />Av. Federico Boyd<br />Ciudad de Panamá, Panamá</address></div></div>
          <div class="contact-row"><span class="contact-symbol" aria-hidden="true">◔</span><div><strong>WhatsApp</strong><a href="{WHATSAPP}" target="_blank" rel="noopener noreferrer">+507 6255-7583</a></div></div>
          <div class="contact-row"><span class="contact-symbol" aria-hidden="true">✉</span><div><strong>Correo electrónico</strong><a href="mailto:villarreallawyers@proton.me">villarreallawyers@proton.me</a></div></div>
          <div class="contact-row"><span class="contact-symbol" aria-hidden="true">↗</span><div><strong>Más información</strong><a href="{GUIDE}">Guía de requisitos</a><a href="contacto.html">Formulario de contacto</a></div></div>
        </section>
        <section class="footer-map-col" aria-labelledby="footer-map-title">
          <h2 id="footer-map-title">Ubicación</h2>
          <div class="map-preview"><span class="map-schematic-label">Esquema ilustrativo</span><div class="map-streets" aria-hidden="true"><span class="map-road map-road-one"></span><span class="map-road map-road-two"></span><span class="map-road map-road-three"></span><span class="map-road map-road-four"></span><span class="map-marker"></span></div><div class="map-preview-caption"><strong>Scotia Plaza · Piso 7</strong><span>Ciudad de Panamá</span></div></div>
          <a class="map-open" href="{MAP}" target="_blank" rel="noopener noreferrer">Ver ubicación en Google Maps <span aria-hidden="true">↗</span></a>
        </section>
      </div>
      <div class="footer-bottom"><img src="assets/logo-principal-navy.svg" alt="Naturalízate.pa" width="1054" height="140" loading="lazy" /><div><p>© <span id="year">2026</span> Naturalízate.pa · Lic. Alfonso Villarreal</p><small>Despacho privado. No afiliado al Estado panameño. La información es general y no garantiza un resultado.</small></div></div>
      <a class="floating-contact" href="{WHATSAPP}" target="_blank" rel="noopener noreferrer" aria-label="Escribir por WhatsApp a Naturalízate.pa"><svg viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="1.65" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20.4 11.7a8.3 8.3 0 0 1-12.1 7.4l-4.8 1.1 1.2-4.6A8.3 8.3 0 1 1 20.4 11.7Z"/><path d="M8.5 8.3c.4-.3.8-.2 1 .3l.8 1.8c.1.3.1.5-.1.8l-.6.8c.8 1.4 1.9 2.4 3.3 3.1l.7-.7c.3-.2.5-.3.8-.2l1.8.7c.5.2.6.6.3 1-.5.8-1.2 1.2-2.1 1.2-3.3-.1-7-3.5-7.1-6.9 0-.8.4-1.5 1.2-1.9Z"/></svg></a>
    </footer>'''


def structured_data():
    faq = {
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": question,
                "acceptedAnswer": {"@type": "Answer", "text": answer.replace("<strong>", "").replace("</strong>", "")},
            }
            for question, answer in FAQ
        ],
    }
    attorney = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Attorney",
                "@id": SITE + "#despacho",
                "name": "Naturalízate.pa",
                "url": SITE,
                "image": SITE + "og-image.png",
                "description": "Oficina legal en Ciudad de Panamá enfocada en la naturalización panameña por residencia, vínculo familiar y reciprocidad.",
                "telephone": "+507 6255-7583",
                "email": "villarreallawyers@proton.me",
                "areaServed": "PA",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "Scotia Plaza, Piso 7, Avenida Federico Boyd",
                    "addressLocality": "Ciudad de Panamá",
                    "addressCountry": "PA",
                },
                "founder": {"@type": "Person", "name": "Alfonso Villarreal", "jobTitle": "Abogado"},
                "makesOffer": {
                    "@type": "Offer",
                    "name": "Auditoría Jurídica de Caso",
                    "price": "49",
                    "priceCurrency": "USD",
                    "description": "Llamada telefónica con el Lic. Alfonso Villarreal, análisis de antecedentes, revisión de documentación y alternativas jurídicas.",
                },
            },
            faq,
        ],
    }
    return (
        '<script type="application/ld+json">'
        + __import__("json").dumps(attorney, ensure_ascii=False, separators=(",", ":"))
        + "</script>"
    )


def build_page(filename, page):
    title = escape(page["title"], quote=True)
    description = escape(page["description"], quote=True)
    home = page.get("home", False)
    robots = page.get("robots", "noindex, follow")
    canonical = page.get("canonical", SITE if home else SITE + filename)
    canonical_tag = f'<link rel="canonical" href="{canonical}" />' if canonical else ""
    og_url = f'<meta property="og:url" content="{canonical or SITE}" />'
    main = f'''<main class="shell main-shell{' is-home' if home else ' is-inner'}" id="contenido">
    {HERO if home else ''}
    {SEARCH}
    {page['body']}
    </main>'''
    return f'''<!doctype html>
<html lang="es-PA">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#0D1B2A" />
    <meta name="robots" content="{robots}" />
    <meta name="description" content="{description}" />
    {canonical_tag}
    <meta property="og:type" content="website" />
    <meta property="og:locale" content="es_PA" />
    <meta property="og:site_name" content="Naturalízate.pa" />
    {og_url}
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{description}" />
    <meta property="og:image" content="{SITE}og-image.png" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{title}" />
    <meta name="twitter:description" content="{description}" />
    <link rel="icon" type="image/png" sizes="32x32" href="assets/favicon-32x32.png" />
    <link rel="apple-touch-icon" href="apple-touch-icon.png" />
    <link rel="manifest" href="site.webmanifest" />
    <link rel="preload" href="assets/fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin />
    <link rel="preload" href="assets/fonts/playfair-display-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin />
    <link rel="stylesheet" href="styles.css" />
    {page.get('page_css', '')}
    <script src="app.js" defer></script>
    {structured_data() if home else page.get('jsonld', '')}
    <title>{title}</title>
  </head>
  <body data-page="{page['active']}">
    {header(page['active'])}
    {main}
    {footer()}
    {page.get('scripts', '')}
  </body>
</html>
'''


def main():
    for filename, page in PAGES.items():
        target = ROOT / filename
        target.write_text(build_page(filename, page), encoding="utf-8")
        print(f"Generated {target.name}: {target.stat().st_size} bytes")


if __name__ == "__main__":
    main()
