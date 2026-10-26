# Naturalízate.pa — Paquete listo para publicar (v4.4 · 13 oct 2026)

Este ZIP contiene el sitio optimizado, listo para subir tal cual. Descomprima y publique el
contenido **en la raíz** de su dominio (el `index.html` debe quedar en `/`).

> **Novedad de la v4:** el formulario público se redujo a **3 preguntas** (país, años con Cédula E
> e ingresos) y el formulario largo del despacho pasó a `formulario-interno.html` (genera el PDF).
>
> **Novedad de la v4.3 (estructura):** **se eliminó la ventana que aparecía al cargar la página.**
> Ahora la página se lee libre y el formulario vive integrado en su sección; cualquier botón de
> acción lleva allí. Además: preguntas frecuentes agrupadas en 3 bloques, títulos sin duplicar y
> **una sola página**.
>
> **Novedad de la v4.4 (conversión):**
> 1. **«Avísenme» en el veredicto educativo.** Quien aún no cumple el cómputo ya no se pierde: deja
>    su WhatsApp o correo (opcional), sale un mensaje ya redactado hacia el despacho y el contacto
>    queda recordado en su navegador para la próxima visita.
> 2. **La reserva pide 2 campos, no 4.** El día y el horario se coordinan en la conversación con
>    Patricia; el paso 3 quedó en **nombre + WhatsApp** (y la referencia de pago si hay pago directo).

---

## 0. Los dos formularios: cuál es cuál

| | **Landing pública** (`index.html`) | **Herramienta interna** (`formulario-interno.html`) |
|---|---|---|
| Preguntas | **3** (país · años con Cédula E · ingresos) | **26 campos** completos del despacho |
| Para quién | El visitante que llega por anuncio/Google | Usted o Patricia, en la oficina o el teléfono |
| Termina en | Veredicto + reserva de la Evaluación (WhatsApp) | **Informe PDF** descargable del caso |
| Indexable | Sí (`index, follow`) | **No** (`noindex, nofollow` — nunca aparece en Google) |
| Datos | Solo en el navegador del visitante (borrador) | Solo en su equipo: nada viaja a ningún servidor |

---

## 1. Contenido del paquete

| Archivo | Para qué sirve |
|---|---|
| `index.html` | **Página principal** — 13 secciones + formulario express de 3 preguntas integrado en «Verificar» (sin ventanas al cargar) |
| `formulario-interno.html` | **Herramienta del despacho** — formulario largo (26 campos) con veredicto en vivo y **generador de informe PDF** |
| `guia.html` | Guía de contratación (el menú apunta aquí en los dos casos) |
| `og-image.png` | Imagen para compartir en WhatsApp / redes (1200×630) |
| `foto-alfonso-villarreal.jpg` | **Provisional** con monograma «AV». Sustitúyala por la fotografía real |
| `favicon.ico`, `favicon-16/32/48.png`, `apple-touch-icon-180.png`, `icon-512.png` | Iconos del sitio |
| `site.webmanifest` | Instalación como app en móvil (PWA básica) |
| `robots.txt`, `sitemap.xml` | Indexación en Google (host `naturalizatepa.github.io/naturalizate-pa/`) |
| `_headers` | Cabeceras de seguridad y caché (solo Netlify / Cloudflare Pages) |
| `ANALISIS-EMBUDO.md` | Análisis del embudo y las fricciones eliminadas (con cifras) |
| `README-PUBLICAR.md` | Este documento |

`formulario-interno.html` **no está enlazado desde ninguna página del sitio** (comprobado). Si no quiere
subirlo, guárdelo en el escritorio de la oficina: funciona abriéndolo con doble clic, sin internet.

---

## 2. Qué cambió en la v4

> **Ajustes v4.1 y v4.2 (13 oct 2026):**
> 1. Se eliminaron del sitio las **dos menciones de «auditoría»** (pilar I y FAQ), sin texto sustituto.
> 2. Se eliminó **el importe de la Evaluación Estratégica** (era el «costo de la auditoría»): metadatos, JSON-LD, hero, tarjeta de la Evaluación, tarjeta de pago, textos del
>    formulario, mensajes de WhatsApp, la guía y el informe PDF interno. Las tarjetas muestran
>    ahora «30 min · 100% aplicable al proceso» y los botones «Pagar con Yappy / Pagar con tarjeta».
>    **La página ya no menciona cifra alguna por la evaluación**.
>
> **Ajuste v4.5 (17 oct 2026):**
> 1. **Se retiraron los montos de los dos paquetes** ($3,800 / $5,500) de la landing y de la guía:
>    las tarjetas muestran «Propuesta a medida · honorarios fijos por escrito» y el precio se
>    entrega en la propuesta personalizada.
> 2. **Ventana de bienvenida estilo WhatsApp** al cargar la página (una vez por sesión): reproduce
>    la conversación con el mensaje de metodología del despacho y enlaza a WhatsApp con el texto
>    ya redactado. Se cierra con la X o con Esc y no vuelve a aparecer en la misma sesión.
>    Para desactivarla en pruebas o campañas, añada `?nopopup=1` a la URL.

### 2.1 La landing ahora pregunta solo 3 cosas
1. **País de origen** (lista con opción «Otro»).
2. **Años con Cédula E**: menos de 3 · entre 3 y 5 · más de 5 · no estoy seguro(a).
3. **Ingresos mensuales de referencia**: menos de US$1,000 · US$1,000 a 5,000 · US$5,001 a 10,000 ·
   US$10,001 a 20,000 o más.

Lo demás (ausencias, estado civil, disposición al examen, documentos, agenda con día y hora) **salió
del formulario público** y vive en la herramienta interna. El recorrido quedó en **3 pantallas**:

| Pantalla | Contenido |
|---|---|
| **Paso 1 de 3 · Tres preguntas** | Las 3 preguntas · aviso de que el examen va incluido · guardado automático |
| **Paso 2 de 3 · Resultado** | Veredicto inmediato según las respuestas (+ «Avísenme» si aún no cumple el cómputo) |
| **Paso 3 de 3 · Reserva** | Nombre y WhatsApp → se abre WhatsApp con todo escrito; el día y la hora se coordinan ahí |

### 2.2 El veredicto sigue filtrando, sin bloquear de más
- **Menos de 3 años con Cédula E y sin reciprocidad** con Panamá → veredicto **educativo**: se explica
  que primero hay que completar el tiempo de residencia. **No se le ofrece pagar**, pero puede pedir
  **«Avísenme»** y quedar en la base de contactos futuros.
- **Menos de 3 años con reciprocidad** (El Salvador, y los países que Migración reconoce) → **sí avanza**.
- **Ingresos menores a US$1,000** → veredicto **«Requiere revisión de solvencia»**: se le explica que
  el requisito se prueba con **dos (2) de las tres** pruebas documentales y **puede reservar igualmente**
  (la revisión fina se hace en la Evaluación).
- **Todo lo demás** → **perfil apto**, citando la regla «dos de tres» y que el examen de naturalización
  va incluido.

### 2.3 La herramienta interna (`formulario-interno.html`)
- **Sección A · Datos**: nombre, WhatsApp, correo, país, años con Cédula E, ausencias, estado civil,
  disposición al examen, dependientes, modalidad recomendada.
- **Sección B · Solvencia**: rango de ingresos y las tres pruebas documentales (Declaración de Renta
  2 años con CPA y notario · Carta bancaria al SNM · Carta de trabajo con ficha CSS), más notas de
  verificación.
- **Sección C · Comercial y cita**: objetivo, situación de inversión, disponibilidad, quién atiende,
  fecha y hora de cita, preferencia del solicitante, referencia de pago, abono y honorarios, notas
  internas del caso.
- **Veredicto en vivo** mientras escribe (insignia de color + explicación + recomendación).
- **Botones**: `Generar informe PDF` · `Copiar resumen` (texto para pegar en un chat o correo) ·
  `Enviar por WhatsApp` · `Limpiar` (borra el caso del equipo).
- **Borrador propio** (`nzq_interno_v1`): si cierra la pestaña, al volver encuentra el caso donde lo dejó.
  Se limpia al pulsar **Limpiar**.

### 2.4 El informe PDF
- Un clic en **Generar informe PDF** descarga `Informe-NZQ-<nombre>-AAAAMMDD.pdf`.
- **Una página** en el caso típico (dos si las notas internas son largas). Un caso con muchísimos
  campos llenos también puede ocupar dos.
- Contenido: cabecera con la marca y **Scotia Plaza, Piso 7. Av. Federico Boyd, Panamá, Provincia de Panamá**, datos del
  solicitante, solvencia, perfil comercial y cita, **veredicto con insignia de color** y la
  **recomendación operativa**, notas internas, líneas de firma y pie «Documento interno del despacho.
  No constituye asesoría legal al solicitante. Naturalízate.pa · Lic. Alfonso Villarreal».
- Los campos vacíos **no se imprimen** (el informe sale limpio, sin guiones sueltos).
- **Sin dependencias ni internet**: el PDF se construye dentro del propio archivo. No se envía nada a
  ningún servidor; el caso no sale de su computadora.

---

## 3. Cómo publicar (3 opciones)

### A) Netlify (la más rápida, arrastrar y soltar)
1. Entre a **app.netlify.com/drop**.
2. Arrastre la **carpeta descomprimida** (o el ZIP).
3. Listo: revisa la URL temporal `https://naturalizatepa.github.io/naturalizate-pa/`. Solo si algún día se registra un dominio propio: *Settings → Pages → Custom domain* (ver `SEO.md`).
   El archivo `_headers` se aplica automáticamente.

### B) Vercel
1. **vercel.com → Add New → Project → Deploy** y arrastre la carpeta.
2. Agregue el dominio en *Settings → Domains*.

### C) Hosting tradicional / cPanel (su proveedor actual)
1. Suba **todo el contenido** a `public_html/` (reemplace el `index.html` anterior).
2. Verifique que `favicon.ico`, `og-image.png` y `guia.html` queden en la misma carpeta.
3. En cPanel (LiteSpeed/Apache) el archivo `_headers` **se ignora**; si desea las mismas cabeceras,
   pida a soporte activar HTTPS + HSTS, o pegue esto en `.htaccess`:

```apache
<IfModule mod_headers.c>
  Header set X-Content-Type-Options "nosniff"
  Header set X-Frame-Options "SAMEORIGIN"
  Header set Referrer-Policy "strict-origin-when-cross-origin"
</IfModule>
```

### ¿Dónde pongo `formulario-interno.html`?
- **Recomendado:** en una carpeta de nombre poco adivinable, p. ej. `public_html/interno/formulario.html`.
  Sigue siendo `noindex, nofollow`, pero además nadie llega por casualidad.
- Alternativa: **no subirlo** y usarlo desde el escritorio de la oficina (funciona sin internet).
- Nunca lo enlace desde la landing: así está ahora y así debe quedar.

---

## 4. Antes de publicar — 4 datos que dependen de usted

1. **Enlaces de pago (importante).** En `index.html`, dentro del `<script>`, están estas líneas:
   ```js
   var ENLACE_PAGO = "";     // Yappy
   var ENLACE_TARJETA = "";  // Stripe / PayPal
   ```
   - Si ambos están vacíos (como vienen), funciona el **modo manual**: Patricia recibe la solicitud
     por WhatsApp y envía el enlace de pago. El botón se oculta solo.
   - Si pega uno o ambos, el usuario paga antes de escribir y el mensaje de WhatsApp ya incluye la
     referencia de pago. **El monto de la Evaluación no se muestra en la página** (así quedó por su
     indicación): comuníquelo en el enlace de pago o por WhatsApp.
2. **Captura de leads (opcional).** `var ENDPOINT_CAPTURA = "";` → pegue su URL de FormSubmit
   (`https://formsubmit.co/ajax/su-correo`) para guardar perfil, veredicto y abandono.
3. **Fotografía.** El paquete incluye una **imagen provisional** con el monograma «AV». Reemplácela por
   la fotografía real del licenciado (cuadrada, 400×400 o mayor).
4. **Píxeles.** Si pauta con Meta/Google/GA4, pegue el script en el `<head>`. Si usa las cabeceras
   `_headers`, agregue también el dominio del píxel en `script-src` y `connect-src`; de lo contrario
   el píxel será bloqueado por la política de seguridad.

---

## 5. Qué se probó antes de entregar

- **68/68 comprobaciones automatizadas** sobre los tres HTML reales (jsdom): las 3 preguntas exactas,
  el badge «Paso 1 de 3», las rutas de veredicto (apto / educativo / revisión de solvencia), la reserva
  completa, el borrador `nzq_draft_v3`, la estructura (CTA, FAQ agrupado, sin modal), los 26 campos internos, el veredicto en vivo y
  la validez de los bytes del PDF.
- **Los PDF se abrieron con un lector real (pypdf):** página(s), texto en español con acentos, tabla
  `xref`, trailer y metadatos correctos. Muestras en `muestras/` del proyecto (no van en el ZIP).
- **Chromium real, escritorio (1440 px) y móvil (390 px):** 0 errores de consola, 0 recursos fallidos,
  0 desbordes horizontales; el recorrido completo (3 preguntas → veredicto → reserva → WhatsApp) se
  ejecutó sin fallos y **el PDF se descargó con su nombre correcto** desde el navegador.

> Nota legal: los requisitos de solvencia se transcribieron de la guía oficial del Servicio Nacional
> de Migración («dos (2) de las siguientes opciones»). Los rangos de ingreso son un criterio
> orientativo del despacho, tal como usted los definió, y la página lo dice expresamente para no
> prometer un mínimo legal que la norma no fija. Conviene que el Lic. Villarreal valide el texto
> antes de publicar.

---

## 6. Una sola página (la prueba A/B quedó superada)

Hasta la v4 el paquete incluía dos archivos: **A** (`index.html`, con la ventana al cargar) y **B**
(`index-b.html`, lectura libre). Al eliminar la ventana, A y B hacen exactamente lo mismo, así que
**se conserva una sola página** y el paquete pesa menos y se publica más simple.

Si más adelante quiere volver a medir dos enfoques, hay dos pruebas que sí valen la pena y se
pueden montar sobre el mismo archivo sin duplicarlo:
1. **Posición del formulario**: al final (como ahora) vs. justo después de «Solvencia».
2. **Titular del hero**: el actual vs. uno centrado en el veredicto («Sepa en un minuto si su caso
   procede»).

Los eventos ya están listos (`cta_ir_formulario`, `funnel_step`, `funnel_veredicto`,
`evaluacion_confirmada`), así que cualquiera de las dos se puede comparar en `window.dataLayer`
sin tocar nada más.
