# Landing «Nacionalidad panameña por naturalización» — Naturalízate.pa

Página principal del embudo comercial de Naturalízate.pa: convierte visitas calificadas en
prospectos clasificados y solicitudes de **Auditoría Jurídica de Caso (US$49)** con el
Lic. Alfonso Villarreal.

**Archivo principal:** `index.html` · **Última revisión:** 23 de noviembre de 2026

- **273.363 bytes**, ~2.744 palabras visibles, sin paso de compilación.
- **Cero peticiones externas bloqueantes**: las tres tipografías (`Inter` y `Playfair Display`
  normal/itálica) van embebidas en base64 y `GA4_ID` está vacío hasta configurarse.
- **Activos locales requeridos**: conservar junto a `index.html` la fotografía
  `foto-alfonso-villarreal.jpg`, `og-image.png`, los favicons y `guia.html`.

---

## 1. Estructura real (10 secciones del embudo)

La portada sigue el recorrido estratégico de 6 etapas
(`CONTACTO → CALIFICACIÓN → CONFIANZA → CONVERSIÓN → EVALUACIÓN → CONTRATACIÓN`):

| # | Ancla | Contenido | Función en el embudo |
|---|---|---|---|
| 1 | `#inicio` | Hero: «Su camino hacia la nacionalidad panameña comienza con una evaluación jurídica seria.» + CTAs «EVALUAR MI SITUACIÓN» y «CONOCER EL PROCESO» | Propuesta de valor y posicionamiento |
| 2 | `#servicios-inicio` | Separación clara de dos puertas de entrada: **Orientación Inicial Gratuita** vs. **Auditoría Jurídica de Caso (US$49)** | Diferenciación de alcance |
| 3 | `#quien-puede` | Marco constitucional verificado: Art. 10 (naturalización), Art. 12 (regulación y facultad estatal), Art. 13 (pérdida de nacionalidad derivada y suspensión de ciudadanía), Art. 14 (inmigración) y autoridades competentes (SNM, Tribunal Electoral, Órgano Ejecutivo, Gobernación) | Autoridad y rigor jurídico |
| 4 | `#riesgos` | «¿Por qué revisar su caso antes de presentar una solicitud?» (5 factores de riesgo frecuentes: Cédula E por sí sola, cambios de categoría migratoria, ausencias, nacionalidad de origen y antecedentes documentales) | Conciencia de riesgo |
| 5 | `#auditoria` | **AUDITORÍA JURÍDICA DE CASO — US$49**: modalidad (llamada telefónica con el Lic. Alfonso Villarreal), alcances, aviso de servicio independiente y CTA «SOLICITAR MI AUDITORÍA JURÍDICA» | Oferta núcleo de conversión |
| 6 | `#como-trabajamos` | **¿CÓMO TRABAJAMOS?** en 5 pasos: 1. Nos contacta, 2. Calificamos su caso, 3. Realizamos la auditoría, 4. Determinamos las alternativas, 5. Presentamos una propuesta | Claridad operativa |
| 7 | `#abogado` | Perfil profesional del Lic. Alfonso Villarreal, enfoque exclusivo en naturalización panameña y sede (Scotia Plaza, Piso 7, Av. Federico Boyd) | Confianza y autoridad |
| 8 | `#preguntas` | **12 preguntas frecuentes** en acordeón accesible, sincronizadas con `FAQPage` JSON-LD | Resolución de objeciones |
| 9 | `#contratacion` | «SI SU CASO ES VIABLE, PODEMOS ACOMPAÑARLO DURANTE EL PROCESO»: 7 servicios jurídicos contratables posteriormente bajo propuesta independiente por escrito | Continuidad post-auditoría |
| 10 | `#calificacion` y `#contacto` | Formulario de calificación preliminar de 8 preguntas (no diagnóstico) + cierre de contacto, WhatsApp `+507 6255-7583` y correo `villarreallawyers@proton.me` | Calificación y conversión |

Además, incluye pie institucional con aviso legal y barra fija móvil con acceso directo a
«Evaluar mi situación» y «WhatsApp».

---

## 2. Formulario de calificación preliminar (`#calificacion`)

El formulario **no emite un diagnóstico definitivo** ni declara automáticamente si el
visitante es elegible o inelegible.

### Las 8 preguntas

1. **Nacionalidad**
2. **Año desde que reside en Panamá**
3. **Tipo de residencia actual**
4. **¿Tiene cédula E?**
5. **¿Desde cuándo tiene cédula E?**
6. **¿Ha salido de Panamá durante su residencia?**
7. **¿Actualmente se encuentra en Panamá o en el extranjero?**
8. **¿Tiene vínculo familiar con ciudadanos panameños?**

### Clasificación preliminar y salida a WhatsApp

- Clasifica vías potenciales que ameritan revisión en auditoría: residencia, matrimonio
  cuando corresponda, reciprocidad, hijos panameños cuando aplique u otras situaciones
  migratorias vinculadas a una eventual naturalización.
- Muestra el mensaje institucional de recepción:
  *«Gracias por compartir su información. Sus respuestas nos permitirán conocer mejor su
  situación y determinar qué aspectos deben revisarse antes de recomendarle un procedimiento.»*
- Habilita el botón **«ENVIAR MI INFORMACIÓN POR WHATSAPP»**, abriendo
  `https://wa.me/50762557583` con las 8 respuestas, la clasificación preliminar y los
  parámetros UTM/referrer capturados.

---

## 3. Marca y sistema visual

| Elemento | Aplicación |
|---|---|
| Navy oscuro `#060F17`, `#0D1B2A`, `#1B3A57` | Encabezado, hero, bandas institucionales, títulos y botones primarios |
| Dorado sobrio `#C5A572` | Acentos institucionales, separadores, etiquetas y destaques de auditoría |
| Blanco y grises neutros | Fondos de lectura, tarjetas y jerarquía editorial |
| `Playfair Display` (400–900, normal e itálica) | Titulares y cifras |
| `Inter` (100–900) | Cuerpo de texto, formularios y botones |

Reglas editoriales permanentes:
- Precio visible (**US$49**) sin ocultarlo ni obligar a escribir para conocer el costo.
- Ninguna promesa de aprobación, plazo garantizado o resultado que depende del Estado panameño.
- Enfoque estricto en naturalización panameña (y situaciones migratorias conexas solo cuando
  inciden en una posible vía de naturalización).

---

## 4. Técnica y analítica

- **Peso y carga**: 273.363 bytes en `index.html`; tipografías `.woff2` embebidas en base64;
  sin bloqueos externos.
- **Accesibilidad**: landmarks semánticos, acordeón con `aria-expanded`, menú móvil
  controlado y foco visible.
- **SEO**: canónica autorreferente en todas las páginas, Open Graph y Twitter Card con
  `og-image.png`, JSON-LD `Attorney` y `FAQPage` con **12 preguntas** sincronizadas con el
  HTML, más `guia.html` indexable.
- **Analítica del embudo**: `track()` registra eventos en `window.dataLayer` y mantiene estado
  en `window.NaturalizateFunnel` (`visita_embudo`, `evaluacion_iniciada`,
  `evaluacion_completada`, `whatsapp_click`, `auditoria_solicitada`, `cta_click`, `faq_abierta`)
  con captura de parámetros UTM (`utm_source`, `utm_medium`, `utm_campaign`, `utm_term`,
  `utm_content`) y `referrer`.
- **Puente a GA4**: `GA4_ID = ""` por defecto (sin peticiones externas ni cookies hasta que
  se pegue un ID `G-XXXXXXXXXX`).

---

## 5. Dónde tocar cada cosa

- **WhatsApp**: `WHATSAPP_NUMBER = "50762557583"` al inicio del `<script>` en `index.html` y
  enlaces `wa.me` del HTML.
- **Analítica GA4**: variable `GA4_ID` al inicio del `<script>` de `index.html`.
- **Preguntas frecuentes**: cualquier cambio en `#preguntas` debe replicarse en el bloque
  JSON-LD `FAQPage` del `<head>` para mantener la paridad de 12 preguntas.
- **No ejecutar `site_builder.py` ni `pages_content.py`**: corresponden a un generador
  heredado que sobrescribiría `index.html`.
