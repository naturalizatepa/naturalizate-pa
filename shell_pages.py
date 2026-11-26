"""Recompose the hand-written pages inside the shared masthead, navigation, search and footer.

The content and the page-specific CSS live in `_fuentes/`. This script scopes that CSS to
the page content wrapper so the shared chrome keeps the new site style, and writes:

  404.html · guia.html · brandbook.html · formulario-interno.html · index (sin extensión)

Run it after editing anything in `_fuentes/` with: python3 -B shell_pages.py
"""

from pathlib import Path

from pages_content import WHATSAPP
from site_builder import ROOT, SITE, build_page

FUENTES = ROOT / "_fuentes"


def source(name: str) -> str:
    return (FUENTES / name).read_text(encoding="utf-8")


def blocks(css: str):
    """Yield (prelude, body) pairs for the top-level rules of a stylesheet."""
    css = __import__("re").sub(r"/\*.*?\*/", "", css, flags=__import__("re").S)
    i, size = 0, len(css)
    while i < size:
        opening = css.find("{", i)
        if opening == -1:
            break
        depth, cursor = 1, opening + 1
        while cursor < size and depth:
            depth += {"{": 1, "}": -1}.get(css[cursor], 0)
            cursor += 1
        yield css[i:opening].strip(), css[opening + 1 : cursor - 1]
        i = cursor


def scope_selector(selector: str, scope: str) -> str:
    selector = selector.strip()
    if not selector:
        return ""
    if selector in {"html", "body", ":root"}:
        return scope
    if selector.startswith(scope):
        return selector
    return f"{scope} {selector}"


def scope_css(css: str, scope: str) -> str:
    """Prefix every rule with the content wrapper so legacy CSS cannot restyle the shared chrome."""
    output = []
    for prelude, body in blocks(css):
        if prelude.startswith("@font-face"):
            continue
        if prelude.startswith(("@media", "@supports")):
            output.append(f"{prelude} {{\n{scope_css(body, scope)}}}")
        elif prelude.startswith(("@keyframes", "@-webkit-keyframes", "@page")):
            if prelude.startswith("@page"):
                continue
            output.append(f"{prelude} {{{body}}}")
        else:
            selectors = [scope_selector(part, scope) for part in prelude.split(",")]
            selectors = [part for part in selectors if part]
            if selectors:
                output.append(", ".join(selectors) + " {" + body + "}")
    return "\n".join(output)


def page_css(name: str, scope: str) -> str:
    return f"<style>\n{scope_css(source(name), scope)}\n</style>"


def wrapped(name: str, scope: str, stylesheet: str) -> str:
    return (
        f'<div class="legacy-page" id="{scope}">\n{source(name)}\n</div>'
    ), page_css(stylesheet, scope)


PAGES = {}


def register(filename, **page):
    PAGES[filename] = page


# --- 404 -------------------------------------------------------------------
register(
    "404.html",
    active="",
    title="Página no encontrada — Naturalízate.pa",
    description="La dirección solicitada no existe o cambió. Vuelva al inicio de Naturalízate.pa o escriba al despacho por WhatsApp.",
    robots="noindex",
    canonical=False,
    body=f'''<div class="content-columns"><article class="article-main">
      <div class="page-heading"><span class="eyebrow">Error 404</span><h1>Esta página no existe, pero su trámite sí tiene inicio.</h1><p>La dirección que abrió pudo cambiar o escribirse con error. Vuelva al inicio o escriba directamente a un asesor para recibir orientación inmediata.</p></div>
      <div class="inline-actions"><a class="button-primary" href="index.html">Ir al inicio <span aria-hidden="true">→</span></a><a class="text-action" href="{WHATSAPP}" target="_blank" rel="noopener noreferrer">Hablar con un asesor <span aria-hidden="true">↗</span></a></div>
    </article></div>''',
)

# --- Guía ------------------------------------------------------------------
body, css = wrapped("guia.html", "guia", "guia.css")
register(
    "guia.html",
    active="",
    title="Requisitos de naturalización en Panamá: marco constitucional y auditoría | Naturalízate.pa",
    description="Guía sobre naturalización panameña: artículo 10 de la Constitución, vías legales, documentos a verificar, autoridades competentes y Auditoría Jurídica de Caso por US$49.",
    robots="index, follow",
    canonical=SITE + "guia.html",
    body=body,
    page_css=css,
    jsonld=source("guia.jsonld"),
)

# --- Brand book (documento interno) ---------------------------------------
body, css = wrapped("brandbook.html", "brandbook", "brandbook.css")
register(
    "brandbook.html",
    active="",
    title="Brand Book, Embudo Comercial y Guía de Aplicación | Naturalízate.pa",
    description="Documento interno de identidad visual, sistema comercial y protocolos de marca de Naturalízate.pa.",
    robots="noindex, nofollow",
    canonical=False,
    body=body,
    page_css=css,
)

# --- Formulario interno del despacho ---------------------------------------
body, css = wrapped("formulario-interno.html", "interno", "formulario-interno.css")
register(
    "formulario-interno.html",
    active="",
    title="Formulario interno · Uso del despacho | Naturalízate.pa",
    description="Herramienta interna del despacho para registrar el perfil del solicitante y generar el informe en PDF.",
    robots="noindex, nofollow",
    canonical=False,
    body=body,
    page_css=css,
    scripts=source("formulario-interno.js"),
)

# --- Página heredada sin extensión ----------------------------------------
body, css = wrapped("legacy-index.html", "legado", "legacy-index.css")
register(
    "index",
    active="",
    title="Residencia Permanente Estudiantes | naturalizate.pa",
    description="Página heredada sobre la subcategoría de residencia permanente para estudiantes en Panamá.",
    robots="noindex, follow",
    canonical=False,
    body=body,
    page_css=css,
)


def main():
    for filename, page in PAGES.items():
        target = ROOT / filename
        target.write_text(build_page(filename, page), encoding="utf-8")
        print(f"Generated {target.name}: {target.stat().st_size} bytes")


if __name__ == "__main__":
    main()
