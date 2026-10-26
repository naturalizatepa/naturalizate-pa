# SEO de Naturalízate.pa — estado y mantenimiento

Documento de referencia con lo aplicado según la *Guía de optimización en buscadores (SEO) para principiantes* de Google Search Central.
Última revisión: **26 de octubre de 2026**.

---

## 1. Dominio canónico (acción pendiente)

El sitio se publica hoy en:

```
https://naturalizatepa.github.io/naturalizate-pa/
```

**`naturalizate.pa` no tiene DNS configurado**, por lo que no sirve contenido. Por eso todas las URLs canónicas
(`<link rel="canonical">`, `og:url`, JSON-LD, `sitemap.xml` y `robots.txt`) apuntan al host que **sí responde**.
Si se dejaran apuntando a un dominio inexistente, Google recibiría señales de canonicalización hacia URLs muertas
y el sitio no podría posicionarse.

### Cuando se conecte `naturalizate.pa`

1. **Repositorio → Settings → Pages → Custom domain** → `naturalizate.pa` (esto crea el archivo `CNAME` y activa la redirección 301 desde `*.github.io`).
2. En el proveedor de DNS: registrar los registros que indique GitHub (A/AAAA para el dominio raíz y CNAME `www`).
3. Activar **Enforce HTTPS**.
4. Reemplazar la constante de dominio en el repositorio (todas las apariciones):

```bash
grep -rl 'naturalizatepa.github.io/naturalizate-pa/' . | xargs sed -i 's|https://naturalizatepa.github.io/naturalizate-pa/|https://naturalizate.pa/|g'
```

5. Volver a enviar el sitemap en Search Console.

> **Por qué importa:** con dominio propio el sitio se sirve en la raíz y `robots.txt` funciona.
> En una *project page* de GitHub Pages, `robots.txt` se sirve en `/naturalizate-pa/robots.txt` y
> los rastreadores **solo leen `robots.txt` en la raíz del dominio**, así que hoy ese archivo no tiene efecto.

---

## 2. Qué se optimizó

### Rastreo e indexación
- `sitemap.xml` con las **2 URLs canónicas e indexables** y `lastmod` real. Sin `changefreq` ni `priority` (Google los ignora).
- `robots.txt` con `Allow: /` y la referencia absoluta al sitemap.
- `variante-dorada.html` → `noindex, nofollow` (es una variante visual del mismo contenido: evita contenido duplicado).
- `formulario-interno.html` → `noindex, nofollow`.
- `404.html` → `noindex`.
- `index` (archivo sin extensión, heredado y huérfano) → `noindex, follow`.
- `.nojekyll` para que GitHub Pages sirva los archivos tal cual.

### Enlaces de título y fragmentos
| Página | `<title>` | Caracteres |
|---|---|---|
| Inicio | `Naturalización en Panamá desde la Cédula E \| Naturalízate.pa` | 60 |
| Guía | `Requisitos de naturalización en Panamá: Cédula E y solvencia` | 60 |

Cada página tiene su propia `meta description` (154–159 caracteres) con la propuesta de valor,
la ubicación y el diferenciador. `og:*` y `twitter:*` replican el mismo texto.

### Datos estructurados (JSON-LD)
- **Inicio:** `Attorney` (`#despacho`) + `WebSite` (`#sitio`) + `WebPage` (`#pagina`) + `FAQPage` (`#preguntas-frecuentes`).
- **Guía:** `BreadcrumbList` + `Article` con autor (`Person: Alfonso Villarreal`) y `dateModified`.
- La **FAQPage se genera a partir del texto visible**: las 6 preguntas y respuestas coinciden carácter por carácter
  con lo que ve el usuario, requisito de Google para los resultados enriquecidos.

### Enlaces internos
- Enlaces contextuales desde el cuerpo de la página de inicio hacia la guía, con texto descriptivo
  («la guía completa de requisitos de naturalización», «la guía del proceso de naturalización paso a paso»).
- Anclas de navegación y pie mejoradas: «Guía» → «Guía de requisitos».

### Frescura y autoría
- Línea visible «Contenido revisado y actualizado en octubre de 2026» en el pie de ambas páginas.
- `dateModified` en el JSON-LD y autoría explícita del abogado en el `Article`.

### Ya resuelto en iteraciones anteriores
- Accesibilidad 100 y SEO 100 en PageSpeed Insights.
- Jerarquía de encabezados correcta y un único `<h1>` por página.
- `<main>` como punto de referencia principal.
- Imágenes con `alt` descriptivo, `width`/`height` y `loading="lazy"`.

---

## 3. Pendientes que dependen de terceros

- [ ] **Conectar `naturalizate.pa`** (ver sección 1).
- [ ] **Dar de alta Search Console** para `https://naturalizatepa.github.io/naturalizate-pa/`
      (o para el dominio propio) y enviar `sitemap.xml`.
- [ ] Verificar la propiedad con la etiqueta HTML de Search Console: se pega en el `<head>` de `index.html`.
- [ ] Revisar el informe **Páginas** de Search Console 2–4 semanas después para confirmar la indexación.

---

## 4. Prácticas que NO se aplican (según la guía de Google)

- No se usa `meta keywords`: Google lo ignora.
- No se repiten palabras clave de forma artificial (keyword stuffing).
- No se compra ni se intercambia enlaces.
- La longitud del texto no se ajusta a un número «mágico» de palabras.
- El orden de los encabezados no es un factor de posicionamiento, pero **sí** es crítico para accesibilidad:
  por eso se mantiene correcto.
