# Naturalízate.pa — Paquete listo para publicar

## Contenido
| Archivo | Descripción |
|---|---|
| `index.html` | Landing principal (versión estricta Brand Book: navy/blanco/grises) |
| `variante-dorada.html` | Variante con acento dorado para comparar (opcional: elimínela si no la usa) |
| `404.html` | Página de error |
| `robots.txt` / `sitemap.xml` | SEO técnico (ya apuntan a `https://naturalizate.pa/`) |
| `site.webmanifest` + `icon-*.png` + `maskable-*.png` | Iconos PWA / móvil |
| `favicon-*.png` + `apple-touch-icon-180.png` | Favicons del navegador |
| `foto-alfonso-villarreal.jpg` | Fotografía oficial (barras laterales recortadas) |
| `og-image.png` | Imagen al compartir en WhatsApp y redes (1200×630) |

## Cómo publicar
1. **cPanel / hosting tradicional:** suba todo el contenido a `public_html/` (o a la carpeta de su dominio) conservando los nombres.
2. **Netlify / Vercel / Cloudflare Pages:** arrastre la carpeta en el panel, o conecte su repositorio.
3. **GitHub Pages:** suba el contenido a la rama `main` (o `docs/`) y active Pages.

## Pendientes (2 minutos, en `index.html`)
1. `ENLACE_PAGO` — enlace de pago del Diagnóstico $49 (buscar `TODO` en el código).
2. Píxel de Meta / Google / GA4 — pegarlo en el `<head>` si pauta tráfico.
3. Verificar WhatsApp `50762557583` y correo `contacto@naturalizate.pa`.

## Verificación
- Rich results: https://search.google.com/test/rich-results
- Vista previa al compartir: https://developers.facebook.com/tools/debug/
