# SEO de Naturalízate.pa — estado y mantenimiento

Documento de referencia con lo aplicado según la *Guía de optimización en buscadores
(SEO) para principiantes* de Google Search Central.
Última revisión: **22 de noviembre de 2026** (coincide con la v5 de la landing).

---

## 1. Dominio canónico

El sitio se publica en:

```
https://naturalizatepa.github.io/naturalizate-pa/
```

**`naturalizate.pa` no pertenece al despacho** (además, hoy no tiene DNS y no sirve
contenido). Por eso **ninguna URL del sitio apunta a ese dominio**: ni canónicas, ni
`og:url`, ni JSON-LD, ni `sitemap.xml`, ni `robots.txt`. Todas apuntan al host que
realmente responde.

> Si se dejaran apuntando a un dominio ajeno, Google recibiría señales de
> canonicalización hacia URLs muertas y el sitio no podría posicionarse.

### Cuando se adquiera un dominio propio

Cualquier dominio que el despacho **registre a su nombre** sirve. Recomendaciones:

- Priorizar el `.com` y las variantes de marca: `naturalizatepanama.com`,
  `naturalizate.com.pa`, `naturalizacionpanama.com`.
- Comprobar antes en el registrador que el nombre esté libre; **no dar por hecho que
  `naturalizate.pa` lo está**.
- Usar `www` redirigido al dominio raíz (o al revés), pero solo uno como canónico.

Pasos al conectar ese dominio:

1. **Registrar** el dominio a nombre del despacho (influye en la verificación de
   Search Console).
2. En el DNS: **A/AAAA** para el dominio raíz y **CNAME** `www` →
   `naturalizatepa.github.io` (los valores exactos los muestra GitHub).
3. En el repositorio: **Settings → Pages → Custom domain**. Esto crea el archivo
   `CNAME` y activa la redirección **301** desde `*.github.io`.
4. Activar **Enforce HTTPS** una vez emitido el certificado.
5. Reemplazar el host en todo el repositorio:

```bash
grep -rl 'naturalizatepa.github.io/naturalizate-pa/' . \
  | xargs sed -i 's|https://naturalizatepa.github.io/naturalizate-pa/|https://TU-DOMINIO.com/|g'
```

6. Volver a enviar el sitemap y avisar del cambio de dirección con la herramienta de
   migración de Search Console.

> **Por qué importa el dominio propio:** con él, el sitio se sirve en la raíz y
> `robots.txt` funciona. En una *project page* de GitHub Pages, `robots.txt` se sirve
> en `/naturalizate-pa/robots.txt`, y los rastreadores **solo leen `robots.txt` en la
> raíz del dominio**: hoy ese archivo no tiene efecto. Las directivas `robots` del
> `<head>` sí se respetan.

### Sobre el nombre «Naturalízate.pa»

«Naturalízate.pa» funciona como **marca** en el logotipo, el `<title>`, el JSON-LD y
los textos, y eso es válido. Lo que **no** se hace es usarlo como URL.

---

## 2. Qué hay indexado hoy

| Página | `robots` | En sitemap |
|---|---|---|
| `index.html` (portada) | `index, follow` | Sí |
| `guia.html` | `index, follow` | Sí |
| `contacto.html` · `servicios.html` · `vias.html` · `honorarios.html` · `informacion-legal.html` · `verificacion.html` · `aviso-legal.html` | `noindex, follow` | No |

Las siete interiores, aunque sigan en `noindex`, llevan ya `<link rel="canonical">`
autorreferente: si se decide indexarlas, solo hay que cambiar la directiva `robots`,
darles contenido propio y añadirlas al sitemap.
| `404.html` | `noindex` | No |
| `formulario-interno.html` | `noindex, nofollow` | No |

- **`sitemap.xml`**: dos URLs, con `lastmod` real (portada 2026-11-22; guía
  2026-11-19). Sin `changefreq` ni `priority`, que Google ignora.
- **`robots.txt`**: `Allow: /` y la referencia absoluta al sitemap. Recuerde que en la
  *project page* no tiene efecto (ver §1).
- **`googlef7de84a63b85219f.html`**: archivo de verificación de Search Console. Ya está
  en la raíz; falta confirmar que la propiedad esté activa y enviar el sitemap.
- **`.nojekyll`**: GitHub Pages sirve los archivos tal cual.
- **`site.webmanifest`**: `start_url`, `scope` e `id` relativos (`./`), de modo que al
  instalar la web como app abra `…/naturalizate-pa/` y no la raíz del dominio.
- **Archivos retirados en la v5**: `index` (sin extensión, heredado) y
  `variante-dorada.html`. Ya no existen ni se enlazan; no los vuelva a crear.

> **Decisión (22 nov 2026): se mantienen en `noindex, follow`.** Las siete interiores
> tienen entre 287 y 489 palabras y ninguna recibe enlaces desde la portada, así que
> indexarlas crearía páginas finas y sin recorrido interno. La intención comercial
> —servicios, honorarios, vías— ya la cubren la portada y `guia.html`. Se revisará si
> alguna supera ~700 palabras, se enlaza desde la portada y responde a una consulta
> propia; su canónica ya está puesta.

---

## 3. Títulos y descripciones (medidos el 22 nov 2026)

| Página | `<title>` | Caracteres | Descripción |
|---|---|---|---|
| Portada | `Naturalización panameña · Asesoría jurídica \| Naturalízate.pa` | **61** (578 px) | **151** caracteres |
| Guía | `Requisitos de naturalización en Panamá: Cédula E y solvencia` | **60** | **136** (848 px) |

Google suele mostrar unos **60 caracteres** de título (≈600 px en Arial Bold 20 px) y
**155–160** de descripción. Las dos páginas se acortaron el 22 nov 2026 para entrar
completas: portada 61 caracteres / **578 px** de título y 151 de descripción; guía 60
y **136** (848 px). La descripción de la guía se sincronizó en `meta`, JSON-LD, `og:*`
y `twitter:*`.

En la portada, `og:title` y `twitter:title` repiten el `title` de Google; las
descripciones sociales mantienen su texto propio. Todas usan `og-image.png`
(1200×630). El eslogan de marca permanece en el `slogan` del JSON-LD y en el pie.

---

## 4. Datos estructurados (JSON-LD)

- **Portada:** `Attorney` con `PostalAddress` y `priceRange`
  («Evaluación $49.99 · Honorarios $3,800 - $5,500») + `FAQPage`.
- **Guía:** `BreadcrumbList` + `Article` con autor (`Person: Alfonso Villarreal`),
  `Organization` y `WebSite`.

La `FAQPage` se genera a partir del texto visible: **11 preguntas en el HTML y 11 en el
schema**, y coinciden carácter por carácter. Es el requisito de Google para los
resultados enriquecidos. Si agrega o quita una pregunta, actualice ambos.

---

## 5. Contenido y enlaces internos

- La portada publica la oferta completa: evaluación **$49.99** deducible y honorarios
  **USD 3,800 / 5,500**, con la nota de ITBMS condicional. Es el contenido que sostiene
  las consultas de marca y de precio.
- El formulario tiene **4 pasos** (5 preguntas de filtro + 2 datos de reserva). Los
  **9** llamados a la acción llevan a `#verificar`.
- La portada enlaza a `guia.html` en dos lugares con texto descriptivo («Guía», «Guía de
  contratación»); la guía es la única página de contenido larga del sitio.
- Línea visible de revisión en el pie y `dateModified` en el JSON-LD de la guía.

---

## 6. Pendientes

- [ ] **Decidir el dominio definitivo** (ver §1). Mientras no exista uno propio, el
      canónico es `naturalizatepa.github.io/naturalizate-pa/`.
- [ ] **Confirmar Search Console**: el archivo de verificación ya está publicado; falta
      comprobar la propiedad y enviar `sitemap.xml`.
- [ ] Revisar el informe **Páginas** 2–4 semanas después de enviar el sitemap.
- [x] **Título y descripción de la portada y la guía** acortados el 22 nov 2026 (§3).
- [x] **Mantener las interiores en `noindex`** (decisión del 22 nov 2026, §2).
- [ ] **Si se activa GA4** (ver `LEEME-landing.md`): pegar el ID en `GA4_ID` y
      registrar `resultado`, `perfil` y `pais` como dimensiones personalizadas. La
      cláusula de cookies ya está en `aviso-legal.html#cookies`.
- [ ] Si se compra un dominio: repetir los pasos 2–6 de §1 y reenviar el sitemap.

---

## 7. Prácticas que NO se aplican (según la guía de Google)

- No se usa `meta keywords`: Google lo ignora.
- No se repiten palabras clave de forma artificial (keyword stuffing).
- No se compra ni se intercambia enlaces.
- La longitud del texto no se ajusta a un número «mágico» de palabras.
- El orden de los encabezados no es un factor de posicionamiento, pero **sí** es crítico
  para accesibilidad: por eso se mantiene correcto.
- No se registra el sitio en directorios de dudosa calidad ni se generan páginas puerta.
- No se usa contenido generado solo para buscadores: la portada y la guía se escriben
  para el cliente.
