# Page news · Naturalízate.pa

Segunda versión del sitio, adaptada a partir de un análisis visual y funcional de **https://www.kerycruz.com/es**. Reproduce su arquitectura (portada editorial, menú con páginas internas, barra lateral, pie de tres columnas y formularios) con **la identidad y los datos de Naturalízate.pa**. El análisis y las equivalencias se documentan en [`ANALISIS-REFERENCIA.md`](ANALISIS-REFERENCIA.md).

## Ver la página

Abra `index.html` o, preferiblemente, inicie un servidor estático en esta carpeta:

```sh
python3 -m http.server 4173
```

Visite `http://localhost:4173/`. Todos los HTML, estilos, scripts, logotipos y fuentes están en esta carpeta; no hace falta instalar dependencias ni compilar para publicar.

## Páginas incluidas

| Archivo | Sección |
|---|---|
| `index.html` | Portada con imagen, búsqueda, presentación, retrato y barra lateral. |
| `servicios.html` | Áreas de práctica, evaluación, expediente y representación. |
| `vias.html` | Vías que deben evaluarse según cada caso. |
| `honorarios.html` | Tabla de alcance y política de propuestas personalizadas. |
| `aviso-legal.html` | Aviso legal y límites de la información. |
| `informacion-legal.html` | Artículos, etapas, guía y enlaces oficiales. |
| `verificacion.html` | Lista documental orientativa de seis puntos. |
| `contacto.html` | Formulario de contacto y mapa bajo demanda. |

`site_builder.py` genera esos ocho HTML desde `pages_content.py` y el encabezado/pie compartidos. Si edita los archivos de origen, regenere las páginas con `python3 -B site_builder.py`. `styles.css` controla el diseño y `app.js` las interacciones. `assets/` contiene fuentes, logos, favicon, retrato e imagen ilustrativa de oficina.

## Funciones y límites reales

- El buscador indexa las secciones locales. No realiza búsquedas en internet ni transmite datos.
- Los formularios **no tienen backend**: validan los campos y abren un borrador de correo en la aplicación del visitante. El visitante confirma el envío. Marcar la casilla de novedades solo deja constancia en ese borrador; **no crea una suscripción automática**.
- La lista de verificación cuenta elementos, no determina elegibilidad ni almacena respuestas. El enlace de WhatsApp abre un mensaje genérico que se puede editar antes de enviarlo.
- El mapa del pie es un **esquema ilustrativo**; en la página de Contacto se carga Google Maps únicamente después de pulsar el botón correspondiente.
- La fotografía panorámica es una **ilustración original** y no representa la oficina real. El resto de activos visuales y los datos del despacho proceden de `naturalizate-pa-main` en Drive.

## Antes de publicar

1. El borrador usa `<meta name="robots" content="noindex, follow">`. Al decidir la URL definitiva, cambiarlo a `index, follow`, agregar URL canónica y ajustar `og:url`/`og:image` y cualquier mapa del sitio que se utilice.
2. Confirmar teléfono `+507 6255-7583`, correo `villarreallawyers@proton.me`, dirección de Scotia Plaza, uso del retrato y los textos legales con el despacho.
3. Los documentos del proyecto discrepan sobre importes y condiciones de la evaluación. Esta versión **no** publica precios ni afirma que la evaluación sea gratuita; aclarar las condiciones vigentes antes de anunciar tarifas.
4. Configurar un servicio real de recepción de mensajes/boletines solo si se desea sustituir el flujo `mailto:`. No presentar este borrador como formulario que registra consultas automáticamente.
5. Comprobar manualmente los enlaces institucionales; ambos portales bloquearon las solicitudes automatizadas de este entorno.

La versión anterior, que gustó en la primera iteración, se conserva aparte como `page-news-v1.zip`. Esta revisión no modifica el proyecto original de Drive.
