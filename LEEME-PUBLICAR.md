# Naturalízate.pa — Paquete listo para publicar

**Estado:** 19 de noviembre de 2026 · **una sola página** (`index.html`), sin ventanas de entrada ni
captura de leads.

## Política comercial vigente (aplicada en todo el sitio)

| Concepto | Condición |
|---|---|
| **Auditoría inicial del caso** | **$49.99**, pago único, se paga **antes** de la cita |
| **Deducible** | Se deduce **en su totalidad** de los honorarios si el cliente contrata |
| **Atención** | Únicamente bajo **cita previa pagada** |
| **Comprobante** | Al WhatsApp **6255-7583** con **nombre** y **número de documento** |
| **Honorarios** | Fijos por escrito: **Esencial $3,800** · **Integral $5,500**, con pago fraccionado |

- El sitio **no promete nada gratis**: no queda ninguna mención de gratuidad, «sin costo» ni
  «sin compromiso» (verificado el 19 nov 2026 en los cinco HTML del paquete).
- **No hay pasarela de pago conectada.** El formulario envía la solicitud por WhatsApp y Patricia
  indica el medio de pago. No invente enlaces de pago en el texto.

## Contenido

| Archivo | Descripción |
|---|---|
| `index.html` | Landing principal: todo el CSS y el JS van dentro (11 secciones + formulario de 4 pasos) |
| `guia.html` | Guía de requisitos con la misma estructura y copy que la landing (incluye planes y evaluación de $49.99) |
| `formulario-interno.html` | Herramienta del despacho (26 campos + informe PDF). **`noindex`**, no enlazada desde el sitio |
| `variante-dorada.html` | Variante con acento dorado del mismo contenido (opcional: elimínela si no la usa) |
| `404.html` | Página de error |
| `robots.txt` / `sitemap.xml` | SEO técnico (host: `https://naturalizatepa.github.io/naturalizate-pa/`) |
| `site.webmanifest`, `icon-*.png`, `maskable-*.png` | Iconos PWA / móvil |
| `favicon.ico`, `favicon-*.png`, `apple-touch-icon*.png` | Favicons |
| `foto-alfonso-villarreal.jpg` | Fotografía del licenciado (héroe y datos estructurados) |
| `og-image.png` | Imagen al compartir (1200×630) |
| `_headers` | Cabeceras de seguridad y caché (solo Netlify / Cloudflare Pages) |
| `README-PUBLICAR.md` | Guía detallada (flujo, campos, verificación) |

## Cómo publicar

1. **cPanel / hosting tradicional:** suba todo a `public_html/` conservando nombres y reemplace el
   `index.html` anterior.
2. **Netlify / Vercel / Cloudflare Pages:** arrastre la carpeta o conecte el repositorio.
3. **GitHub Pages:** suba a `main` (o `docs/`) y active Pages.

## Pendientes antes de publicar

1. **Medio de pago.** Confirmar cómo se cobra el $49.99 (Yappy, transferencia, tarjeta) y si se
   automatiza con un enlace. Hoy el sitio dice que se coordina por WhatsApp.
2. **Validación legal.** El Lic. Villarreal debe aprobar los textos de honorarios, deducible y
   requisitos (los de solvencia salen de la guía del SNM; los rangos de ingreso son criterio del
   despacho).
3. **Píxeles** (Meta / Google / GA4) en el `<head>` si se pauta tráfico; si usa `_headers`, agregue
   el dominio del píxel a `script-src` y `connect-src`.
4. **Fotografía** definitiva en `foto-alfonso-villarreal.jpg`.
5. Verificar WhatsApp `50762557583` y correo `Villarreallawyers@proton.me`.

## Verificación

- `grep` sin coincidencias de «gratis», «gratuita», «sin costo» y «sin compromiso» en los cinco HTML.
- Script inline de `index.html` validado (`new Function`, sin errores de sintaxis).
- Flujo del formulario probado en Chrome sin interfaz: bloquea sin número de documento, avanza al
  completarlo y lo incluye en el resumen y en el mensaje de WhatsApp.

Pendiente de validación humana: revisión visual en navegador real y aprobación del abogado.
