# Naturalízate.pa — Paquete listo para publicar

**Versión:** 19 de noviembre de 2026 (una sola página, sin ventana de entrada)
**Raíz del sitio:** `index.html` debe quedar en `/`.

> Esta guía reemplaza las versiones anteriores del README. La estructura que describían (formulario
> de 3 preguntas, precio de la evaluación oculto, puerta de entrada, captura de leads) **ya no existe**
> en el paquete.

---

## 1. Política comercial vigente

| Concepto | Condición tal como aparece en el sitio |
|---|---|
| **Auditoría inicial del caso** | **$49.99**, pago único, se paga **antes** de la cita |
| **Deducible** | **En su totalidad** de los honorarios si el cliente contrata el trámite |
| **Atención** | Únicamente bajo **cita previa pagada** |
| **Comprobante** | Al WhatsApp **6255-7583** con **nombre** y **número de documento**; con eso se confirma fecha y hora |
| **Honorarios** | Fijos por escrito: **Esencial $3,800** · **Integral $5,500**, con pago fraccionado |
| **Medio de pago** | Patricia lo indica por WhatsApp; el sitio **no** enlaza una pasarela |

**No hay ninguna promesa de gratuidad.** Verificado el 19 nov 2026: cero coincidencias de
«gratis», «gratuita», «sin costo» y «sin compromiso» en los cinco HTML del paquete
(`index.html`, `guia.html`, `formulario-interno.html`, `variante-dorada.html`, `404.html`).

Regla editorial para futuras ediciones: la auditoría **siempre** se presenta como servicio pagado de
$49.99, deducible, y la cita **siempre** como previa y pagada. Nunca «diagnóstico gratis», «primera
consulta sin costo» ni «sin compromiso».

---

## 2. Contenido del paquete

| Archivo | Para qué sirve |
|---|---|
| `index.html` | **Página principal.** 11 secciones + formulario de 4 pasos. Todo el CSS y el JS van inline |
| `guia.html` | Guía de requisitos con la estructura y el copy de la landing (incluye planes y evaluación de $49.99) |
| `formulario-interno.html` | **Herramienta del despacho** (26 campos + informe PDF). `noindex, nofollow`, no enlazada desde el sitio |
| `variante-dorada.html` | Variante dorada del mismo contenido (opcional; `noindex`) |
| `404.html` | Página de error |
| `robots.txt`, `sitemap.xml` | Indexación (host `https://naturalizatepa.github.io/naturalizate-pa/`) |
| `site.webmanifest`, `icon-*.png`, `maskable-*.png` | Iconos PWA / móvil |
| `favicon.ico`, `favicon-*.png`, `apple-touch-icon*.png` | Favicons |
| `foto-alfonso-villarreal.jpg` | Fotografía del licenciado (héroe y datos estructurados) |
| `og-image.png` | Imagen al compartir en WhatsApp y redes (1200×630) |
| `_headers` | Cabeceras de seguridad y caché (solo Netlify / Cloudflare Pages) |
| `LEEME-PUBLICAR.md` | Resumen rápido de publicación |
| `README-PUBLICAR.md` | Este documento |
| `ANALISIS-EMBUDO.md` | Análisis del embudo de una versión anterior; **desactualizado** en precios y flujo |

`formulario-interno.html` no está enlazado desde ninguna página (comprobado). Si no quiere subirlo,
guárdelo en el equipo de la oficina: funciona con doble clic, sin internet.

---

## 3. La landing (`index.html`)

### 3.1 Secciones, en orden

`#inicio` (héroe + tarjeta de la auditoría) · `#elegibilidad` (filtro de entrada) · `#riesgo` ·
`#metodo` · `#proceso` · `#abogado` · `#casos` · `#diagnostico` (auditoría $49.99) ·
`#honorarios` (Esencial $3,800 · Integral $5,500) · `#preguntas` (FAQ) · `#verificar` (formulario) ·
`#compromiso` · cierre con CTA final.

La barra superior muestra siempre **«Auditoría inicial $49.99 · Cita previa pagada · Cédula E +5 años»**
y la barra móvil lleva al formulario.

### 3.2 Formulario: 4 pasos + confirmación

| Paso | Contenido |
|---|---|
| **Paso 1 de 4 · Filtro** | País de origen · años con Cédula E · ausencias prolongadas · disposición al examen · ingreso mensual. Todo con toques, sin escribir (salvo «Otro» país) |
| **Paso 2 de 4 · Resultado** | Veredicto inmediato y personalizado (ver 3.3) |
| **Paso 3 de 4 · Reserva** | Nombre completo · WhatsApp · **número de documento (obligatorio)** · día · horario · modalidad de interés |
| **Paso 4 de 4 · Confirmación** | Resumen completo y botón **Confirmar por WhatsApp** |
| **Éxito** | «Reserva lista»: se abre WhatsApp con el mensaje redactado; la cita se confirma al recibir el comprobante |

Validación en `runBooking()`: exige nombre, documento, WhatsApp con al menos 7 dígitos, día, horario
y modalidad. Si falta algo, el mensaje de error lo indica y no se avanza.

### 3.3 Perfiles del veredicto

- **A — Prioritario**, **B — Viable con revisión**, **C — Requiere verificación**: avanzan a la reserva
  de la auditoría.
- **D — Aún no procede (cómputo insuficiente)**: se explica qué falta y se ofrece reservar la
  auditoría igualmente para revisar el cómputo con documentos.
- **D — Pendiente examen obligatorio**: se explica la ruta y se ofrece la auditoría.
- **Reciprocidad — país (N años)**: los convenios con Panamá se marcan para verificación.

### 3.4 Mensaje de WhatsApp que recibe el despacho

Incluye saludo, nombre, **documento**, WhatsApp, país, cédula E, ausencias, examen, ingreso,
modalidad, día, horario, el **perfil interno**, la línea
«Auditoría inicial: $49.99 (deducible de honorarios). Enviaré el comprobante con mi nombre y número
de documento.» y las UTM cuando existen.

---

## 4. Cómo publicar

### A) Netlify (arrastrar y soltar)
1. **app.netlify.com/drop**.
2. Arrastre la carpeta descomprimida.
3. `_headers` se aplica solo. El dominio propio se configura en *Settings → Domains*.

### B) Vercel
1. **vercel.com → Add New → Project → Deploy**, arrastrando la carpeta.
2. Dominio en *Settings → Domains*.

### C) Hosting tradicional / cPanel
1. Suba **todo el contenido** a `public_html/` (reemplace el `index.html` anterior).
2. Confirme que `favicon.ico`, `og-image.png`, `guia.html` y la fotografía queden en la misma carpeta.
3. `_headers` se ignora en LiteSpeed/Apache; si quiere las mismas cabeceras, pida HTTPS + HSTS a
   soporte o pegue esto en `.htaccess`:

```apache
<IfModule mod_headers.c>
  Header set X-Content-Type-Options "nosniff"
  Header set X-Frame-Options "SAMEORIGIN"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
```

### ¿Dónde pongo `formulario-interno.html`?
- **Recomendado:** carpeta poco adivinable, p. ej. `public_html/interno/formulario.html`. Sigue siendo
  `noindex, nofollow` y nadie llega por casualidad.
- Alternativa: no subirlo y usarlo desde el escritorio de la oficina.
- **Nunca** enlazarlo desde la landing.

---

## 5. Antes de publicar — pendientes que dependen del despacho

1. **Medio de pago del $49.99.** Definir si se cobra por Yappy, transferencia o tarjeta, y si se
   automatiza con un enlace. Hoy el sitio dice que Patricia lo indica por WhatsApp; si se agrega un
   enlace, hay que actualizar también el texto de éxito y el mensaje de WhatsApp.
2. **Alcance del deducible.** El sitio dice «deducible en su totalidad» sin distinguir modalidad.
   Confirmar si aplica a Esencial e Integral por igual y si tiene vigencia (p. ej. 30 días).
3. **Validación legal.** El Lic. Villarreal debe aprobar honorarios, deducible, requisitos y plazos.
   Los requisitos de solvencia provienen de la guía del SNM; los rangos de ingreso son criterio del
   despacho y así se advierte en el texto.
4. **Píxeles** (Meta / Google / GA4) en el `<head>` si se pauta. Con `_headers`, agregue el dominio del
   píxel a `script-src` y `connect-src` o será bloqueado.
5. **Fotografía** definitiva en `foto-alfonso-villarreal.jpg`.
6. **`guia.html`** ya incluye los planes y la evaluación de $49.99; revise que coincidan con la
   propuesta vigente del despacho antes de publicar.

---

## 6. Qué se verificó en esta versión

- **Política de precio:** `grep` sin coincidencias de «gratis», «gratuita», «sin costo» ni
  «sin compromiso» en los cinco HTML; 24 menciones de $49.99 en `index.html`, todas coherentes
  (metadatos, JSON-LD, héroe, tarjeta, diagnóstico, honorarios, FAQ, formulario, éxito, CTA).
- **Sintaxis:** el script inline de `index.html` se evalúa sin errores (`new Function`).
- **Formulario en Chrome sin interfaz:** bloquea el avance sin número de documento, avanza al
  completarlo y lo muestra en el resumen y en el mensaje de WhatsApp.
- **No verificado:** revisión visual en navegador real, comportamiento en Safari/Firefox y pruebas
  automatizadas del paquete anterior (las «68 comprobaciones» correspondían a otra versión y no se
  volvieron a ejecutar).

> Nota legal: los textos comerciales son propuesta del sitio y requieren aprobación del abogado antes
> de publicar.
