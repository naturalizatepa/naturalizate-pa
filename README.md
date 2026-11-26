# naturalizate-pa

Sitio estático del despacho **Naturalízate.pa**: landing de naturalización panameña,
guía de requisitos y siete páginas de apoyo. Se publica en
<https://naturalizatepa.github.io/naturalizate-pa/> sin build ni dependencias.

- **Portada:** `index.html` — diseño editorial (masthead, menú con submenús, imagen panorámica, buscador, columna 75/25 y pie de tres columnas) con el contenido comercial del embudo: Orientación Inicial Gratuita frente a Auditoría Jurídica de Caso (**US$49**), marco constitucional, riesgos, 5 pasos de trabajo, perfil del abogado, 12 preguntas frecuentes, servicios posteriores y formulario de calificación de 8 preguntas que prepara un mensaje de WhatsApp. Las tipografías (`Playfair Display` e `Inter`) se sirven desde `assets/fonts`.
- **Contenido:** `guia.html` es la única página indexable además de la portada.
- **Apoyo:** `contacto`, `servicios`, `vias`, `honorarios`, `informacion-legal`,
  `verificacion` y `aviso-legal` (todas `noindex, follow`), más `404.html`.
- **Oferta comercial:** Orientación Inicial Gratuita (clasificación preliminar, sin dictamen) y **Auditoría Jurídica de Caso por US$49** (llamada telefónica con el Lic. Alfonso Villarreal). Los servicios jurídicos posteriores se cotizan mediante propuesta de honorarios independiente por escrito.

## Publicar

Subir la carpeta a GitHub Pages (*Deploy from a branch*) o arrastrarla a Netlify /
Cloudflare Pages. No hay paso de compilación.

Las ocho páginas se generan con `site_builder.py` y `pages_content.py`
(encabezado, navegación, buscador y pie compartidos). Edite esos dos archivos y ejecute
`python3 -B site_builder.py`; no edite los HTML a mano porque se sobrescriben.
`guia.html`, `brandbook.html`, `formulario-interno.html` y `404.html` quedan fuera del
generador.

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

Los precios y el número de WhatsApp se repiten en `pages_content.py` y en
`site_builder.py`; cambie ambos y regenere. `LEEME-landing.md` §3 y §7 describen las
reglas editoriales y los puntos que deben moverse juntos.
