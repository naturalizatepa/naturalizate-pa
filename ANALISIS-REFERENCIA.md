# Análisis de la referencia y adaptación a Naturalízate.pa

**Referencia estudiada:** https://www.kerycruz.com/es · **Revisión:** 19 de noviembre de 2026.

## 1. Portada: anatomía medida en navegador

A 1440 px de ancho, la web original coloca el contenido en un lienzo blanco de **1040 px** centrado sobre fondo gris (`x = 200…1240`). Su lectura visual sigue este orden:

| Parte | Referencia observada | Adaptación entregada |
|---|---|---|
| Franja superior | 56 px; selector de idioma con banderas | 56 px; «Panamá · Español» y contacto. No se ofrecen idiomas no traducidos. |
| Cabecera | 129 px; logotipo centrado | 129 px; SVG oficial de Naturalízate.pa y descriptor del despacho. |
| Navegación | 50 px; banda azul y menús desplegables de varios niveles | 50 px; navy oficial, menú con enlaces y submenús funcionales. |
| Imagen panorámica | 1040 × 513 px, sin texto promocional | La misma proporción; ilustración original de oficina, rotulada como ilustrativa. |
| Búsqueda | Línea de 37 px inmediatamente bajo la imagen | Buscador local de páginas y temas, con resultados y navegación por teclado. |
| Cuerpo | Artículo izquierdo de unos 780 px y barra lateral derecha de 260 px | Columna 75/25; titular, retrato, presentación y nueve enlaces relacionados. |
| Pie | Tres columnas blancas: formulario/contacto/ubicación; línea de copyright | Las tres columnas con datos reales, esquema de mapa, logo y nota legal. |

La portada original mide unos **2080 px** de alto en ese navegador; la portada adaptada ronda **1950 px** con la misma composición general. En móvil el original apila las columnas, pero presenta **desbordamiento horizontal** (477 px de contenido en un viewport de 390 px) y controles superpuestos; la adaptación conserva el apilado y corrige esos problemas.

### Detalles de la referencia que la primera propuesta no reproducía

- En la referencia, los servicios detallados **no** se presentan como tarjetas debajo de la portada: se abren desde páginas del menú.
- La barra lateral contiene enlaces temáticos a procesos migratorios y nacionalidad, no una tarjeta de CTA.
- El pie es **blanco**, no un gran bloque oscuro. Tiene un formulario con nombre, correo, mensaje y casilla para boletines; una columna de datos de contacto; y una columna de ubicación.
- La página «Contáctenos» posee un formulario propio y un mapa adicional; el formulario del pie aparece de nuevo en todas las páginas.
- Las páginas «Tarifas», «Información Legal Gratuita», «Descargo» y «Calculadora de Impuestos» tienen diseños de contenido distintos, aunque comparten cabecera, búsqueda y pie.

## 2. Arquitectura de navegación: equivalencias

| Sitio de referencia | Sitio entregado | Criterio |
|---|---|---|
| Inicio | `index.html` | Portada editorial fiel a la estructura original. |
| Áreas de Práctica + menú | `servicios.html` + submenú | Solo evaluación, expediente, representación y seguimiento de naturalización. |
| Propiedades | `vias.html` | Se sustituye el catálogo inmobiliario por vías de naturalización; no se inventan inmuebles. |
| Tarifas | `honorarios.html` | Tabla de servicio, alcance y propuesta; sin cifras no confirmadas. |
| Descargo | `aviso-legal.html` | Información general, relación profesional, resultados y sitios externos. |
| Información Legal Gratuita → Noticias/Enlaces del Gobierno | `informacion-legal.html` + submenú | Recursos auténticos del despacho, etapas y enlaces institucionales; sin noticias ficticias. |
| Calculadora de Impuestos | `verificacion.html` | Lista interactiva documental, **no** una calculadora fiscal ni un veredicto legal. |
| Contáctenos | `contacto.html` | Formulario amplio, WhatsApp, dirección y mapa cargado solo tras pulsar un botón. |

La barra lateral de la portada enlaza a requisitos, residencia, reciprocidad, documentación, examen, solvencia, honorarios y verificación. Los enlaces son rutas internas reales, no menús sin destino.

## 3. Marca, datos y decisiones editoriales

**Origen:** carpeta de Drive `naturalizate-pa-main`. No apareció un PDF independiente llamado «brandbook»; las reglas de marca están documentadas en `LEEME-landing.md` y en los activos del sitio. Se aplicaron los logotipos SVG oficiales, retrato aportado, isotipo blanco, favicon y fuentes autoalojadas **Playfair Display + Inter**. La paleta es navy `#0D1B2A`, secundario `#1B3A57` y blancos/grises; no se incorporaron acentos de color ajenos a la marca.

**Datos empleados:** Lic. Alfonso Villarreal; Scotia Plaza, Piso 7, Avenida Federico Boyd, Ciudad de Panamá; WhatsApp `+507 6255-7583`; correo `villarreallawyers@proton.me`. La imagen panorámica **no es una fotografía de la oficina real**: es una ilustración original etiquetada. El mapa del pie es un esquema y enlaza a Google Maps.

**No se trasladaron:** el logotipo, retrato, imagen de oficina, textos, cartera de propiedades, precios, redes sociales ni servicios de Kery Cruz. No se incluyeron traducciones inexistentes de Naturalízate.pa. Se preserva la arquitectura visual, no se suplanta la identidad de la referencia.

## 4. Comportamiento y límites

- **Menú:** navegación real a ocho páginas; submenús con ratón, teclado y móvil.
- **Buscador:** filtra un índice local de páginas/temas; no usa backend ni envía consultas.
- **Formulario del pie y de Contacto:** validan campos y preparan un correo `mailto:` para que quien consulta lo revise y lo envíe en su propia aplicación. **No son una bandeja de entrada, no garantizan la entrega y no suscriben automáticamente a boletines.** La casilla de novedades se agrega al mensaje.
- **Mapa:** el pie muestra un esquema ilustrativo; el mapa interactivo de Contacto solo solicita Google Maps cuando se pulsa «Cargar mapa».
- **Lista de verificación:** cuenta seis puntos de preparación documental en el navegador, sin almacenar datos ni concluir elegibilidad.
- **Compartir:** los artículos internos permiten copiar el enlace o usar la función nativa del dispositivo.

Todas las páginas conservan `noindex, follow` mientras sean borrador. Antes de publicarlas, elegir la URL definitiva y revisar metadatos/canónicas. Los documentos del proyecto discrepan sobre importes y condiciones de la evaluación; por eso no se muestran precios ni se promete gratuidad. El abogado debe revisar textos jurídicos, datos de contacto, fotografía y alcance profesional antes de publicar.

## 5. Comprobaciones

- Ocho páginas generadas con un único encabezado, pie y buscador compartidos.
- Navegación local y anclas verificadas; sin enlaces internos rotos.
- Probadas a 1440, 768 y 390 px: sin desbordamiento horizontal ni errores de JavaScript o recursos locales.
- Auditoría Axe de ocho páginas a 1440 y 390 px: **cero infracciones detectadas**.
- Probados menú, submenús, buscador, lista de verificación, preparación de correo y carga voluntaria del mapa.

**Fuentes examinadas:** [portada de Kery Cruz](https://www.kerycruz.com/es), [tarifas](https://www.kerycruz.com/es/tarifas), [contacto](https://www.kerycruz.com/es/contactenos), [información legal](https://www.kerycruz.com/es/informacion-legal-gratuita), [descargo](https://www.kerycruz.com/es/descargo), [calculadora](https://www.kerycruz.com/es/calculadora-de-impuestos), [guía publicada de Naturalízate.pa](https://naturalizatepa.github.io/naturalizate-pa/guia.html), [Tribunal Electoral](https://www.tribunal-electoral.gob.pa/) y [Servicio Nacional de Migración](https://www.migracion.gob.pa/). Los dos portales institucionales bloquearon consultas automatizadas directas desde este entorno, aunque figuran como portales oficiales en resultados públicos; verificar manualmente sus enlaces antes de publicar.
