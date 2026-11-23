# Naturalízate.pa — Guía de publicación

**Actualizada:** 23 de noviembre de 2026 · **Sitio:** estático, sin paso de compilación.

Esta es la única guía de publicación vigente. Sustituye a `LEEME-PUBLICAR.md` (retirado por
duplicar esta guía y describir una versión comercial anterior).

---

## 1. Qué hay en la carpeta

| Archivo | Papel |
|---|---|
| `index.html` | Portada y embudo comercial completo (CSS, JS y 3 tipografías woff2 embebidas). **Indexable** |
| `guia.html` | Guía jurídica y de requisitos (Art. 10 y autoridades competentes). **Indexable**, con canónica propia |
| `aviso-legal.html` · `contacto.html` · `honorarios.html` · `informacion-legal.html` · `servicios.html` · `verificacion.html` · `vias.html` | Páginas de apoyo, `noindex, follow`, con canónica propia |
| `404.html` | Página de error. `noindex` |
| `formulario-interno.html` | Herramienta interna del despacho. `noindex, nofollow`, no enlazada desde el sitio |
| `robots.txt` · `sitemap.xml` | Dos URLs indexables: portada (`index.html`) y guía (`guia.html`) |
| `_headers` | Cabeceras de seguridad y caché para Netlify / Cloudflare Pages |
| `site.webmanifest` · `favicon-*.png` · `apple-touch-icon*.png` | Iconos e instalación como app |
| `styles.css` · `app.js` | Sistema visual y comportamiento de las siete páginas interiores (no los carga `index.html`) |
| `assets/fonts/` · `fonts/` | Tipografías autoalojadas (`Inter` y `Playfair Display`) |
| `foto-alfonso-villarreal.jpg` · `og-image.png` | Retrato del abogado y tarjeta social 1200×630 |
| `googlef7de84a63b85219f.html` | Verificación de Google Search Console. No borrar |

---

## 2. Política comercial vigente

| Concepto | Condición |
|---|---|
| **Orientación Inicial Gratuita** | Primer contacto orientativo breve (nacionalidad, estatus general, necesidad, clasificación preliminar y siguiente paso). **No incluye** opinión jurídica, revisión completa de expediente, análisis exhaustivo ni diagnóstico definitivo de elegibilidad |
| **Auditoría Jurídica de Caso** | **US$49**, precio visible en la página. Modalidad: **llamada telefónica con el Lic. Alfonso Villarreal**. Servicio profesional independiente |
| **Alcance de la auditoría** | Análisis de antecedentes del caso, revisión de documentos pertinentes aportados por el cliente, evaluación migratoria, identificación de riesgos u obstáculos, posibles vías legales, requisitos y próximos pasos |
| **Servicios posteriores** | Si el caso resulta viable, cualquier representación legal, redacción, presentación o acompañamiento se cotiza y contrata **por separado** mediante propuesta de honorarios independiente y por escrito |
| **Medio de pago** | Se coordina por WhatsApp (`+507 6255-7583`); actualmente **no hay pasarela de pago conectada** en la página |

El sitio nunca declara elegibilidad o inelegibilidad automática ni promete aprobaciones,
plazos garantizados o resultados que dependen del Estado panameño.

---

## 3. Portada y formulario de calificación

La portada (`index.html`) sigue un recorrido de 10 bloques estratégicos para el embudo
`CONTACTO → CALIFICACIÓN → CONFIANZA → CONVERSIÓN → EVALUACIÓN → CONTRATACIÓN`:
`#inicio`, `#servicios-inicio`, `#quien-puede`, `#riesgos`, `#auditoria`, `#como-trabajamos`,
`#abogado`, `#preguntas`, `#contratacion`, `#calificacion` y `#contacto`.

El formulario de calificación (`#calificacion`) recoge **8 preguntas clave**:

1. Nacionalidad.
2. Año desde que reside en Panamá.
3. Tipo de residencia actual.
4. ¿Tiene cédula E?
5. ¿Desde cuándo tiene cédula E?
6. ¿Ha salido de Panamá durante su residencia?
7. ¿Actualmente se encuentra en Panamá o en el extranjero?
8. ¿Tiene vínculo familiar con ciudadanos panameños?

Al enviarse, clasifica posibles vías preliminares a revisar (residencia, matrimonio cuando
corresponda, reciprocidad, hijos panameños cuando aplique u otras situaciones migratorias)
sin emitir veredicto automático, muestra el mensaje institucional de recepción y habilita el
botón **«ENVIAR MI INFORMACIÓN POR WHATSAPP»** con los datos estructurados y atribución UTM.

---

## 4. Cómo publicar

### GitHub Pages (host actual)

1. Suba el contenido a `main` y mantenga activo *Deploy from a branch*.
2. `.nojekyll` ya está incluido.
3. Con dominio propio, actualice la URL en `<link rel="canonical">`, `og:url`, `og:image`,
   `sitemap.xml` y la línea `Sitemap:` de `robots.txt`.

### Netlify o Cloudflare Pages

Arrastre la carpeta o conecte el repositorio. `_headers` se aplica automáticamente.

### Vercel

Despliegue el repositorio. **Vercel no lee `_headers`**: si requiere las mismas cabeceras,
declárelas en `vercel.json`.

### cPanel o hosting tradicional

1. Suba todo el contenido a `public_html/`, conservando nombres y rutas.
2. `_headers` se ignora; añada en `.htaccess` las cabeceras de seguridad (`X-Content-Type-Options`,
   `X-Frame-Options`, `Referrer-Policy`).

### Formulario interno

- Manténgalo con `noindex, nofollow` y **nunca** lo enlace desde la portada ni desde las
  páginas públicas.

---

## 5. Pendientes opcionales de configuración

- [ ] **GA4:** pegar el Measurement ID (`G-XXXXXXXXXX`) en `GA4_ID` dentro de `index.html`
      (actualmente vacío, sin peticiones externas; eventos listos en `window.dataLayer`).
- [ ] **Enlace de pago directo (opcional):** si se habilita cobro en línea para la
      Auditoría Jurídica de Caso (US$49), integrarlo junto al botón de WhatsApp.
- [ ] **Dominio propio y Search Console:** confirmar la propiedad en Search Console y enviar
      `sitemap.xml`.
- [ ] **Validación periódica del abogado:** confirmar vigencia de criterios administrativos
      del SNM, Tribunal Electoral y Órgano Ejecutivo.

---

## 6. Qué se verificó en esta versión (23 nov 2026)

- **Cero peticiones externas bloqueantes** en `index.html` (3 fuentes `.woff2` embebidas en
  base64 y `GA4_ID = ""`).
- **Sintaxis JS** de `index.html` verificada (`node --check`, sin errores).
- **JSON-LD** válido (`Attorney` y `FAQPage` con **12 preguntas** sincronizadas con el HTML).
- **HTTP 200 OK** en todas las páginas públicas y verificación de enlaces locales y anclas.
- **Telemetría del embudo** validada en simulación DOM (`visita_embudo`, `evaluacion_iniciada`,
  `evaluacion_completada`, `whatsapp_click`, `auditoria_solicitada`, `cta_click`, `faq_abierta`).
- **Limpieza comercial**: cero referencias residuales a tarifas anteriores en las páginas
  publicadas y retirada de `variante-dorada.html` y `LEEME-PUBLICAR.md`.

---

## 7. Archivos heredados que no deben usarse ni recrearse

- `variante-dorada.html` y `LEEME-PUBLICAR.md`: retirados del repositorio por corresponder a
  una versión comercial anterior. No recrear.
- `site_builder.py` y `pages_content.py`: generadores antiguos que sobrescribirían `index.html`
  con una versión obsoleta; **no ejecutar**.

---

## 8. Documentación relacionada

| Necesidad | Archivo |
|---|---|
| Estructura, identidad visual, formulario y mantenimiento | `LEEME-landing.md` |
| Embudo comercial de 6 etapas y analítica | `ANALISIS-EMBUDO.md` |
| Canónicas, indexación, JSON-LD y Search Console | `SEO.md` |
