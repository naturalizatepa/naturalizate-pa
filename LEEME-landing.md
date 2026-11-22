# Landing «Nacionalidad panameña por naturalización» — Naturalízate.pa

Página de aterrizaje del despacho: una sola página que explica el servicio, publica
los honorarios y convierte en una reserva de evaluación.

**Archivo principal:** `index.html` · **Última revisión:** 22 de noviembre de 2026

- **263.451 bytes**, un solo archivo, sin paso de compilación.
- **Cero peticiones externas**: las tres tipografías van embebidas en base64 y no hay
  CDN, ni Google Fonts, ni JavaScript de terceros. Verificado con el resolutor DNS
  bloqueado: 0 recursos solicitados.
- **No es un archivo suelto**: la fotografía del abogado y los iconos son archivos
  locales de la misma carpeta. Para verla completa hay que conservar `index.html`,
  `foto-alfonso-villarreal.jpg` y los favicons.

---

## 1. Estructura real (11 bloques)

Diez secciones con `id` más el cierre comercial. Todos los enlaces del menú apuntan a
estas anclas, y las nueve llamadas a la acción llevan a `#verificar`.

| # | Ancla | Contenido | Función en el embudo |
|---|---|---|---|
| 1 | `#inicio` | Hero: «Sepa si su caso de naturalización se sostiene antes de invertir» + tarjeta del abogado con la evaluación de $49.99 | Promesa y ruta |
| 2 | `#situacion` | «Vivir en Panamá durante años no significa conocer todos los pasos» + cita destacada | Reconocimiento del problema |
| 3 | `#enfoque` | «Su proceso necesita algo más que presentar documentos» + **5 pilares** (evaluación, transparencia, acompañamiento, atención personalizada, presencia profesional) | Diferenciación |
| 4 | `#proceso` | **5 etapas**: evaluación, análisis jurídico, expediente, presentación y seguimiento, acompañamiento | Confianza procesal |
| 5 | `#honorarios` | Plan Esencial **USD 3,800** y Plan Todo Incluido **USD 5,500** + **tabla comparativa de 9 filas** + notas de moneda e ITBMS | Precio ancla |
| 6 | `#diagnostico` | Única sección de oferta: «Antes de invertir, sepa qué tan sólido es su caso», qué incluye el informe, tarjeta de **$49.99** y 3 pasos del servicio | Oferta núcleo |
| 7 | `#abogado` | Lic. Alfonso Villarreal, foto, sede y criterio de admisión de casos | Autoridad |
| 8 | `#casos` | **3 testimonios** con identidad protegida y nota de confidencialidad | Prueba social |
| 9 | `#preguntas` | **11 preguntas frecuentes** en acordeón accesible | Objeciones |
| 10 | `#verificar` | **Formulario de 4 pasos** (ver §2) | Conversión |
| 11 | `section.final-cta` | Cierre: «No comience su proceso sin conocer primero su situación jurídica» + WhatsApp | Cierre |

Después del cierre: pie con navegación, contacto y sede, aviso legal y barra fija de
llamada a la acción en móvil.

**No hay** sección de «marco legal», ni autoevaluación de criterios, ni bloque de
«compromiso», ni modal de entrada. Si algún documento anterior los menciona, está
desactualizado.

**Procedencia visual:** la composición se adaptó de la referencia kerycruz.com
(revisión del 19 nov 2026), conservando su arquitectura de lectura, sin copiar
logotipo, textos, precios ni identidad. El análisis comparativo original está
archivado fuera del proyecto desde el 22 nov 2026.

---

## 2. El formulario, paso por paso

Cuatro pantallas con barra de progreso (`role="progressbar"`, 25 % por paso) y
etiqueta «Paso N de 4». El estado vive en memoria: **no guarda borrador** y recargar
pierde las respuestas.

### Paso 1 · Su situación (5 preguntas)

| Pregunta | Opciones | Para qué sirve |
|---|---|---|
| País de origen | Lista de **40 países** + «Otro» (abre un campo de texto) | Detecta convenio de reciprocidad |
| Años con Cédula E | Menos de 3 · entre 3 y 5 · más de 5 · no estoy seguro(a) | Cómputo legal |
| Ausencias prolongadas | No · menores a 6 meses · mayores a 6 meses · no estoy seguro(a) | Arraigo |
| Disposición al examen | Sí, con disciplina · tengo dudas · no | Requisito legal |
| Ingreso mensual | Menos de $1,000 · 1,000–3,000 · 3,000–5,000 · 5,000–10,000 · más de $10,000 | Solvencia (filtro blando) |

Son **16 chips y una lista**, con un campo de texto condicional para «Otro». Ningún
campo es obligatorio por atributo HTML: la validación es propia y muestra un error con
`role="alert"`.

### Paso 2 · Resultado

El veredicto se calcula en el navegador y se anuncia con `aria-live="polite"`. Tiene
tres estilos visuales y **siempre** ofrece dos salidas: reservar o corregir respuestas.
Ninguna ruta cierra la puerta.

| Caso | Mensaje | ¿Puede reservar? |
|---|---|---|
| Menos de 3 años **con** reciprocidad | «Su nacionalidad puede aplicar con menos años» | Sí |
| Menos de 3 años **sin** reciprocidad | «Su caso aún no cumple el cómputo legal» | Sí (evaluación; no se propone iniciar) |
| Examen: «No» | «El examen es obligatorio» | Sí (evaluación) |
| Perfil con puntaje ≥ 7 | «Perfil prioritario · A» | Sí |
| Perfil con puntaje 4–6 | «Revisión recomendada · B» | Sí |
| Perfil con puntaje ≤ 3 | «Revisión recomendada · C» | Sí |

**Puntaje** (máximo 8): Cédula E de más de 5 años +2; sin ausencias +2 (menores o «no
estoy seguro» +1); dispuesto al examen +2 (con dudas +1); ingreso desde $3,000 +2.
Los ingresos bajos no restan: agregan una advertencia de solvencia.

**Reciprocidad aplicada**: El Salvador 1 año; Argentina, Colombia, Ecuador, España,
Honduras, México, Nicaragua y Perú 2 años; Uruguay 3 años. La vigencia de cada
convenio debe confirmarse al presentar.

### Paso 3 · Reserva (2 campos)

Solo **nombre completo** y **WhatsApp**. Una nota explica que el día, la hora y el
plan se coordinan por WhatsApp y que no hace falta preparar documentos todavía. Hay un
campo trampa oculto contra spam.

### Paso 4 · Confirmación

Resumen de **8 filas** (nombre, WhatsApp, país, Cédula E, ausencias, examen, ingreso y
resultado), casilla de consentimiento para el tratamiento de datos y botón
«Confirmar por WhatsApp». Al confirmar se abre `wa.me/50762557583` con el mensaje
completo, incluido el perfil interno y el origen UTM si existe. Si el navegador bloquea
la ventana, el mismo enlace queda como botón de respaldo.

---

## 3. Marca y sistema visual

| Elemento | Aplicación |
|---|---|
| Navy `#0D1B2A` y neutros | Fondo del hero y del cierre, botones primarios, títulos |
| Playfair Display (400–900, normal e itálica) | Titulares y cifras |
| Inter (100–900) | Texto, etiquetas, botones |
| Tarjetas de 12 px de radio, botones de 4 px | Sistema sobrio, sin acentos cromáticos |
| Tabla comparativa | 9 filas, encabezado navy, marcas de inclusión |

Regla editorial respetada: **ninguna promesa de resultados**. El texto habla de
viabilidad, alcance y riesgos, y el aviso legal recuerda que la decisión corresponde al
Estado panameño.

---

## 4. Técnica

- **Peso y palabras**: 263.451 bytes; unas 2.484 palabras visibles.
- **Sin red**: 3 `@font-face` en base64, iconos locales, WhatsApp solo al confirmar.
- **Responsive**: probado a **360 px** y **1440 px** sin desborde horizontal. Menú
  hamburguesa desde 900 px, tabla comparativa con desplazamiento interno desde 640 px
  (con la indicación «Deslice la tabla…») y barra fija de CTA que se oculta cuando el
  formulario está a la vista.
- **Anclas**: `scroll-margin-top: 92px`; las secciones aterrizan a 92 px en ambos anchos.
- **Accesibilidad**: `<main>`, `role="alert"` en los tres errores, `aria-live` en
  veredicto y resumen, `progressbar` con `aria-valuenow`, foco visible blanco de 2 px
  sobre fondos navy, `aria-expanded` en menú y acordeón,
  `prefers-reduced-motion` respetado. **No hay enlace «saltar al contenido».**
- **Sin `content-visibility`**: se retiró porque excluía secciones del árbol de
  accesibilidad y de `innerText` hasta acercarse al viewport.
- **SEO**: `title` (61 caracteres, 578 px) y `description` (151), canónica autorreferente
  en las nueve páginas (portada, guía y las siete de apoyo),
  Open Graph + Twitter Card con imagen 1200×630, datos estructurados `Attorney` y
  `FAQPage` con **las mismas 11 preguntas** del HTML. `robots.txt` y `sitemap.xml` con
  dos URLs: la portada y `guia.html`. Ambas entran completas en Google (portada
  61/151; guía 60/136). Ver `SEO.md` §3.
- **Analítica**: `track()` acumula en `window.dataLayer` (compatible con GTM). El
  puente a GA4 está listo pero **inactivo**: `GA4_ID` está vacío, así que no se carga
  `gtag.js` ni se hace ninguna petición. Al pegar el ID, `filtro_resultado` y
  `reserva_confirmada` se envían a GA4. La cláusula de cookies ya está en
  `aviso-legal.html#cookies`; falta pegar el ID para activar la medición.

---

## 5. Archivos

```
naturalizate-pa-main/
├── index.html                 ← la portada (tipografías embebidas)
├── 404.html                   ← error; GitHub Pages la sirve sola
├── guia.html                  ← única página enlazada desde la portada
├── contacto.html · servicios.html · vias.html · honorarios.html
├── informacion-legal.html · verificacion.html · aviso-legal.html
├── formulario-interno.html    ← herramienta del despacho (noindex, nofollow)
├── styles.css · app.js        ← sistema de las páginas interiores (NO lo usa index.html)
├── assets/fonts/              ← woff2 de origen de las tipografías embebidas
├── fonts/ · svg/              ← fuentes y logotipos sueltos
├── foto-alfonso-villarreal.jpg (36 KB) · og-image.png (128 KB)
├── favicons, iconos PWA y site.webmanifest
├── robots.txt · sitemap.xml · .nojekyll · _headers
└── LEEME-landing.md · ANALISIS-EMBUDO.md · SEO.md · README.md
```

`styles.css` y `app.js` **no son archivos muertos**: los cargan las siete páginas
interiores. `_headers` añade cabeceras de seguridad para Netlify o Cloudflare Pages y
`noindex` para el formulario interno.

---

## 6. Publicar

Se edita `index.html` y se sube: la portada no se compila.

> **Nota:** los generadores antiguos `site_builder.py` y `pages_content.py` se
> eliminaron el 22 nov 2026. Reescribían `index.html` con la portada anterior
> («Bienvenidos a la oficina legal»); no los restaure.

1. **GitHub Pages estático**: sube el contenido de la carpeta a `main` (o `docs/`) y
   elige *Deploy from a branch*. El `.nojekyll` ya está incluido y evita que Jekyll
   procese el sitio.
2. **Netlify / Cloudflare Pages**: arrastra la carpeta. `_headers` se aplica solo.
3. **Dominio propio**: cambia la URL en `<link rel="canonical">`, `og:url`, `og:image`,
   `sitemap.xml` y la línea `Sitemap:` de `robots.txt`. Todo es relativo, así que
   también funciona en un subdirectorio.
4. **Comprobar**: resultados enriquecidos en
   <https://search.google.com/test/rich-results> y la imagen al compartir en
   <https://developers.facebook.com/tools/debug/>.

---

## 7. Dónde tocar cada cosa

- **WhatsApp y nombre de la asistente**: `WHATSAPP_NUMBER` y `ASISTENTE` al inicio del
  `<script>` final. El número también aparece en el enlace del cierre y en el pie.
- **Precios**: están en cuatro lugares que deben moverse juntos — tarjetas de plan,
  fila «Honorarios fijos» de la tabla, sección de evaluación y FAQ.
- **FAQ**: si agregas o quitas una pregunta, actualiza el HTML **y** el bloque
  `FAQPage` del `<head>`; hoy coinciden en 11.
- **Menú**: los enlaces deben apuntar a los `id` de la tabla del §1.
- **Analítica**: `GA4_ID`, al inicio del `<script>` final. Vacío = sin peticiones ni
  cookies. Con un ID `G-XXXXXXXXXX` se carga GA4 y los eventos se envían solos.
- **Después de un cambio estructural**, actualiza este archivo y `ANALISIS-EMBUDO.md`.

---

## 8. Pendientes que no dependen del código

- [ ] Confirmar que `villarreallawyers@proton.me` está activo. El dominio
      `naturalizate.pa` no es del despacho: el sitio vive en GitHub Pages.
- [ ] Revisar con el abogado las respuestas del FAQ y el plazo «19 a 22 meses».
- [ ] Confirmar si el servicio está gravado con ITBMS: la página lo deja condicional.
- [ ] Decidir si se activa GA4: la cláusula de cookies ya está en el aviso legal;
      falta pegar el ID en `GA4_ID` y registrar `resultado`, `perfil` y `pais` como
      dimensiones personalizadas. Sin ID, la página sigue sin peticiones externas.
- [ ] Valorar un enlace «saltar al contenido» si se exige WCAG 2.2 AA.
- [x] Siete interiores en `noindex` por decisión del 22 nov 2026 (`SEO.md` §2);
      canónica lista por si se amplían.
