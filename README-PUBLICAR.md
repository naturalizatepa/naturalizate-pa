# Naturalízate.pa — Guía de publicación

**Actualizada:** 22 de noviembre de 2026 · **Sitio:** 11 páginas HTML, sin paso de compilación.

Esta es la única guía de publicación. Sustituye a `LEEME-PUBLICAR.md`, que se archivó por
duplicarla y por describir una versión anterior del paquete.

---

## 1. Qué hay en la carpeta

| Archivo | Papel |
|---|---|
| `index.html` | Portada y landing completa. CSS y JS inline; **indexable** |
| `guia.html` | Guía de requisitos. **Indexable**, con canónica propia |
| `aviso-legal.html` · `contacto.html` · `honorarios.html` · `informacion-legal.html` · `servicios.html` · `verificacion.html` · `vias.html` | Páginas de apoyo, `noindex, follow`, con canónica propia |
| `404.html` | Error. `noindex` |
| `formulario-interno.html` | Herramienta del despacho. `noindex, nofollow`, no enlazada desde el sitio |
| `robots.txt` · `sitemap.xml` | Dos URLs indexables: portada y guía |
| `_headers` | Seguridad y caché para Netlify / Cloudflare Pages. **No define CSP** |
| `site.webmanifest` · `favicon-*.png` · `apple-touch-icon*.png` | Iconos e instalación como app |
| `styles.css` · `app.js` | Sistema visual y comportamiento de las siete interiores |
| `assets/fonts/` · `fonts/` | Tipografías autoalojadas; las usan páginas distintas, no sobran |
| `foto-alfonso-villarreal.jpg` · `og-image.png` | Retrato y tarjeta social 1200×630 |
| `googlef7de84a63b85219f.html` | Verificación de Search Console. No borrar |

---

## 2. Política comercial vigente

| Concepto | Condición |
|---|---|
| **Evaluación inicial** | **$49.99**, pago único, antes de la cita |
| **Deducible** | Se descuenta de los honorarios si el cliente contrata |
| **Atención** | Solo con **cita previa pagada** |
| **Comprobante** | Al WhatsApp **6255-7583** con nombre y número de documento |
| **Honorarios** | Fijos por escrito: **Esencial $3,800** · **Todo Incluido $5,500** |
| **Medio de pago** | Se coordina por WhatsApp; **no hay pasarela conectada** |

El sitio no promete gratuidad. El formulario prepara un mensaje de WhatsApp; no cobra ni
confirma la cita por sí solo.

---

## 3. Portada y formulario

La portada tiene diez secciones con `id` y un cierre comercial: `#inicio`, `#situacion`,
`#enfoque`, `#proceso`, `#honorarios`, `#diagnostico`, `#abogado`, `#casos`, `#preguntas`,
`#verificar` y `section.final-cta`. Las nueve llamadas a la acción llevan a `#verificar`.

El formulario tiene **cuatro pasos**:

1. **Filtro** (5 preguntas): país, años con Cédula E, ausencias, examen e ingreso.
2. **Veredicto**: perfiles A, B, C y D, además de la ruta por reciprocidad.
3. **Reserva**: nombre, WhatsApp, documento obligatorio, día, horario y modalidad.
4. **Confirmación**: resumen y botón para enviar por WhatsApp.

No guarda borrador: recargar pierde las respuestas.

---

## 4. Cómo publicar

### GitHub Pages (host actual)

1. Suba el contenido a `main` (o a `docs/`) y active *Deploy from a branch*.
2. `.nojekyll` ya está incluido.
3. Con dominio propio, cambie la URL en `<link rel="canonical">`, `og:url`, `og:image`,
   `sitemap.xml` y la línea `Sitemap:` de `robots.txt`.

### Netlify o Cloudflare Pages

Arrastre la carpeta. `_headers` se aplica solo. El dominio se configura en *Domains*.

### Vercel

Despliegue la carpeta o el repositorio. **Vercel no lee `_headers`**: si quiere las mismas
cabeceras, declárelas en `vercel.json`.

### cPanel o hosting tradicional

1. Suba todo el contenido a `public_html/`, conservando nombres y rutas.
2. `_headers` se ignora; para las cabeceras básicas, añada a `.htaccess`:

```apache
<IfModule mod_headers.c>
  Header set X-Content-Type-Options "nosniff"
  Header set X-Frame-Options "SAMEORIGIN"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
```

### Formulario interno

- **Recomendado:** una carpeta poco adivinable, por ejemplo `public_html/interno/formulario.html`.
- Alternativa: no subirlo y usarlo desde el escritorio, con doble clic y sin internet.
- **Nunca** enlazarlo desde la landing.

---

## 5. Antes de publicar

- [ ] Definir el medio de pago del $49.99 (Yappy, transferencia o tarjeta) y si se automatiza.
- [ ] Confirmar el alcance del deducible en ambos planes y su vigencia.
- [ ] Revisión legal de honorarios, deducible, requisitos y plazos por el licenciado.
- [ ] Verificar WhatsApp `50762557583` y correo `villarreallawyers@proton.me`.
- [ ] Fotografía definitiva.
- [ ] **GA4:** pegar el ID en `GA4_ID` (hoy vacío, sin peticiones), registrar `resultado`,
      `perfil` y `pais` como dimensiones personalizadas y revisar la cláusula de
      `aviso-legal.html#cookies`.
- [ ] Search Console: comprobar la propiedad y enviar `sitemap.xml`.
- [x] Siete interiores en `noindex` (decisión del 22 nov 2026); canónica preparada por si se amplían.

---

## 6. Qué se verificó en esta versión

- **Cero peticiones externas** con `GA4_ID` vacío, medido en Chrome con el resolutor DNS bloqueado.
- **Sintaxis** del script inline de la portada (`node --check`), sin errores.
- **286 referencias locales** de HTML, CSS, JS y manifiesto: ninguna falta.
- **Carga headless** de portada, guía, aviso legal y 404: título y `h1` correctos.
- **JSON-LD** de portada y guía válido; 11 preguntas en HTML y 11 en el schema.
- **Canónicas** en portada, guía y las siete interiores; `noindex` solo donde corresponde.
- **Sitemap** válido, con dos URLs y `lastmod` real.

No verificado: revisión visual en navegador real, comportamiento en Safari o Firefox y
aprobación del abogado.

---

## 7. Archivos retirados (no recrear)

`index` sin extensión, `variante-dorada.html`, `site_builder.py`, `pages_content.py`,
`icon-*.png` y `maskable-*.png`, `favicon.svg`, `panama-office.jpg`,
`perfil-villarreal-88.webp` y los duplicados de fotografía y favicon que no estaban
referenciados. Los generadores reescribían `index.html`; por eso se eliminaron.

---

## 8. Documentación relacionada

| Necesidad | Archivo |
|---|---|
| Estructura, marca, formulario y mantenimiento | `LEEME-landing.md` |
| Embudo, eventos y fricción | `ANALISIS-EMBUDO.md` |
| Canonical, indexación y Search Console | `SEO.md` |
