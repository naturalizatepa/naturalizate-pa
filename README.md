# naturalizate-pa

Sitio estático del despacho **Naturalízate.pa**: landing de naturalización panameña,
guía de requisitos y siete páginas de apoyo. Se publica en
<https://naturalizatepa.github.io/naturalizate-pa/> sin build ni dependencias.

- **Portada:** `index.html` — sistema comercial de 10 secciones alineado al embudo de 6 etapas (Contacto → Calificación → Confianza → Conversión → Evaluación → Contratación), separación entre Orientación Inicial Gratuita y Auditoría Jurídica de Caso (**US$49**), formulario de calificación de 8 preguntas y 12 preguntas frecuentes. Las tipografías (`Playfair Display` e `Inter`) van embebidas en base64.
- **Contenido:** `guia.html` es la única página indexable además de la portada.
- **Apoyo:** `contacto`, `servicios`, `vias`, `honorarios`, `informacion-legal`,
  `verificacion` y `aviso-legal` (todas `noindex, follow`), más `404.html`.
- **Oferta comercial:** Orientación Inicial Gratuita (clasificación preliminar, sin dictamen) y **Auditoría Jurídica de Caso por US$49** (llamada telefónica con el Lic. Alfonso Villarreal). Los servicios jurídicos posteriores se cotizan mediante propuesta de honorarios independiente por escrito.

## Publicar

Subir la carpeta a GitHub Pages (*Deploy from a branch*) o arrastrarla a Netlify /
Cloudflare Pages. No hay paso de compilación.

La portada se edita a mano. El generador antiguo (`site_builder.py` y
`pages_content.py`) se eliminó el 22 nov 2026 porque reescribía `index.html`; no lo
restaure.

## Dónde está cada cosa

| Necesidad | Archivo |
|---|---|
| Brand Book completo, embudo comercial y guía de aplicación | `BRANDBOOK.md` · `brandbook.html` (visual/imprimible) |
| Estructura, formulario, marca y mantenimiento | `LEEME-landing.md` |
| Embudo, eventos y fricción | `ANALISIS-EMBUDO.md` |
| Canonical, sitemap, indexación y Search Console | `SEO.md` |
| Publicación paso a paso y dominio | `README-PUBLICAR.md` |

## Vista local

```bash
python3 -m http.server 8080
# http://localhost:8080/index.html
```

Los precios y el número de WhatsApp están duplicados en varios puntos de `index.html`;
`LEEME-landing.md` §7 indica todos los lugares que deben moverse juntos.
