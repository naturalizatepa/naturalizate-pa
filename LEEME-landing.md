# Landing «Nacionalidad panameña por naturalización» — Naturalízate.pa

Página de aterrizaje lista para publicar, construida con el sistema de marca
(logo, tipografías, favicons y sistema gráfico oficiales).

**Archivo principal:** `index.html` — ábrelo con doble clic: funciona sin internet,
porque las tipografías y los logotipos van embebidos en el propio archivo.

---

## 1. De qué trata esta página

Servicio principal del despacho: la obtención de la **nacionalidad panameña por
naturalización** para extranjeros con **cédula de identidad de extranjero residente
(cédula E) emitida hace más de 5 años**.

- El recorrido: portada → marco legal → requisitos y autoevaluación → proceso →
  servicio del despacho → preguntas frecuentes → contacto.
- El **marco legal** se explica desde la Constitución Política (artículos 9 a 14):
  los 5 años de residencia, la solicitud mediante abogado ante el **Tribunal Electoral**,
  el examen de naturalización (español, historia, geografía, gobierno y cultura), la
  concesión por el Poder Ejecutivo y el juramento con renuncia a la nacionalidad de origen.
- La **autoevaluación de 5 criterios** se calcula en el navegador (no envía datos) y arma
  un mensaje de WhatsApp con el resultado.
- El **proceso en 5 etapas** describe cómo trabaja el despacho, de la evaluación inicial
  al juramento y la cédula panameña.
- 8 **preguntas frecuentes** basadas en la normativa vigente, marcadas con `FAQPage`
  para aparecer en los resultados de Google.
- Aviso legal: la información es general, no constituye asesoría para un caso
  particular y no se garantizan resultados.

## 2. Marca aplicada

| Elemento | Dónde |
|---|---|
| Logotipo principal navy (trazados reales) | barra de navegación, embebido como SVG en línea |
| Logotipo principal blanco | portada y pie de página |
| Sello circular navy | bloque de perfil del abogado |
| Isotipo N. blanco como marca de agua | imagen para compartir (Open Graph) |
| Favicon `.ico` + `.svg`, apple-touch, PWA | iconos del navegador y del manifiesto |
| Playfair Display + Inter (variables) | embebidas en base64: sin depender de Google Fonts |

Reglas del manual respetadas: paleta navy + neutros (sin acentos), tipografías de marca
en títulos y texto, y **ninguna promesa de resultados**: la comunicación del despacho
evalúa viabilidad y la explica por escrito.

### Técnica
- **Sin dependencias externas**: cero peticiones de red; funciona offline y carga de inmediato.
- **Responsive** probado a 1440 px y 390 px; barra fija con sombra al desplazar.
- Accesibilidad: enlace «saltar al contenido», `aria-label` en iconos, foco visible,
  contraste alto sobre navy, `prefers-reduced-motion` respetado.
- **SEO**: `title`/`description`, canónica, Open Graph + Twitter Card con imagen 1200×630,
  datos estructurados `LegalService` y `FAQPage`, `sitemap.xml` y `robots.txt`.
- Botones con área táctil cómoda en móvil.

---

## 3. Archivos

```
landing-naturalizate-pa/
├── index.html              ← la página (todo embebido: fuentes + logos)
├── 404.html                ← página de error; GitHub Pages la sirve automáticamente
├── og-image.png / .svg     ← imagen al compartir el enlace en WhatsApp o redes
├── favicon.ico · favicon.svg
├── favicon-16x16 · 32x32 · 48x48 · icon-120 · 152 · 167 · 192 · 256 · 384 · 512 · 1024
├── maskable-192x192 · maskable-512x512 · apple-touch-icon-180
├── site.webmanifest        ← instalación como app (PWA)
├── robots.txt · sitemap.xml
└── svg/                    ← logotipos y sello sueltos, para el diseñador o el servidor
```

## 4. Cómo publicar

### En GitHub Pages

**Opción A — despliegue automático (recomendada).** El repo incluye un workflow de
GitHub Actions (`.github/workflows/deploy-pages.yml`) que en cada `push` a `main`
reconstruye la landing desde el generador (instala dependencias, corre
`landing_build.py`, verifica artefactos) y la publica en Pages:

1. Crea el repo y haz push de este proyecto a la rama `main`.
2. En el repo: *Settings → Pages → Source: **GitHub Actions*** (única configuración manual).
3. El workflow corre solo; la página queda en `https://<usuario>.github.io/<repo>/`.
   También se puede lanzar a mano desde la pestaña *Actions* («Run workflow»).

**Opción B — estática.** Sube el contenido de esta carpeta tal cual a la rama `main`
(o `docs/`) y elige *Deploy from a branch*. En un par de minutos la página queda en
`https://<usuario>.github.io/<repo>/`.

4. El `.nojekyll` es imprescindible: evita que GitHub procese el sitio con Jekyll y sirva
   correctamente los archivos que empiezan por punto o con `_`. El build lo regenera siempre.
5. Los enlaces rotos muestran `404.html` (mismo diseño, con botón de vuelta al inicio) —
   GitHub Pages lo detecta solo; se regenera con el build desde `sistema/landing/404.template.html`.
4. Para dominio propio: *Settings → Pages → Custom domain* y ajusta el DNS (CNAME/A).

Todo en la página es relativo y autosuficiente (fuentes, logos y foto embebidos), así que
funciona igual en la raíz o en un subdirectorio de GitHub Pages sin tocar nada.

### En hosting propio

1. Sube **todo el contenido de esta carpeta** a la raíz del dominio (o a una subcarpeta,
   p. ej. `/nacionalidad/`). Conserva los nombres y la subcarpeta `svg/`.
2. Abre `index.html` con un editor y reemplaza el dominio en tres lugares:
   - la etiqueta `<link rel="canonical">` y las etiquetas `og:url` / `og:image`;
   - `sitemap.xml` (`<loc>`);
   - `robots.txt` (línea `Sitemap:`).
3. Verifica el resultado en <https://search.google.com/test/rich-results> (marcado FAQ)
   y en <https://developers.facebook.com/tools/debug/> (imagen al compartir).

### Cambiar el contacto
El correo (`villarreallawyers@proton.me`) aparece en la sección Contacto, el pie y los
datos estructurados. El único WhatsApp de la página es el de la **autoevaluación**:
se activa solo cuando el visitante marca al menos un criterio y envía su resultado
(`wa.me/50762557583` con mensaje precargado, también en la línea 439 aprox. del template).

---

## 5. Cómo regenerarla

La página se genera desde una plantilla; así los logotipos y las tipografías se vuelven
a embeber con la versión vigente de la carpeta de activos:

```bash
cd sistema
python3 landing_build.py     # escribe en ../landing-naturalizate-pa/
python3 landing_shot.py      # capturas de control en landing/shots/
```

- Plantilla editable: `sistema/landing/index.template.html`
  (los marcadores `{{LOGO_NAVY}}`, `{{LOGO_BLANCO}}`, `{{SELLO_NAVY}}`,
  `{{FONTS_CSS}}`, `{{FAVICON_SVG}}` y `{{FOTO_ABOGADO}}` se sustituyen al construir).
- Datos que conviene revisar antes de publicar: el correo y el número de WhatsApp de la autoevaluación.

> Nota: si `cairosvg` no está instalado, la exportación de PNG usa Google Chrome
> automáticamente; para el trazado de tipografías sí hacen falta `uharfbuzz` y
> `fonttools` (`python3 -m pip install -r requirements.txt`).

## 6. Pendientes que no dependen del código

- [x] Foto del abogado guardada en esta carpeta como `foto-alfonso-villarreal.jpg` y embebida: aparece circular en el bloque «Hablemos de su caso». Para cambiarla, reemplace el archivo (jpg/jpeg/png/webp) y regenere con `python3 landing_build.py`; el recorte se centra en el rostro automáticamente. Si faltara, se muestra el sello de marca.
- [ ] Confirmar que `villarreallawyers@proton.me` y `naturalizate.pa` están activos y apuntan al hosting correcto.
- [ ] Revisar con el abogado los criterios de la autoevaluación y las respuestas del FAQ antes de publicar.
- [ ] Añadir analítica (por ejemplo, Plausible o Google Analytics) si se quiere medir conversión.
