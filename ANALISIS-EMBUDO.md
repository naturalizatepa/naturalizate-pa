# Análisis del embudo comercial — Naturalízate.pa

**Fecha:** 23 de noviembre de 2026 · **Alcance:** `index.html` (embudo comercial de 6 etapas
en 10 secciones) y versión móvil · **Versión:** v6 (rediseño estratégico).

---

## 1. Arquitectura comercial (6 etapas)

```
CONTACTO → CALIFICACIÓN → CONFIANZA → CONVERSIÓN → EVALUACIÓN → CONTRATACIÓN
```

Posicionamiento central:
**«Primero evaluamos su caso. Después determinamos si conviene iniciar el proceso.»**

### Mapa de la portada (`index.html`)

| # | Sección (`id`) | Etapa del embudo | Rol comercial |
|---|---|---|---|
| 1 | `#inicio` | Contacto | Propuesta de valor + CTAs «EVALUAR MI SITUACIÓN» y «CONOCER EL PROCESO» |
| 2 | `#servicios-inicio` | Contacto / Calificación | Separación explícita entre **Orientación Inicial Gratuita** y **Auditoría Jurídica de Caso (US$49)** |
| 3 | `#quien-puede` | Confianza | Marco constitucional (Arts. 10, 12, 13 y 14) y competencias institucionales (SNM, Tribunal Electoral, Órgano Ejecutivo, Gobernación) |
| 4 | `#riesgos` | Confianza | 5 riesgos frecuentes que justifican revisar el caso antes de presentar una solicitud |
| 5 | `#auditoria` | Conversión / Evaluación | Oferta núcleo **US$49** — llamada telefónica con el Lic. Alfonso Villarreal, alcances y límite de servicio independiente |
| 6 | `#como-trabajamos` | Confianza / Evaluación | Metodología clara en 5 pasos |
| 7 | `#abogado` | Confianza | Autoridad profesional del Lic. Alfonso Villarreal y especialidad en naturalización |
| 8 | `#preguntas` | Confianza / Conversión | 12 preguntas frecuentes verificadas (sin promesas ni tarifas ocultas) |
| 9 | `#contratacion` | Contratación | 7 servicios posteriores contratables por separado bajo propuesta escrita si el caso es viable |
| 10 | `#calificacion` y `#contacto` | Calificación / Conversión | Formulario de 8 preguntas + transferencia estructurada a WhatsApp `+507 6255-7583` |

---

## 2. Separación de las dos puertas de entrada

### A. Orientación Inicial Gratuita
- Primer contacto breve para conocer nacionalidad, estatus migratorio general y necesidad.
- Permite clasificar preliminarmente el caso e indicar el siguiente paso.
- **Límites explícitos:** no incluye opinión jurídica, revisión completa de expediente,
  análisis exhaustivo, diagnóstico definitivo de elegibilidad, redacción legal ni garantía de
  aprobación.

### B. Auditoría Jurídica de Caso — US$49
- Precio transparente y visible en la página (**US$49**).
- Modalidad: **llamada telefónica con el Lic. Alfonso Villarreal**.
- Incluye análisis de antecedentes, revisión de documentos pertinentes aportados por el
  cliente, evaluación migratoria, identificación de riesgos u obstáculos, posibles vías
  legales, requisitos y próximos pasos.
- **Servicio independiente:** no incluye automáticamente representación legal, redacción de
  escritos, presentaciones, recursos ni trámites administrativos o judiciales; cualquier
  servicio posterior se cotiza por separado por escrito.

---

## 3. Formulario de calificación preliminar (`#calificacion`)

- **8 preguntas obligatorias de contexto**: nacionalidad, año de residencia en Panamá, tipo
  de residencia actual, tenencia de Cédula E, fecha de Cédula E, salidas de Panamá, ubicación
  actual (Panamá o extranjero) y vínculo familiar con panameños.
- **Regla jurídica clave:** nunca declara elegibilidad ni inelegibilidad automática; clasifica
  posibles vías a revisar (residencia, matrimonio cuando corresponda, reciprocidad, hijos
  panameños cuando aplique u otras situaciones migratorias) y deriva a WhatsApp con el mensaje
  estructurado.
- **Mensaje post-envío:** *«Gracias por compartir su información. Sus respuestas nos
  permitirán conocer mejor su situación y determinar qué aspectos deben revisarse antes de
  recomendarle un procedimiento.»* + botón **«ENVIAR MI INFORMACIÓN POR WHATSAPP»**.

---

## 4. Medición del embudo (`window.dataLayer` y `window.NaturalizateFunnel`)

| Evento | Cuándo se dispara | Propósito |
|---|---|---|
| `visita_embudo` | Al cargar `index.html` | Volumen de visitas y fuente/UTM |
| `cta_click` | Al pulsar CTAs estratégicos | Eficiencia de llamados a la acción |
| `evaluacion_iniciada` | Al interactuar por primera vez con el formulario de 8 preguntas | Inicio de calificación |
| `evaluacion_completada` | Al completar y enviar las 8 preguntas | Prospecto calificado + vías preliminares |
| `auditoria_solicitada` | Al pulsar los CTAs de Auditoría Jurídica (US$49) | Intención directa de compra |
| `whatsapp_click` | Al abrir WhatsApp desde botones o desde el resultado del formulario | Conversión a contacto directo |
| `faq_abierta` | Al desplegar una pregunta frecuente | Objeciones más consultadas |

Todos los eventos incluyen atribución de origen (`utm_source`, `utm_medium`, `utm_campaign`,
`utm_term`, `utm_content` y `referrer`), y el mensaje enviado a WhatsApp incluye también la
fuente capturada para medir conversión real fuera del sitio.

- Con `GA4_ID = ""`, la telemetría se registra en `window.dataLayer` sin peticiones externas.
- Al configurar un Measurement ID `G-XXXXXXXXXX` en `GA4_ID`, `index.html` carga `gtag.js` y
  reenvía automáticamente los eventos a GA4.

---

## 5. Verificación realizada (23 nov 2026)

- Carga HTTP `200 OK` en todas las páginas y recursos locales.
- Validación de sintaxis JS (`node --check`) y ejecución del flujo completo de eventos,
  clasificación no diagnóstica y armado de mensaje WhatsApp en simulación DOM.
- Comprobación de que los 12 ítems de `#preguntas` coinciden con `FAQPage` JSON-LD.
- Comprobación de cero peticiones externas bloqueantes con `GA4_ID = ""`.

---

## 6. Mejoras opcionales futuras

1. **Activar GA4**: pegar un ID real en `GA4_ID` dentro de `index.html` y configurar
   conversiones en Google Analytics 4 (`evaluacion_completada`, `auditoria_solicitada`,
   `whatsapp_click`).
2. **Cobro en línea de la Auditoría (US$49)**: añadir un enlace de pago directo si el
   despacho decide automatizar el pago previo a la llamada telefónica.
3. **Integración CRM / seguimiento**: registrar sistemáticamente la etapa de cada contacto
   (`calificado → auditoría pagada → llamada realizada → propuesta enviada → contratado`).
