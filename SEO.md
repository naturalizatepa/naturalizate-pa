# SEO de Naturalízate.pa — estado y mantenimiento

Documento de referencia con lo aplicado según la *Guía de optimización en buscadores (SEO) para principiantes* de Google Search Central.
Última revisión: **26 de octubre de 2026**.

---

## 1. Dominio canónico

El sitio se publica en:

```
https://naturalizatepa.github.io/naturalizate-pa/
```

**`naturalizate.pa` no pertenece al despacho** (además, hoy no tiene DNS y no sirve contenido).
Por eso **ninguna URL del sitio apunta a ese dominio**: ni canónicas, ni `og:url`, ni JSON-LD, ni `sitemap.xml`, ni `robots.txt`.
Todas apuntan al host que realmente responde.

> Si se dejaran apuntando a un dominio ajeno, Google recibiría señales de canonicalización hacia URLs muertas
> y el sitio no podría posicionarse.

### Cuando se adquiera un dominio propio

Cualquier dominio que el despacho **registre a su nombre** sirve. Recomendaciones:

- Priorizar el `.com` y las variantes de marca: `naturalizatepanama.com`, `naturalizate.com.pa`, `naturalizacionpanama.com`.
- Comprobar primero en el registrador que el nombre esté libre; **no dar por hecho que `naturalizate.pa` lo está**.
- Usar `www` redirigido al dominio raíz (o al revés), pero solo uno de los dos como canónico.

Pasos al conectar ese dominio:

1. **Registrar** el dominio a nombre del despacho (con datos reales: influye en la verificación de Search Console).
2. En el DNS del registrador: registros **A/AAAA** para el dominio raíz y **CNAME** `www` → `naturalizatepa.github.io` (los valores exactos los muestra GitHub).
3. En el repositorio: **Settings → Pages → Custom domain** → el dominio nuevo. Esto crea el archivo `CNAME` y activa la redirección **301** desde `*.github.io` (se conserva el historial, sin penalización).
4. Activar **Enforce HTTPS** una vez emitido el certificado.
5. Reemplazar la constante de dominio en el repositorio:

```bash
grep -rl 'naturalizatepa.github.io/naturalizate-pa/' . \
  | xargs sed -i 's|https://naturalizatepa.github.io/naturalizate-pa/|https://TU-DOMINIO.com/|g'
```

6. Volver a enviar el sitemap en Search Console y avisar del **cambio de dirección** con la herramienta de migración.

> **Por qué importa el dominio propio:** con él, el sitio se sirve en la raíz y `robots.txt` funciona.
> En una *project page* de GitHub Pages, `robots.txt` se sirve en `/naturalizate-pa/robots.txt`, y
> los rastreadores **solo leen `robots.txt` en la raíz del dominio**: hoy ese archivo no tiene efecto.

### Sobre el nombre «Naturalízate.pa»

«Naturalízate.pa» funciona como **marca** en el logotipo, el `<title>`, el JSON-LD y los textos, y eso es válido.
Lo que **no** se hace es usarlo como URL: no hay enlaces, canónicas ni correos apuntando a ese dominio.

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
- `site.webmanifest` con `start_url`, `scope` e `id` relativos (`./`), de modo que al instalar la web como app abra
  `…/naturalizate-pa/` y no la raíz del dominio (que daría 404).

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

## 3. Pendientes

- [ ] **Decidir el dominio definitivo** (ver sección 1). Mientras no exista uno propio, el canónico es `naturalizatepa.github.io/naturalizate-pa/`.
- [ ] **Dar de alta Search Console** para `https://naturalizatepa.github.io/naturalizate-pa/` y enviar `sitemap.xml`
      (funciona aunque el dominio sea de GitHub: el sitemap se envía por ruta absoluta).
- [ ] Verificar la propiedad con la etiqueta HTML de Search Console: se pega en el `<head>` de `index.html`.
- [ ] Revisar el informe **Páginas** de Search Console 2–4 semanas después para confirmar la indexación.
- [ ] Si se compra un dominio: repetir los pasos 2–6 de la sección 1 y reenviar el sitemap.

---

## 4. Prácticas que NO se aplican (según la guía de Google)

- No se usa `meta keywords`: Google lo ignora.
- No se repiten palabras clave de forma artificial (keyword stuffing).
- No se compra ni se intercambia enlaces.
- La longitud del texto no se ajusta a un número «mágico» de palabras.
- El orden de los encabezados no es un factor de posicionamiento, pero **sí** es crítico para accesibilidad:
  por eso se mantiene correcto.
- No se registra el sitio en directorios de dudosa calidad ni se generan páginas puerta.
