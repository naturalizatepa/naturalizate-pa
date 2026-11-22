# naturalizate-pa

Sitio estático del despacho **Naturalízate.pa**: landing de naturalización panameña,
guía de requisitos y siete páginas de apoyo. Se publica en
<https://naturalizatepa.github.io/naturalizate-pa/> sin build ni dependencias.

- **Portada:** `index.html` — una sola página con la oferta, la tabla de planes, el
  formulario de 4 pasos y las 11 preguntas frecuentes. Las tipografías van embebidas en
  base64, así que abre sin conexión.
- **Contenido:** `guia.html` es la única página indexable además de la portada.
- **Apoyo:** `contacto`, `servicios`, `vias`, `honorarios`, `informacion-legal`,
  `verificacion` y `aviso-legal` (todas `noindex, follow`), más `404.html`.
- **Oferta publicada:** evaluación **$49.99** deducible; honorarios **USD 3,800**
  (Esencial) y **USD 5,500** (Todo Incluido), con ITBMS condicional.

## Publicar

Subir la carpeta a GitHub Pages (*Deploy from a branch*) o arrastrarla a Netlify /
Cloudflare Pages. No hay paso de compilación.

La portada se edita a mano. El generador antiguo (`site_builder.py` y
`pages_content.py`) se eliminó el 22 nov 2026 porque reescribía `index.html`; no lo
restaure.

## Dónde está cada cosa

| Necesidad | Archivo |
|---|---|
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
