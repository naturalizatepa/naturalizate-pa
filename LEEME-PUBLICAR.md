# Naturalízate.pa — Paquete listo para publicar (v4)

Novedades v4 (embudo de venta): pago dual Yappy + tarjeta (cada botón sin
enlace se oculta solo); factura de valor + garantía en el paso 4; pregunta de
antecedentes movida a la evaluación privada; etiqueta comercial interna
eliminada del mensaje de WhatsApp; captura progresiva opcional de leads
(FormSubmit); lead magnet para perfiles educativos; 5 FAQs de pago + schema;
credencial 98% reemplazada por 5+ años de cédula E (Brand Book v3.0).
Novedades v3: la precalificación aparece centrada al cargar, con el fondo
desenfocado hasta completar los datos; FAQPage para Google; render diferido
de secciones; formulario sin zoom en iOS.
Filtro por reciprocidad: 10 nacionalidades (El Salvador 1 año; Argentina,
Colombia, Ecuador, España, Honduras, México, Nicaragua, Perú 2 años; Uruguay
3 años) no se rechazan por <3 años: pasan a WhatsApp como «verificar cómputo
por reciprocidad». Validar la vigencia de los convenios con el abogado.

## Contenido
| Archivo | Descripción |
|---|---|
| `index.html` | Landing principal (estricta Brand Book: navy/blanco/grises) |
| `guia.html` | Guía de contratación y preguntas frecuentes (mismo formulario y filtro) |
| `variante-dorada.html` | Variante con acento dorado (opcional: elimínela si no la usa) |
| `404.html` | Página de error |
| `robots.txt` / `sitemap.xml` | SEO técnico (ya apuntan a `https://naturalizate.pa/`) |
| `site.webmanifest` + `icon-*.png` + `maskable-*.png` | Iconos PWA / móvil |
| `favicon-*.png` + `apple-touch-icon-180.png` | Favicons del navegador |
| `foto-alfonso-villarreal.jpg` | Fotografía oficial (barras laterales recortadas) |
| `og-image.png` | Imagen al compartir en WhatsApp y redes (1200×630) |

## Puerta de entrada (cómo funciona)
- Al cargar, el formulario de precalificación se muestra centrado con el fondo
  desenfocado y la página bloqueada (sin desplazamiento).
- Al completar los datos (cualquier veredicto), el botón principal abre
  WhatsApp con su resultado y revela el contenido; el formulario regresa a su
  sección con el resultado visible. Cada mensaje llega etiquetado
  (Perfil A/B/C, consulta general, pendiente examen o "Aún no procede" con solicitud de diagnóstico).
- Se recuerda por sesión (`sessionStorage nzq_gate_done`): recargar no la
  muestra de nuevo; nueva visita sí. Sin JavaScript, la puerta no aparece y el
  formulario queda en su sección (compatible con Google).
- **Desactivarla:** elimine el bloque `#entryGate`, el micro-script
  `nzq_gate_done` del `<head>` y el bloque JS «Puerta de entrada».

## Cómo publicar
1. **cPanel / hosting tradicional:** suba todo a `public_html/` conservando nombres.
2. **Netlify / Vercel / Cloudflare Pages:** arrastre la carpeta o conecte su repo.
3. **GitHub Pages:** suba a `main` (o `docs/`) y active Pages.

## Pendientes (2 minutos, en `index.html`)
1. `ENLACE_PAGO` — enlace de pago del Diagnóstico $49 (buscar `TODO`).
2. Píxel de Meta / Google / GA4 — pegarlo en el `<head>` si pauta tráfico.
3. Verificar WhatsApp `50762557583` y correo `Villarreallawyers@proton.me`.

## Verificación
- Rich results: https://search.google.com/test/rich-results
- Vista previa al compartir: https://developers.facebook.com/tools/debug/
