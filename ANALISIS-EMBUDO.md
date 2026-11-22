# Análisis del embudo — Naturalízate.pa

**Fecha:** 22 de noviembre de 2026 · **Alcance:** `index.html` completo (11 bloques) y
versión móvil · **Versión:** v5 · **Sustituye** a las cifras de la v4, que describían
otra estructura.

---

## 1. Mapa real de la página (verificado en el DOM)

| # | Bloque | Función en el embudo |
|---|---|---|
| 1 | `#inicio` Hero + tarjeta del abogado | Promesa y ruta |
| 2 | `#situacion` «Vivir en Panamá durante años…» | Reconocimiento del problema |
| 3 | `#enfoque` 5 pilares | Diferenciación |
| 4 | `#proceso` 5 etapas | Confianza procesal |
| 5 | `#honorarios` 2 planes + tabla de 9 filas | Precio ancla |
| 6 | `#diagnostico` Evaluación de $49.99 | Oferta núcleo |
| 7 | `#abogado` Lic. Villarreal | Autoridad |
| 8 | `#casos` 3 testimonios | Prueba social |
| 9 | `#preguntas` 11 preguntas | Objeciones |
| 10 | `#verificar` Formulario de 4 pasos | **Conversión** |
| 11 | `section.final-cta` + pie | Cierre |

El orden sostiene el recorrido: problema → método → proceso → precio → oferta → prueba
→ objeciones → conversión. El formulario está al final, después de que el visitante ya
vio el precio y la comparativa.

---

## 2. El formulario actual

### 2.1 Paso 1 · Cinco preguntas

| Pregunta | Opciones | Qué decide |
|---|---|---|
| País de origen | 40 países + «Otro» | Reciprocidad (1, 2 o 3 años) |
| Años con Cédula E | <3 · 3–5 · >5 · no seguro | Cómputo legal |
| Ausencias | No · <6 meses · >6 meses · no seguro | Arraigo |
| Examen | Sí · dudas · no | Requisito legal |
| Ingreso mensual | <1,000 · 1–3 mil · 3–5 mil · 5–10 mil · >10 mil | Solvencia |

Total: **16 chips y una lista**, más un campo de texto condicional. Cada pregunta
alimenta el veredicto o el mensaje; ninguna se pide «para el expediente».

### 2.2 Paso 2 · Veredicto (sin salidas secas)

| Caso | Mensaje | Reserva |
|---|---|---|
| <3 años con reciprocidad | Aviso de convenio | Sí |
| <3 años sin reciprocidad | No procede todavía | Sí (evaluación) |
| Examen «No» | Requisito legal | Sí (evaluación) |
| Puntaje ≥ 7 | Perfil prioritario · A | Sí |
| Puntaje 4–6 | Revisión recomendada · B | Sí |
| Puntaje ≤ 3 | Revisión recomendada · C | Sí |

**Puntaje máximo 8**: Cédula E >5 años +2; sin ausencias +2 (menores/«no seguro» +1);
examen +2 (dudas +1); ingreso ≥3,000 +2. El ingreso bajo **no resta**: agrega una
advertencia de solvencia y el caso sigue siendo reservable.

Todas las rutas ofrecen dos botones: reservar o corregir respuestas. No hay descarte
seco ni pantalla sin salida.

### 2.3 Paso 3 · Reserva de dos campos

Nombre y WhatsApp. Día, hora y plan se cierran en la conversación. El documento y el
comprobante de $49.99 se piden después, por WhatsApp, junto con el pago.

### 2.4 Paso 4 · Confirmación

Resumen de 8 filas + consentimiento + apertura de WhatsApp con el mensaje completo
(incluye perfil interno y UTM). Enlace de respaldo si el navegador bloquea la ventana.

---

## 3. Qué cambió en la v5

| Punto | Antes | Ahora | Por qué |
|---|---|---|---|
| Oferta | Repetida en hero, diagnóstico y formulario | Una sola sección de oferta (`#diagnostico`) | El precio aparecía 18 veces en el HTML; hoy 15 y solo 5 en texto visible |
| Hero | H1 en pregunta + 3 CTAs | H1 afirmativo + 1 CTA + enlace secundario | La promesa se entiende sin conocer la ley |
| Reserva | 15 campos y 3 preferencias | 2 campos | El punto de máxima intención no admite formularios largos |
| Resumen | 15 filas | 8 filas | Solo lo que el despacho necesita para responder |
| Navegación móvil | Sin menú | Hamburguesa con 6 anclas y CTA | La página tiene 11 bloques y antes solo se recorría con scroll |
| Comparativa | 5 bullets por plan | Tabla de 9 filas | La diferencia entre planes se decide, no se intuye |
| Accesibilidad | Sin `main`, errores sin anuncio | `main`, `role="alert"`, `aria-live`, `progressbar`, foco blanco | Lectores de pantalla y teclado |
| Rendimiento | Fuentes desde Google Fonts | 3 woff2 en base64 | 0 peticiones externas; la página abre sin conexión |
| Anclas | `content-visibility: auto` | Retirado | Excluía secciones del árbol de accesibilidad y desplazaba el foco |

**Contrapartida asumida:** el filtro pasó de 3 a 5 preguntas (se sumaron ausencias y
examen) porque ambas cambian el veredicto. La reducción real está en la reserva: de 15
campos a 2: el total público es de 7 campos (5 preguntas + 2 datos de contacto) más el
consentimiento.

---

## 4. Medición incluida

El sitio emite dos eventos a `window.dataLayer`:

| Evento | Cuándo | Datos |
|---|---|---|
| `filtro_resultado` | Al calcular el veredicto | `resultado` (`reciprocidad`, `no_procede_computo`, `no_procede_examen`, `calificado`), `pais` o `perfil` |
| `reserva_confirmada` | Al enviar a WhatsApp | `perfil` |

**Puente a GA4 listo, sin activar.** Los eventos se acumulan en `window.dataLayer` y
`track()` los reenvía a GA4 si `GA4_ID` tiene un valor. Mientras esté vacío no se carga
`gtag.js` ni se hace ninguna petición: la página sigue siendo offline-first. Para
leerlos en GA4 hay que registrar `resultado`, `perfil` y `pais` como dimensiones
personalizadas. La caída del embudo se mide con esos dos eventos: cuántos llegan al
veredicto y cuántos confirman.

---

## 5. Verificación (22 nov 2026)

Método: Chrome headless, medición con iframe a 360 px (la ventana headless no baja de
500 px) y ventana directa a 1440 px.

| Comprobación | Resultado |
|---|---|
| Desborde horizontal | 0 a 360 px y a 1440 px; ningún elemento fuera del viewport |
| Anclas | `#honorarios`, `#preguntas` y `#verificar` aterrizan a **92 px** en ambos anchos |
| Foco | `:focus-visible` con contorno **blanco de 2 px** en hero y CTA del menú |
| Menú móvil | Abre 0→360 px, `aria-expanded=true`, cierra al pulsar un enlace |
| Recorrido del formulario | Paso 1 → 2 → 3 → 4; reserva con **2 campos**; resumen con **8 filas**; `aria-valuenow=4` |
| Rangos de ingreso | 5 opciones; «menos de $1,000» da *Revisión B* con reserva disponible; «más de $10,000» da *Prioritario A* |
| Tipografías | Inter y Playfair activas con la red bloqueada; **0 peticiones** |
| Script | `node --check` sin errores |
| Analítica | `GA4_ID` vacío: 0 peticiones. Con un ID de prueba, `filtro_resultado` y `reserva_confirmada` llegan a `dataLayer` con su nombre de evento |
| Peso | 263.451 bytes; 2.484 palabras visibles |

**Lo que esta verificación no cubre:** no hay batería jsdom en esta copia, ni pruebas
de PDF, ni prueba en Safari, Firefox o dispositivo real. Las cifras de «68/68» de la v4
correspondían a otra compilación y no aplican aquí.

---

## 6. Fricción que queda

1. **Pago fuera de la página.** El visitante confirma, recibe el enlace de pago por
   WhatsApp y vuelve con el comprobante. Es un paso manual que se puede automatizar.
2. **Sin analítica conectada.** `dataLayer` no se envía a ningún destino.
3. **Sin borrador.** Recargar o cerrar el navegador pierde las respuestas.
4. **Precio público antes del veredicto.** Decisión del despacho: filtra curiosos, pero
   también puede frenar a quien aún no sabe si su caso aplica.
5. **ITBMS condicional.** La página dice que se añade «si el servicio está gravado»;
   falta confirmar el criterio para poder afirmarlo o excluirlo.
6. **Reserva y herramienta interna no están conectadas.** Los datos llegan por WhatsApp;
   nadie los vuelca automáticamente a `formulario-interno.html`.

---

## 7. Lo que no se tocó, a propósito

- **El orden de las secciones.** El recorrido actual (problema → método → proceso →
  precio → oferta → autoridad → prueba → FAQ → formulario) funciona y no se reordenó.
- **La pregunta de ingresos.** Podría moverse a WhatsApp, pero ahí se pierde el aviso
  de solvencia antes de hablar con nadie.
- **Los precios publicados.** $3,800 y $5,500 siguen visibles: son el ancla de la
  comparativa y sostienen la credibilidad del «honorarios fijos por escrito».
- **La ausencia de promesas de resultado.** Se mantiene el aviso legal y el criterio de
  no aceptar expedientes que no cumplan la ley.
