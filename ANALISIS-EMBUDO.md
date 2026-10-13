# Análisis del embudo y eliminación de fricción — Naturalízate.pa
**Fecha:** 13 de octubre de 2026 · **Alcance:** `index.html` completo (14 secciones + precalificación) y versión móvil · **Versión:** v4 (formulario express de 3 preguntas + herramienta interna con informe PDF)

---

## 1. Mapa real de la página (verificado en el DOM)

| # | Sección | Función en el embudo |
|---|---|---|
| 1 | `#inicio` Hero + tarjeta de la Evaluación (sin precio) | Promesa y ruta |
| 2 | Cómo se empieza (3 pasos) | Orientación inmediata: qué va a pasar |
| 3 | `#elegibilidad` ¿Es para usted? | Filtro de expectativas |
| 4 | `#solvencia` Solvencia económica | Requisito + rangos de ingreso |
| 5 | `#riesgo` Costo de un expediente incompleto | Dolor / urgencia |
| 6 | `#metodo` Tres pilares + comparativa | Diferenciación |
| 7 | `#proceso` Cinco fases | Confianza procesal |
| 8 | `#abogado` Lic. Villarreal | Autoridad |
| 9 | `#casos` Testimonios | Prueba social |
| 10 | `#evaluacion` Evaluación Estratégica | Oferta núcleo |
| 11 | `#honorarios` Esencial $3,800 · Todo Incluido $5,500 | Precio ancla |
| 12 | `#preguntas` FAQ (17 preguntas) | Objeciones |
| 13 | `#verificar` **Precalificación express (3 preguntas)** | **Conversión** |
| 14 | `#compromiso` + CTA final + footer | Cierre y contacto |

El orden es correcto (dolor → método → autoridad → prueba → precio → objeciones → conversión). El
trabajo de la v4 fue otro: **quitar del formulario público todo lo que no decide el veredicto**.

---

## 2. El cambio de la v4: 3 preguntas en la landing

> **Nota v4.2:** a indicación del despacho se retiró **todo precio de la Evaluación** de las páginas
> (hero, tarjeta de la Evaluación, tarjeta de pago, FAQ, metadatos, guía y mensajes de WhatsApp).
> El flujo comercial no cambia: el visitante ve *qué recibe* y paga con el enlace que le envía
> Patricia por WhatsApp. Efecto esperado en el embudo: menos abandono por precio antes del veredicto,
> y el costo se comunica en la conversación, no en la página pública.

### 2.1 La medición que lo justifica
En la v3 el visitante debía tomar **6 decisiones** antes de ver su veredicto (y 9 en la v2). Cada
decisión es una oportunidad de abandono, y los campos que más abandono generaban —ausencias,
estado civil, disposición al examen, documentos de solvencia— **no cambiaban el veredicto**: eran
datos para el expediente, no para el filtro.

### 2.2 Antes → después

| | v2 | v3 | **v4 (actual)** |
|---|---|---|---|
| Decisiones hasta el veredicto | 9 | 6 | **3** |
| Opciones visibles antes del veredicto | 35 chips | 22 chips | **8 chips + 1 lista** |
| Pantallas del recorrido | 5 | 5 | **3** |
| Tiempo de llenado percibido | ~2 min | ~2 min | **«menos de un minuto»** |
| Campos que pide la landing | 15 | 13 | **3** |

### 2.3 Las tres preguntas y para qué sirve cada una

| Pregunta | Opciones | Qué decide |
|---|---|---|
| 1 · País de origen | lista + «Otro» | Reciprocidad con Panamá (acelera el cómputo) |
| 2 · Años con Cédula E | <3 · 3–5 · >5 · no estoy seguro(a) | Elegibilidad por tiempo de residencia |
| 3 · Ingresos mensuales | <US$1,000 · 1,000–5,000 · 5,001–10,000 · 10,001–20,000+ | Solvencia: perfil directo, con aviso, o educativo |

Todo lo demás (ausencias, estado civil, examen, dependientes, documentos, cita) **no desapareció**:
pasó a la **herramienta interna** `formulario-interno.html` (26 campos), que se usa en la oficina y
**genera el informe PDF del caso**.

### 2.4 Reglas del veredicto (sin bloqueos innecesarios)

| Caso | Veredicto | ¿Puede reservar? |
|---|---|---|
| <3 años de Cédula E **sin** reciprocidad | Educativo: primero completar residencia | **No** (no se le ofrece pagar) |
| <3 años **con** reciprocidad (p. ej. El Salvador) | Apto | Sí |
| Ingresos <US$1,000 | «Requiere revisión de solvencia» | **Sí** — se explica la regla «2 de 3» y se revisa en la Evaluación |
| Todo lo demás | Apto (cita «2 de 3» y examen incluido) | Sí |

La lógica: **filtrar solo cuando el trámite es realmente imposible hoy**; cuando la duda es de
documentos, se acompaña al visitante en lugar de cerrarle la puerta.

### 2.5 El paso de reserva (v4.4)

Solo **nombre y WhatsApp** (más la referencia de pago si hay pago directo). El día y el horario
salieron del formulario: son dos decisiones en el punto de máxima intención y se resuelven mejor en
la conversación con Patricia, que además confirma la agenda del titular.

### 2.6 Correspondencia con la herramienta interna
Cada respuesta express **llega ya marcada** al formulario del despacho: quien atendió por WhatsApp
solo abre `formulario-interno.html`, completa país, cédula e ingresos con lo que el visitante ya
declaró y añade lo demás. El veredicto interno (6 estados: incompleto, cómputo, examen, solvencia
baja, solvencia en revisión, apto 2 de 3, apto falta una, apto sin docs) es el mismo del sitio, con
más detalle, y termina en un **informe PDF de una página** con recomendación operativa y líneas de
firma.

---

## 3. Fricciones eliminadas en las pasadas anteriores (historial)

### 3.1 Entrada
- La puerta bloqueaba la página sin salida → botón **«Prefiero explorar el sitio primero →»** y no
  vuelve a abrirse en la sesión.
- Los CTA solo hacían scroll → ahora **abren la precalificación en el acto** (y dejan de interceptar
  tras reservar).
- Franja **«Cómo se empieza»** (3 pasos + botón «Empezar»).

### 3.2 Formulario
- Ausencias y estado civil salieron del paso 1 (v3) y del formulario público (v4).
- «¿Cuándo podría iniciar?» retirada: se pregunta al agendar.
- Errores específicos por caso + `role="alert"` / `aria-live`.
- **Borrador automático** (`nzq_draft_v3`) con aviso «Recuperamos sus respuestas anteriores»; se
  limpia al confirmar.
- Salida intermedia en el veredicto apto: **«Ver modalidades y honorarios antes de reservar →»**.
- Mensaje de WhatsApp que omite campos vacíos e incluye la sede (Street Mall, Oficina 215).

### 3.3 Móvil y web
- Botón sticky compactado a una línea (46 px) con acceso directo a WhatsApp.
- Campos a 16 px (sin zoom de iOS), áreas seguras del notch, 0 desborde horizontal (390 px).
- `prefers-reduced-motion`, focos visibles, `text-wrap: balance`, ARIA en barras y acordeón.
- Se retiró `content-visibility: auto` (desplazaba los anclajes ~1.200 px).

### 3.4 Bug crítico corregido (detectado en navegador real)
Al reenumerar las pantallas, la función del veredicto seguía enviando a la pantalla equivocada; en
jsdom pasaba inadvertido y solo la prueba de visibilidad en Chromium lo reveló (**el veredicto
quedaba en una pantalla oculta**). Corregido y cubierto con pruebas de visibilidad. En la v4 se
repitió la lección: la salida intermedia se perdió al reescribir el veredicto y se restauró tras
detectarla en la batería automática.

---

## 4. Ya no hay modal de entrada (v4.3)

Hasta la v4.2 el visitante caía en una **ventana con el formulario** encima de la página. Se
eliminó por completo: la página se lee de corrido y el formulario vive en su sección. Razones, por
orden de peso:

1. **Tapaba la propuesta de valor.** Quien llegaba por un anuncio veía un formulario antes de
   entender por qué el despacho es distinto: el mejor activo de la página era lo último que se veía.
2. **Penalizaba el móvil.** Una ventana a pantalla completa en 390 px obliga a decidir antes de leer.
3. **Duplicaba estructura.** Sin modal hay un solo recorrido y un solo punto de conversión.

En su lugar, los **11 botones de acción** llevan a `#verificar` y **enfocan la primera pregunta**:
el visitante decide cuándo empezar. El borrador (`nzq_draft_v3`) sigue intacto.

---

## 5. Medición ya incluida (sin instalar nada)
El sitio emite eventos a `window.dataLayer` (visibles con GTM/GA4 o con el `ENDPOINT_CAPTURA` de
FormSubmit):

`funnel_step {paso: 1|2|3}` · `cta_ir_formulario {texto}` · `funnel_veredicto {resultado}` ·
`embudo_educativo` · `evaluacion_confirmada`

La caída se lee igual de fácil: **cuántos llegan al Paso 2 (veredicto)** y cuántos confirman. El
paso 1 se registra al cargar la página y `cta_ir_formulario` dice **qué botón** llevó al formulario
(hero, precios o barra fija), así se sabe qué mensaje empuja de verdad.

---

## 6. La fricción que queda y no es de diseño
1. **Enlaces de pago vacíos** → hoy: confirmar → esperar el enlace de Patricia → volver a pagar. Al
   pegar `ENLACE_PAGO` / `ENLACE_TARJETA` desaparece un paso completo.
2. **`ENDPOINT_CAPTURA` vacío** → sin datos de abandono no hay optimización posible (FormSubmit es
   gratuito).
3. **Fotografía del abogado** → su ausencia resta autoridad justo antes del precio.
4. **Píxel** → sin él, la puerta y el filtro optimizan a ciegas.

---

## 7. Resultado de la verificación (13 oct 2026)
- **68/68** pruebas automatizadas (jsdom): 3 preguntas exactas, badge «Paso 1 de 3», rutas de
  veredicto (apto / educativo / revisión), reserva y WhatsApp, borrador `nzq_draft_v3`, estructura
  (11 CTA hacia el formulario, FAQ agrupado, sin modal), 26 campos internos, veredicto en vivo y
  bytes del PDF.
- **PDF validados con lector real (pypdf):** 1–2 páginas según el caso, texto con acentos correcto,
  tabla `xref`, trailer y metadatos; informe típico en **una sola página**.
- **Chromium real (escritorio 1440 px y móvil 390 px):** 0 errores de consola, 0 recursos fallidos,
  0 desbordes; recorrido completo ejecutado y **descarga del PDF verificada** con el nombre
  `Informe-NZQ-maria-fernandez-rios-20261013.pdf`; apertura de WhatsApp con el número y el mensaje
  correctos.

---

## 8. Una sola página

El paquete ya no incluye la variante B: al eliminar la ventana de entrada, ambas versiones hacían lo
mismo. Pruebas que sí valdría la pena medir más adelante, sin duplicar archivos: **posición del
formulario** (al final, como ahora, vs. tras «Solvencia») y **titular del hero**. Ver README §6.

---

## 9. Filtros: ¿muchos filtros son contraproducentes? (v4.4)

Pregunta del despacho, con respuesta aplicada al embudo real:

**No por sí solos: lo contraproducente es filtrar mal.** Un filtro se paga cuando **(a)** bloquea
solo a quien no puede avanzar, **(b)** devuelve información útil y **(c)** es el único en su tramo.
Con ese criterio, el embudo tiene **un filtro duro** (años de Cédula E) y **uno blando** (ingresos,
que nunca bloquea), no una escalera de filtros; y se redujo de 9 decisiones a 3.

| Forma de filtrar mal | Estado |
|---|---|
| Filtrar sin devolver nada | Resuelto: cada veredicto explica el porqué y qué hacer |
| Filtrar sin salida (descarte seco) | **Resuelto en la v4.4:** «Avísenme» convierte el descarte legal en contacto futuro |
| Filtrar en el momento de máxima intención | **Resuelto en la v4.4:** la reserva pide 2 campos, no 4 |

**Lo que NO se tocó, a propósito:** la pregunta de ingresos. Es tentador moverla a WhatsApp, pero
ahí se pierde el aviso automático de solvencia (la regla «dos de tres» explicada antes de hablar con
nadie). Esa decisión se toma con datos: `funnel_step` y `funnel_veredicto` ya la miden.

---

## 10. Reestructura v4.3 — qué se revisó y qué se cambió

**Análisis de la estructura** (13 secciones + franjas, medido sobre el HTML):

| Hallazgo | Acción |
|---|---|
| Ventana con el formulario al cargar, encima de la página | **Eliminada** (§4): −6,3 KB de código y una decisión menos para el visitante |
| «Verifique si su perfil encaja» aparecía **dos veces seguidas** (título de sección y del formulario) | El formulario ahora dice «Empiece aquí: tres preguntas» |
| 18 preguntas frecuentes en una lista plana de ~9.600 caracteres | **3 grupos temáticos**: Requisitos y elegibilidad · La Evaluación, el proceso y las garantías · Pagos, agenda y seguridad |
| Los botones de acción abrían una ventana sobre el contenido | Ahora **llevan al formulario y enfocan la primera pregunta** |
| Compensación del anclaje con la barra fija (76 px) | Revisada: ya existía (`section { scroll-margin-top: 92px }`); se descartó añadir una segunda regla que **sumaba 176 px** al salto |
| Dos páginas casi idénticas en el paquete | **Consolidadas en una** (§8) |

**Verificado tras el cambio:** en Chromium (escritorio y móvil): **0 errores de consola**, 0
desbordes, el CTA aterriza la sección a 92 px —bajo la barra— con **la primera pregunta visible en
ambos tamaños**, y el recorrido completo sigue funcionando. Las dos mejoras de la v4.4 (§9) quedaron
cubiertas por la batería —**68/68** pruebas—: aviso con contacto inválido, válido, su mensaje de
WhatsApp y su memoria entre visitas.
