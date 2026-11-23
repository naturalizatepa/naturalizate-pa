# SEO de Naturalízate.pa — estado y mantenimiento

Documento de referencia con lo aplicado en el sitio estático de Naturalízate.pa.
Última revisión: **23 de noviembre de 2026** (v6, rediseño del embudo comercial y
Auditoría Jurídica de Caso US$49).

---

## 1. Dominio canónico

El sitio se publica en:

```
https://naturalizatepa.github.io/naturalizate-pa/
```

**`naturalizate.pa` funciona como marca**, no como URL canónica mientras no esté registrado y
configurado en DNS por el despacho. Todas las canónicas, `og:url`, `og:image`, JSON-LD,
`sitemap.xml` y `robots.txt` apuntan al host activo de GitHub Pages.

### Cuando se conecte un dominio propio

1. Registrar el dominio a nombre del despacho.
2. Configurar DNS (`A/AAAA` y `CNAME`) y activar **Custom domain** + **Enforce HTTPS** en
   GitHub Pages.
3. Reemplazar `https://naturalizatepa.github.io/naturalizate-pa/` por el dominio definitivo en
   todos los archivos del repositorio.
4. Verificar la nueva propiedad en Google Search Console y reenviar `sitemap.xml`.

---

## 2. Qué hay indexado hoy

| Página | `robots` | En `sitemap.xml` |
|---|---|---|
| `index.html` (portada) | `index, follow` | Sí (`lastmod: 2026-11-23`) |
| `guia.html` | `index, follow` | Sí (`lastmod: 2026-11-23`) |
| `contacto.html` · `servicios.html` · `vias.html` · `honorarios.html` · `informacion-legal.html` · `verificacion.html` · `aviso-legal.html` | `noindex, follow` | No |
| `404.html` | `noindex` | No |
| `formulario-interno.html` | `noindex, nofollow` | No |

- **`sitemap.xml`**: 2 URLs indexables (`index.html` y `guia.html`), actualizadas al
  `2026-11-23`.
- **`robots.txt`**: `Allow: /` con referencia absoluta al sitemap.
- **`googlef7de84a63b85219f.html`**: archivo de verificación de Google Search Console.
- **`.nojekyll`**: asegura que GitHub Pages sirva los archivos estáticos sin procesamiento
  Jekyll.
- **Archivos retirados**: `variante-dorada.html` y `LEEME-PUBLICAR.md` se eliminaron del
  repositorio para evitar contenido duplicado o tarifas desactualizadas.

---

## 3. Títulos y descripciones vigentes (23 nov 2026)

| Página | `<title>` | Descripción (`meta description`) |
|---|---|---|
| `index.html` | `Naturalización panameña · Auditoría Jurídica de Caso \| Naturalízate.pa` (70 caracteres) | 184 caracteres · destaca evaluación jurídica seria, orientación inicial gratuita y Auditoría Jurídica de Caso por US$49 con el Lic. Alfonso Villarreal |
| `guia.html` | `Requisitos de naturalización en Panamá: marco constitucional y auditoría \| Naturalízate.pa` (90 caracteres) | 169 caracteres · destaca artículo 10 de la Constitución, vías legales, documentos a verificar, autoridades competentes y Auditoría Jurídica de Caso por US$49 |

Ambas páginas cuentan con etiquetas Open Graph (`og:*`) y Twitter Card con `og-image.png`
(1200×630) y `<link rel="canonical">` autorreferente.

---

## 4. Datos estructurados (JSON-LD)

- **Portada (`index.html`)**:
  - `Attorney` con dirección física (`Scotia Plaza, Piso 7, Av. Federico Boyd, Ciudad de
    Panamá`), teléfono WhatsApp, imagen del titular y `priceRange`:
    `Auditoría Jurídica de Caso US$49 · Servicios posteriores mediante propuesta independiente`.
  - `FAQPage` con **12 preguntas y respuestas** sincronizadas con la sección `#preguntas`.
- **Guía (`guia.html`)**:
  - `@graph` con `BreadcrumbList` y `Article` (`dateModified: "2026-11-23"`), alineada con el
    marco constitucional verificado (Arts. 10, 12, 13 y 14) y las autoridades competentes
    (SNM, Tribunal Electoral, Órgano Ejecutivo y Gobernación).

Si se modifica una pregunta frecuente en `index.html`, debe actualizarse tanto el HTML visible
de `#preguntas` como el bloque JSON-LD `FAQPage` para conservar la paridad exigida por Google.

---

## 5. Contenido y arquitectura de enlaces

- La portada presenta de forma transparente las dos entradas (**Orientación Inicial Gratuita**
  y **Auditoría Jurídica de Caso por US$49**), el marco constitucional verificado, 5 riesgos
  frecuentes, metodología de 5 pasos, perfil del Lic. Alfonso Villarreal, 12 FAQs, servicios
  posteriores bajo propuesta independiente y el formulario de calificación de 8 preguntas.
- `guia.html` funciona como recurso informativo indexable de apoyo, enlazado desde la portada
  y alineado con la misma política comercial y jurídica.
- Las páginas de apoyo (`servicios.html`, `honorarios.html`, `vias.html`,
  `informacion-legal.html`, `verificacion.html`, `contacto.html`, `aviso-legal.html`)
  permanecen en `noindex, follow` con contenido coherente y canónica propia.

---

## 6. Pendientes

- [ ] Confirmar la propiedad en **Google Search Console** y enviar `sitemap.xml`.
- [ ] Configurar un ID real en `GA4_ID` (`index.html`) si se desea enviar los eventos de
      `window.dataLayer` a Google Analytics 4.
- [ ] Si se adquiere dominio propio, migrar canónicas, `sitemap.xml` y `robots.txt` según §1.
