"""Editorial content for the Naturalízate.pa pages.

Portado del rediseño editorial («page news») e integrado con la oferta
comercial del despacho: Orientación Inicial Gratuita y Auditoría Jurídica
de Caso por US$49.
"""

from urllib.parse import quote

GUIDE = "guia.html"
WA_NUMBER = "50762557583"
WA_WELCOME = """¡Hola! 👋 Bienvenido/a a Naturalízate.pa 🇵🇦
Te acompañamos en tu proceso de naturalización panameña con atención jurídica personalizada ⚖️✨

✅ Primer contacto gratuito y sin compromiso.

Para comenzar, cuéntanos:
🌎 ¿Cuál es tu nacionalidad?
📅 ¿Desde qué año tienes residencia permanente en Panamá?"""


def wa_link(message=WA_WELCOME):
    return f"https://wa.me/{WA_NUMBER}?text={quote(message)}"


WHATSAPP = wa_link()
AUDIT_WHATSAPP = wa_link("Hola, quisiera solicitar la Auditoría Jurídica de Caso (US$49) con el Lic. Alfonso Villarreal.")

RELATED = [
    ("index.html#auditoria", "Auditoría Jurídica · US$49"),
    ("index.html#calificacion", "Evaluar mi situación"),
    ("informacion-legal.html#proceso", "Etapas del proceso de naturalización"),
    ("informacion-legal.html#requisitos", "Requisitos generales"),
    ("vias.html#residencia", "Cédula E y residencia"),
    ("vias.html#reciprocidad", "Convenios de reciprocidad"),
    ("informacion-legal.html#documentos", "Documentos del expediente"),
    ("informacion-legal.html#examen", "Examen de naturalización"),
    ("honorarios.html", "Honorarios del despacho"),
    ("verificacion.html", "Lista de verificación"),
]

FAQ = [
    ("¿Cuánto tiempo tarda el proceso de naturalización?",
     "La duración depende de la vía aplicable, la integridad documental del expediente y los tiempos administrativos de las autoridades competentes (Servicio Nacional de Migración, Tribunal Electoral, Gobernación y Órgano Ejecutivo). Por rigor profesional no garantizamos plazos fijos; durante la auditoría jurídica le orientamos sobre las etapas y tiempos referenciales según su situación."),
    ("¿Tener cédula E significa que puedo naturalizarme?",
     "No por sí sola. La cédula E acredita su condición de residente permanente, pero para solicitar la naturalización deben verificarse además el tiempo consecutivo de residencia exigido por el artículo 10 de la Constitución Política, el historial de ausencias, los antecedentes documentales y el cumplimiento del resto de requisitos aplicables."),
    ("¿Debo estar físicamente en Panamá durante todo el procedimiento?",
     "No necesariamente durante todo el trámite, pero existen diligencias presenciales obligatorias como entrevistas, verificaciones personales, el examen de conocimientos cuando corresponda y el acto de juramentación. En la auditoría jurídica revisamos su situación actual y sus desplazamientos para orientarle adecuadamente."),
    ("¿Qué ocurre si he salido de Panamá?",
     "Las salidas del territorio panameño no descartan automáticamente una solicitud, pero deben evaluarse según su duración, frecuencia, fechas y categoría migratoria. En la Auditoría Jurídica de Caso analizamos sus movimientos migratorios para identificar si existen riesgos que deban atenderse antes de presentar."),
    ("¿Puedo solicitar la naturalización si tengo nacionalidad de otro país?",
     "El artículo 10 de la Constitución Política de Panamá contempla la declaración de voluntad y renuncia expresa conforme al marco constitucional panameño, mientras que los efectos jurídicos respecto de su nacionalidad anterior dependen también de la legislación de su país de origen. En la auditoría explicamos las implicaciones concretas de su caso y el alcance del artículo 13 constitucional."),
    ("¿Existe una vía especial por matrimonio con un ciudadano panameño?",
     "Sí. El artículo 10, ordinal 2.º de la Constitución Política contempla la posibilidad de solicitar la naturalización con tres (3) años consecutivos de residencia en Panamá para extranjeros con cónyuge de nacionalidad panameña (así como para quienes tengan hijos nacidos en Panamá de padre o madre panameños), sujeto a la verificación de los demás requisitos constitucionales y legales."),
    ("¿Qué documentos debo presentar?",
     "La lista depende de la vía aplicable, su nacionalidad, estado civil, historial migratorio y situación económica (estatus migratorio, cédula E, antecedentes, pruebas de solvencia y documentos de respaldo según el caso). Durante la Auditoría Jurídica revisamos la documentación pertinente que usted facilite y le indicamos qué deberá preparar."),
    ("¿Puedo iniciar una evaluación desde el extranjero?",
     "Sí. Tanto la orientación inicial gratuita como la Auditoría Jurídica de Caso (US$49) pueden realizarse a distancia, ya que la auditoría se lleva a cabo mediante llamada telefónica con el Lic. Alfonso Villarreal y revisión previa de la documentación pertinente que usted comparta."),
    ("¿Cuánto cuesta la auditoría jurídica?",
     "La Auditoría Jurídica de Caso tiene un honorario único de <strong>US$49</strong>. Se realiza mediante llamada telefónica con el Lic. Alfonso Villarreal e incluye el análisis de antecedentes, revisión de documentación pertinente, evaluación de su situación migratoria, identificación de riesgos y determinación de posibles alternativas jurídicas."),
    ("¿Los US$49 incluyen todo el trámite?",
     "No. La Auditoría Jurídica de Caso es un servicio profesional independiente de evaluación. No incluye automáticamente representación legal, elaboración o presentación de solicitudes, recursos, procesos judiciales ni gestiones administrativas posteriores. Esas actuaciones se cotizan por separado mediante una propuesta independiente."),
    ("¿Qué sucede si mi caso no es viable?",
     "Se lo indicamos con total transparencia y sustento jurídico durante la auditoría, sin proponerle un trámite improcedente. Cuando corresponda, le explicamos qué aspectos convendría regularizar o qué alternativas migratorias o legales podrían evaluarse a futuro."),
    ("¿Cómo se contratan los servicios jurídicos posteriores?",
     "Si tras la auditoría se confirma una alternativa jurídicamente viable, presentamos una propuesta formal de honorarios por escrito en la que se detallan el alcance de los servicios, las condiciones, los costos y las responsabilidades de cada parte. Usted decide libremente si desea contratar."),
]

NATIONALITIES = [
    "Alemania", "Argentina", "Bolivia", "Brasil", "Canadá", "Chile", "China",
    "Colombia", "Costa Rica", "Cuba", "Ecuador", "El Salvador", "España",
    "Estados Unidos", "Francia", "Guatemala", "Haití", "Honduras", "India",
    "Italia", "México", "Nicaragua", "Paraguay", "Perú", "Portugal",
    "Reino Unido", "República Dominicana", "Uruguay", "Venezuela",
]


def related(items=RELATED, title="Información de interés"):
    links = "\n".join(f'<li><a href="{href}">{text}</a></li>' for href, text in items)
    return f'<aside class="related-sidebar" aria-label="{title}"><h2>{title}</h2><ul>{links}</ul></aside>'


def columns(article, links=RELATED, title="Información de interés", extra="", share=True):
    share_bar = '<div class="share-row"><span>Compartir</span><button type="button" data-share>Compartir esta página <span aria-hidden="true">↗</span></button><small data-share-status role="status"></small></div>' if share else ""
    return f'<div class="content-columns {extra}"><article class="article-main">{article}{share_bar}</article>{related(links, title)}</div>'


HOME = '''<h1>Su camino hacia la nacionalidad panameña comienza con una evaluación jurídica seria.</h1>
      <div class="article-text home-article">
        <figure class="portrait"><img src="assets/foto-alfonso-villarreal.jpg" alt="Retrato del Lic. Alfonso Villarreal" width="480" height="480" /><figcaption>Lic. Alfonso Villarreal</figcaption></figure>
        <p>Gracias por su interés en nuestro sitio web y en nuestros servicios.</p>
        <p>Naturalízate.pa es una oficina legal en Ciudad de Panamá enfocada en los procesos de nacionalidad panameña por naturalización. El despacho está dirigido por el <strong>Lic. Alfonso Villarreal, abogado idóneo en Panamá</strong>, y atiende cada caso de forma personalizada.</p>
        <p>Sabemos que una solicitud de naturalización no comienza con llenar un formulario. Primero es necesario entender la historia migratoria, las fechas de residencia, la documentación disponible y la situación particular de quien desea iniciar el trámite. Por ello, nuestra labor comienza con una revisión de viabilidad y una explicación clara de los próximos pasos.</p>
        <p>Hay dos formas de comenzar: una <a href="#servicios-inicio">orientación inicial gratuita</a> para clasificar su situación, o una <a href="#auditoria">Auditoría Jurídica de Caso por US$49</a> con el Lic. Alfonso Villarreal. En ambos casos explicamos el alcance antes de cualquier contratación.</p>
        <p>Cuando corresponde avanzar, acompañamos la preparación del expediente, la presentación mediante abogado y el seguimiento de las etapas ante las autoridades panameñas. También orientamos sobre la documentación y el examen de naturalización que puedan corresponder al caso.</p>
        <p>Nuestro objetivo es que cada persona tome decisiones informadas. No prometemos aprobaciones ni plazos que dependen del Estado; explicamos el alcance del trabajo, los honorarios y los posibles obstáculos antes de iniciar una representación.</p>
        <p class="signature"><strong>Lic. Alfonso Villarreal</strong><br />Naturalízate.pa</p>
      </div>'''

DOORS = '''<section class="home-band alt" id="servicios-inicio">
  <div class="band-head"><span class="eyebrow">Dos puertas de entrada claras</span><h2>Orientación inicial gratuita o <em>Auditoría Jurídica de Caso</em></h2><p>Sepa exactamente qué recibe sin costo y qué comprende la evaluación jurídica profesional de US$49.</p></div>
  <div class="doors-grid">
    <article class="door-card">
      <span class="door-badge">Puerta A · Sin costo</span>
      <h3>Orientación Inicial Gratuita</h3>
      <p class="door-price">Gratuita <small>Contacto breve para clasificar su situación</small></p>
      <p><strong>Objetivo:</strong> conocer brevemente su situación y determinar si corresponde avanzar a una evaluación jurídica.</p>
      <p class="door-subhead">Incluye</p>
      <ul class="check-list"><li>Identificación de la nacionalidad.</li><li>Conocimiento general de su situación migratoria.</li><li>Identificación de su necesidad.</li><li>Preguntas preliminares para clasificar el caso.</li><li>Orientación sobre el siguiente paso.</li></ul>
      <p class="door-subhead">No incluye</p>
      <ul class="check-list muted"><li>Dictamen jurídico ni análisis exhaustivo.</li><li>Revisión integral del expediente.</li><li>Determinación definitiva de elegibilidad.</li><li>Elaboración de documentos legales.</li></ul>
      <a class="button-primary door-cta" href="#calificacion">Evaluar mi situación <span aria-hidden="true">→</span></a>
    </article>
    <article class="door-card featured">
      <span class="door-badge">Puerta B · Servicio profesional</span>
      <h3>Auditoría Jurídica de Caso</h3>
      <p class="door-price">US$49 <small>Llamada telefónica con el Lic. Alfonso Villarreal</small></p>
      <p>Evaluación profesional individualizada para identificar alternativas jurídicas, riesgos y requisitos antes de iniciar un trámite.</p>
      <p class="door-subhead">Incluye</p>
      <ul class="check-list"><li>Análisis de los antecedentes del caso.</li><li>Revisión de la documentación pertinente.</li><li>Evaluación de la situación migratoria.</li><li>Identificación de riesgos y posibles obstáculos.</li><li>Determinación de alternativas jurídicas.</li><li>Explicación de requisitos y siguientes pasos.</li></ul>
      <p class="door-note"><strong>Aclaración:</strong> no incluye automáticamente representación legal, presentación de solicitudes ni gestiones posteriores. Esas actuaciones se cotizan mediante una propuesta independiente.</p>
      <a class="button-primary door-cta" href="#auditoria">Solicitar mi Auditoría Jurídica <span aria-hidden="true">→</span></a>
    </article>
  </div>
</section>'''

VIAS_HOME = '''<section class="home-band" id="quien-puede">
  <div class="band-head"><span class="eyebrow">Marco constitucional y legal</span><h2>¿Quién puede solicitar la <em>nacionalidad panameña</em>?</h2><p>El artículo 10 de la Constitución Política contempla las vías principales para solicitar la Carta de Naturaleza, sujetas a la ley y reglamentación vigentes.</p></div>
  <div class="vias-grid">
    <article class="via-card"><span class="via-num">Art. 10, ordinal 1.º</span><h3>Naturalización por residencia</h3><p>Extranjeros mayores de edad con <strong>cinco (5) años consecutivos de residencia</strong> que declaren su voluntad de naturalizarse, renuncien expresamente a su nacionalidad de origen y comprueben el dominio del español y conocimientos básicos de geografía, historia y organización política panameñas.</p></article>
    <article class="via-card"><span class="via-num">Art. 10, ordinal 2.º</span><h3>Cónyuge o hijos panameños</h3><p>Extranjeros con <strong>tres (3) años consecutivos de residencia</strong> que tengan <strong>cónyuge de nacionalidad panameña</strong> o <strong>hijos nacidos en Panamá de padre o madre panameños</strong>, cumpliendo la declaración y comprobaciones exigidas.</p></article>
    <article class="via-card"><span class="via-num">Art. 10, ordinal 3.º</span><h3>Reciprocidad (España y Latinoamérica)</h3><p>Nacionales <strong>por nacimiento de España o de un Estado latinoamericano</strong> que llenen los mismos requisitos que en su país de origen se exigen a los panameños. Su aplicación concreta debe comprobarse jurídicamente caso por caso.</p></article>
  </div>
  <div class="legal-precision"><strong>Precisión constitucional:</strong> el artículo 10 establece los supuestos de naturalización; el artículo 12 dispone su reglamentación y las causales por las cuales el Estado puede negar una solicitud; el artículo 13 regula la pérdida de la nacionalidad derivada y la suspensión de ciudadanía; y el artículo 14 se refiere a la regulación legal de la inmigración. Cada situación debe verificarse frente a la legislación y criterios administrativos vigentes.</div>
  <div class="inline-actions"><a class="button-primary" href="#calificacion">Evaluar mi situación <span aria-hidden="true">→</span></a><a class="text-action" href="vias.html">Ver vías en detalle ↗</a></div>
</section>'''

RISKS = '''<section class="home-band alt" id="riesgos">
  <div class="band-head"><span class="eyebrow">Prevención de errores</span><h2>¿Por qué revisar su caso <em>antes de presentar una solicitud</em>?</h2><p>Un expediente presentado sin evaluación jurídica previa puede exponerse a requerimientos evitables, retrasos prolongados o una negativa por aspectos que debieron verificarse antes.</p></div>
  <ol class="risk-list">
    <li><strong>Una cédula E antigua no garantiza por sí sola que se cumplan todos los requisitos.</strong><p>La cédula E acredita identidad de residente permanente, pero no sustituye la verificación integral de residencia consecutiva, arraigo, conducta, solvencia y cumplimiento documental.</p></li>
    <li><strong>Los cambios de categoría migratoria pueden ser relevantes.</strong><p>El historial de permisos provisionales, cambios de subcategoría o resoluciones migratorias incide en la fecha desde la cual corresponde analizar el cómputo de residencia.</p></li>
    <li><strong>Las ausencias del país deben analizarse según las circunstancias del caso.</strong><p>Las entradas y salidas del territorio panameño durante el período de residencia deben revisarse frente al historial migratorio para evaluar posibles impactos antes de presentar.</p></li>
    <li><strong>La nacionalidad de origen puede determinar una vía especial.</strong><p>Dependiendo de su país de nacimiento y de la normativa vigente, podría requerirse verificar la reciprocidad del artículo 10, ordinal 3.º u otra vía constitucional.</p></li>
    <li><strong>Los antecedentes documentales pueden revelar obstáculos previos.</strong><p>Discrepancias en registros civiles, nombres, fechas, pruebas de solvencia o estatus migratorio deben identificarse y atenderse antes de comprometer tiempo y honorarios en un expediente formal.</p></li>
  </ol>
  <div class="inline-actions"><a class="button-primary" href="#auditoria">Solicitar mi Auditoría Jurídica <span aria-hidden="true">→</span></a><a class="text-action" href="#calificacion">Evaluar mi situación ↗</a></div>
</section>'''

AUDIT = '''<section class="home-band audit-band" id="auditoria">
  <div class="band-head"><span class="eyebrow on-dark">Servicio profesional principal</span><h2>Auditoría Jurídica de Caso</h2><p>Una evaluación profesional antes de iniciar su trámite de naturalización.</p></div>
  <div class="audit-grid">
    <div>
      <h3>¿Qué incluye?</h3>
      <ul class="check-list on-dark"><li>Análisis de su situación migratoria.</li><li>Revisión de los antecedentes del caso.</li><li>Revisión de la documentación pertinente.</li><li>Identificación de riesgos y obstáculos.</li><li>Evaluación de posibles alternativas jurídicas.</li><li>Orientación sobre los siguientes pasos.</li></ul>
      <blockquote class="audit-quote">«Primero conocemos su situación. Después determinamos qué servicio necesita.»</blockquote>
    </div>
    <div class="audit-price-card">
      <span class="ap-label">Honorario único</span>
      <p class="ap-price">US$49</p>
      <p class="ap-mode"><strong>Modalidad:</strong> llamada telefónica con el Lic. Alfonso Villarreal.</p>
      <a class="button-primary ap-button" href="''' + AUDIT_WHATSAPP + '''" target="_blank" rel="noopener noreferrer">Solicitar mi Auditoría <span aria-hidden="true">↗</span></a>
      <p class="ap-alt">¿Prefiere compartir primero sus datos generales? <a href="#calificacion">Complete el formulario breve</a>.</p>
    </div>
  </div>
  <p class="audit-disclaimer"><strong>Aclaración:</strong> la auditoría es un servicio profesional independiente. No incluye automáticamente la representación ni la ejecución de trámites posteriores.</p>
</section>'''

STEPS = '''<section class="home-band" id="como-trabajamos">
  <div class="band-head"><span class="eyebrow">Recorrido claro</span><h2>¿Cómo trabajamos?</h2><p>Cinco pasos ordenados desde su primer contacto hasta una eventual contratación.</p></div>
  <ol class="process-steps">
    <li><span>01</span><div><strong>Nos contacta</strong><p>El interesado nos explica brevemente su nacionalidad, situación migratoria y necesidad.</p></div></li>
    <li><span>02</span><div><strong>Calificamos su caso</strong><p>Identificamos qué información y documentos necesitamos para comprender su situación.</p></div></li>
    <li><span>03</span><div><strong>Realizamos la auditoría · US$49</strong><p>El Lic. Alfonso Villarreal analiza el caso mediante una llamada telefónica y revisa la documentación pertinente.</p></div></li>
    <li><span>04</span><div><strong>Determinamos las alternativas</strong><p>Explicamos los riesgos, requisitos y posibles vías jurídicas.</p></div></li>
    <li><span>05</span><div><strong>Presentamos una propuesta</strong><p>Cuando corresponda, presentamos una propuesta de honorarios y alcance para la representación posterior.</p></div></li>
  </ol>
  <p class="legal-small">No iniciamos trámites ni presentamos solicitudes sin haber revisado antes la documentación y las circunstancias reales de su caso.</p>
</section>'''

PROFILE = '''<section class="home-band alt" id="abogado">
  <div class="profile-grid">
    <figure class="profile-photo"><img src="assets/foto-alfonso-villarreal.jpg" alt="Lic. Alfonso Villarreal, abogado responsable de Naturalízate.pa" width="300" height="300" loading="lazy" decoding="async" /><figcaption>Lic. Alfonso Villarreal</figcaption></figure>
    <div>
      <span class="eyebrow">Quién analiza su caso</span>
      <h2>Rigor jurídico, transparencia y acompañamiento responsable.</h2>
      <blockquote class="audit-quote dark">«Primero evaluamos su caso. Después determinamos si conviene iniciar el proceso.»</blockquote>
      <div class="pillars">
        <div><h3>Conocimiento</h3><p>Su caso es analizado por un abogado que conoce el procedimiento de naturalización y sus implicaciones jurídicas.</p></div>
        <div><h3>Transparencia</h3><p>No se prometen resultados ni aprobaciones sin verificar primero requisitos, antecedentes y documentos.</p></div>
        <div><h3>Acompañamiento</h3><p>Usted conoce cada paso y el alcance de cada servicio antes de contratar.</p></div>
      </div>
      <p class="profile-addr">Scotia Plaza, Piso 7 · Av. Federico Boyd · Ciudad de Panamá, República de Panamá</p>
      <div class="inline-actions"><a class="button-primary" href="#auditoria">Solicitar mi Auditoría Jurídica <span aria-hidden="true">→</span></a><a class="text-action" href="servicios.html">Áreas de práctica ↗</a></div>
    </div>
  </div>
</section>'''

CONTRACT = '''<section class="home-band alt" id="contratacion">
  <div class="band-head"><span class="eyebrow">Representación posterior</span><h2>Si su caso es viable, podemos acompañarlo durante el proceso.</h2><p>Cuando la Auditoría Jurídica identifica una alternativa jurídicamente viable, estos son los servicios que pueden prestarse según el alcance contratado:</p></div>
  <ul class="check-list services-columns"><li><strong>Preparación documental:</strong> organización y verificación de los soportes requeridos para el expediente.</li><li><strong>Solicitudes y poderes:</strong> redacción técnica de poderes, memoriales y documentación legal.</li><li><strong>Presentación mediante abogado:</strong> ingreso formal de la solicitud ante la autoridad competente.</li><li><strong>Seguimiento del expediente:</strong> control de actuaciones e informes claros del estado del trámite.</li><li><strong>Atención de requerimientos:</strong> respuesta jurídica ante observaciones institucionales.</li><li><strong>Orientación para el examen:</strong> preparación estructurada cuando aplique.</li><li><strong>Acompañamiento en las etapas:</strong> asistencia durante las fases comprendidas en el acuerdo.</li></ul>
  <div class="legal-precision"><strong>Condiciones de contratación:</strong> cada servicio está sujeto a una <strong>propuesta de honorarios independiente por escrito</strong>, con alcance, condiciones y responsabilidades definidos. Naturalízate.pa no promete resultados ni la aprobación de solicitudes.</div>
  <div class="inline-actions"><a class="button-primary" href="#auditoria">Solicitar mi Auditoría Jurídica <span aria-hidden="true">→</span></a><a class="text-action" href="honorarios.html">Ver honorarios ↗</a></div>
</section>'''


def faq_section():
    items = []
    for index, (question, answer) in enumerate(FAQ, start=1):
        items.append(
            f'<div class="faq-item">'
            f'<h3><button type="button" class="faq-q" aria-expanded="false" id="faq-q-{index}" aria-controls="faq-a-{index}">'
            f'<span class="faq-num">{index}.</span> {question} <span class="faq-mark" aria-hidden="true">+</span></button></h3>'
            f'<div class="faq-a" id="faq-a-{index}" role="region" aria-labelledby="faq-q-{index}" hidden><p>{answer}</p></div>'
            f'</div>'
        )
    return f'''<section class="home-band" id="preguntas">
  <div class="band-head"><span class="eyebrow">Preguntas frecuentes</span><h2>Dudas clave sobre la <em>naturalización y la auditoría jurídica</em></h2><p>Respuestas breves, claras y jurídicamente verificadas sobre el procedimiento y nuestro servicio.</p></div>
  <div class="faq-list">{"".join(items)}</div>
</section>'''


def nationality_options():
    return "\n".join(f'<option value="{name}">{name}</option>' for name in NATIONALITIES)


def qualification_section():
    years = "\n".join(f'<option value="{year}">{year}</option>' for year in range(2010, 2027))
    return f'''<section class="home-band alt" id="calificacion">
  <div class="band-head"><span class="eyebrow">Orientación inicial gratuita · Calificación de caso</span><h2>Evalúe preliminarmente <em>su situación</em></h2><p>Complete estas 8 preguntas breves para ayudarnos a clasificar su caso e identificar qué aspectos deben revisarse antes de recomendarle un procedimiento.</p></div>
  <form class="qual-form" data-qual-form novalidate>
    <div class="qual-progress"><span id="qual-count">0 de 8 respondidas</span><div class="progress-track" role="progressbar" aria-label="Preguntas completadas" aria-valuemin="0" aria-valuemax="8" aria-valuenow="0"><span id="qual-progress"></span></div></div>
    <div class="qual-grid">
      <p class="qual-field"><label for="q1"><span>1.</span> Nacionalidad</label><select id="q1" name="Nacionalidad" data-qual-field required><option value="">Seleccione su nacionalidad</option>{nationality_options()}<option value="Otra">Otra nacionalidad</option></select></p>
      <p class="qual-field"><label for="q2"><span>2.</span> ¿Desde qué año reside en Panamá?</label><select id="q2" name="Año de residencia" data-qual-field required><option value="">Seleccione el año aproximado</option><option value="Antes de 2010">Antes de 2010</option><option value="2010 - 2015">Entre 2010 y 2015</option><option value="2016 - 2018">Entre 2016 y 2018</option>{years}<option value="Aún no resido en Panamá">Aún no resido en Panamá</option></select></p>
      <p class="qual-field"><label for="q3"><span>3.</span> Tipo de residencia actual</label><select id="q3" name="Residencia actual" data-qual-field required><option value="">Seleccione una opción</option><option value="Residencia permanente">Residencia permanente</option><option value="Residencia provisional">Residencia provisional</option><option value="Cédula E">Cédula E</option><option value="Estatus migratorio irregular">Estatus migratorio irregular</option><option value="No resido en Panamá">No resido en Panamá</option></select></p>
      <p class="qual-field"><label for="q4"><span>4.</span> ¿Tiene cédula E?</label><select id="q4" name="Cédula E" data-qual-field required><option value="">Seleccione una opción</option><option value="Sí">Sí</option><option value="No">No</option><option value="En trámite">En trámite</option></select></p>
      <p class="qual-field"><label for="q5"><span>5.</span> ¿Desde cuándo tiene cédula E?</label><select id="q5" name="Fecha de cédula E" data-qual-field required><option value="">Seleccione una opción</option><option value="Menos de 3 años">Menos de 3 años</option><option value="Entre 3 y 5 años">Entre 3 y 5 años</option><option value="Más de 5 años">Más de 5 años</option><option value="No tengo cédula E">No tengo cédula E</option></select></p>
      <p class="qual-field"><label for="q6"><span>6.</span> ¿Ha salido de Panamá durante su residencia?</label><select id="q6" name="Ausencias" data-qual-field required><option value="">Seleccione una opción</option><option value="No he salido">No he salido</option><option value="Salidas breves y esporádicas">Salidas breves y esporádicas</option><option value="Salidas prolongadas o frecuentes">Salidas prolongadas o frecuentes</option></select></p>
      <p class="qual-field"><label for="q7"><span>7.</span> ¿Se encuentra actualmente en Panamá?</label><select id="q7" name="Ubicación actual" data-qual-field required><option value="">Seleccione una opción</option><option value="Sí, en Panamá">Sí, en Panamá</option><option value="No, estoy en el extranjero">No, estoy en el extranjero</option></select></p>
      <p class="qual-field"><label for="q8"><span>8.</span> ¿Tiene vínculo familiar con ciudadanos panameños?</label><select id="q8" name="Vínculo familiar" data-qual-field required><option value="">Seleccione una opción</option><option value="Cónyuge panameño(a)">Cónyuge panameño(a)</option><option value="Hijos nacidos en Panamá">Hijos nacidos en Panamá</option><option value="Otro familiar panameño">Otro familiar panameño</option><option value="Sin vínculo familiar">Sin vínculo familiar</option></select></p>
    </div>
    <div class="qual-actions"><button class="form-submit" type="submit">Enviar mi información por WhatsApp <span aria-hidden="true">↗</span></button><a class="text-action" href="#auditoria">Prefiero la auditoría de US$49 ↗</a></div>
    <p class="form-note">Gracias por compartir su información. Sus respuestas nos permitirán conocer mejor su situación y determinar qué aspectos deben revisarse antes de recomendarle un procedimiento. Este formulario no emite un dictamen ni determina elegibilidad; abre un mensaje de WhatsApp que usted revisa y envía.</p>
    <p class="form-note qual-status" data-qual-status role="status"></p>
  </form>
</section>'''


CLOSING = '''<section class="home-band closing-band" id="contacto">
  <div>
    <span class="eyebrow on-dark">Siguiente paso</span>
    <h2>Conversemos sobre su caso.</h2>
    <p>Escríbanos por WhatsApp o utilice el formulario. Le indicaremos cómo continuar con la evaluación antes de cualquier contratación.</p>
  </div>
  <div class="inline-actions"><a class="button-primary light" href="''' + WHATSAPP + '''" target="_blank" rel="noopener noreferrer">WhatsApp +507 6255-7583 <span aria-hidden="true">↗</span></a><a class="button-primary outline-light" href="contacto.html">Formulario de contacto</a></div>
</section>'''


SERVICES = '''<div class="page-heading"><span class="eyebrow">Áreas de práctica</span><h1>Naturalización en Panamá, con acompañamiento jurídico.</h1><p>El despacho concentra su práctica en el proceso de adquisición de la nacionalidad panameña por naturalización. Cada servicio se define después de revisar las circunstancias de la persona solicitante.</p></div>
      <section class="content-section" id="evaluacion"><span class="section-index">01 · Antes de empezar</span><h2>Evaluación de viabilidad</h2><p>Revisamos la Cédula E, el historial de residencia, los documentos disponibles y las situaciones que requieren especial atención. Esta conversación permite identificar una ruta de trabajo o explicar por qué conviene esperar antes de presentar.</p><p>La evaluación profesional se realiza mediante la <a href="index.html#auditoria">Auditoría Jurídica de Caso (US$49)</a>, una llamada telefónica con el Lic. Alfonso Villarreal. La <a href="index.html#calificacion">orientación inicial</a> es gratuita y solo clasifica su situación.</p><ul class="check-list"><li>Revisión de fechas y antecedentes migratorios.</li><li>Identificación de documentación pendiente.</li><li>Alcance del servicio y propuesta por escrito.</li></ul></section>
      <section class="content-section" id="expediente"><span class="section-index">02 · Preparación</span><h2>Integración del expediente</h2><p>Una solicitud requiere orden documental. Ayudamos a organizar los soportes personales y económicos que correspondan, revisar su coherencia y preparar la presentación conforme a la vía aplicable.</p><p>La lista exacta de requisitos varía según el caso. Para una explicación general, consulte la <a href="''' + GUIDE + '''">guía del despacho</a>.</p></section>
      <section class="content-section" id="representacion"><span class="section-index">03 · Trámite</span><h2>Representación y seguimiento</h2><p>La solicitud se presenta mediante abogado ante el Tribunal Electoral. El despacho realiza seguimiento a las actuaciones y comunica los requerimientos que deban atenderse durante el proceso.</p></section>
      <section class="content-section" id="etapas-finales"><span class="section-index">04 · Acompañamiento</span><h2>Etapas posteriores</h2><p>Orientamos sobre la preparación para la evaluación y las etapas de resolución, juramentación y documentación, cuando procedan. La decisión final corresponde a las autoridades competentes.</p></section>
      <div class="article-callout"><span class="callout-mark" aria-hidden="true">N.</span><div><h2>¿Por dónde comenzar?</h2><p>Con una descripción de su caso y sus fechas de residencia podemos indicarle cómo se inicia la revisión.</p><a class="button-primary" href="contacto.html">Contactar al despacho <span aria-hidden="true">↗</span></a></div></div>'''

VIAS = '''<div class="page-heading"><span class="eyebrow">Panorama general</span><h1>Vías de naturalización que deben evaluarse.</h1><p>La ruta aplicable depende del historial migratorio y de la normativa pertinente. Esta página ofrece una orientación general, no un dictamen sobre un caso concreto.</p></div>
      <section class="content-section" id="residencia"><span class="section-index">01 · Residencia</span><h2>Tiempo de residencia y Cédula E</h2><p>Las fechas de residencia legal y la emisión de la Cédula E son puntos de partida para analizar la posibilidad de solicitar la nacionalidad. No basta contar años de forma aislada: también deben revisarse los antecedentes y la documentación de soporte.</p></section>
      <section class="content-section" id="reciprocidad"><span class="section-index">02 · Supuestos especiales</span><h2>Reciprocidad y otras circunstancias</h2><p>Determinados convenios o circunstancias personales pueden modificar la vía que corresponde examinar. Su aplicación requiere revisar el país de origen y la situación particular; no debe presumirse una excepción sin confirmación jurídica.</p></section>
      <section class="content-section" id="familia"><span class="section-index">03 · Vínculos</span><h2>Vínculos familiares y arraigo</h2><p>Los vínculos con Panamá y el arraigo pueden formar parte del análisis documental. El tipo de prueba y su relevancia dependen de la ruta legal aplicable y de la historia de cada persona.</p></section>
      <section class="route-next"><h2>Una vía correcta empieza con una revisión completa.</h2><p>No podemos determinar elegibilidad solo con una casilla o con una visita a esta página. Reúna los documentos disponibles y solicite una evaluación individual.</p><div class="inline-actions"><a class="button-primary" href="index.html#auditoria">Solicitar la auditoría de US$49 <span aria-hidden="true">→</span></a><a class="text-action" href="verificacion.html">Preparar mi consulta ↗</a></div></section>'''

HONORARIOS = '''<div class="page-heading"><span class="eyebrow">Transparencia</span><h1>Honorarios y alcance del servicio.</h1><p>La evaluación profesional tiene un honorario único y publicado. Los servicios de representación posteriores se comunican en una propuesta personalizada y por escrito, según los antecedentes y la documentación de cada caso.</p></div>
      <div class="table-scroll" tabindex="0" role="region" aria-label="Tabla de honorarios; desplace horizontalmente para ver todas las columnas"><table class="fees-table"><caption>Servicios jurídicos del despacho</caption><thead><tr><th scope="col">Descripción del servicio</th><th scope="col">Alcance orientativo</th><th scope="col">Honorarios</th></tr></thead><tbody><tr><th scope="row">Orientación inicial</th><td>Contacto breve para clasificar la situación y el siguiente paso.</td><td>Gratuita. Sin dictamen jurídico.</td></tr><tr><th scope="row">Auditoría Jurídica de Caso</th><td>Llamada telefónica con el Lic. Alfonso Villarreal, análisis de antecedentes y revisión de documentación.</td><td><strong>US$49</strong>, honorario único.</td></tr><tr><th scope="row">Preparación del expediente</th><td>Organización y revisión de los soportes aplicables.</td><td>Propuesta a medida, por escrito.</td></tr><tr><th scope="row">Representación legal</th><td>Presentación de la solicitud mediante abogado.</td><td>Propuesta a medida, por escrito.</td></tr><tr><th scope="row">Seguimiento del trámite</th><td>Comunicación de actuaciones y requerimientos.</td><td>Según alcance acordado.</td></tr></tbody></table></div>
      <section class="content-section"><h2>Qué cubre y qué no cubre la auditoría</h2><p>Los US$49 corresponden a un servicio profesional independiente de evaluación. No incluyen representación legal, elaboración o presentación de solicitudes, recursos, procesos judiciales ni gestiones administrativas posteriores. Esas actuaciones se cotizan por separado.</p></section>
      <section class="content-section"><h2>Qué debe quedar claro en la propuesta</h2><p>El alcance de la representación, las etapas incluidas, los posibles gastos de terceros y las condiciones de pago deben explicarse antes de iniciar el trabajo. Las tasas oficiales, traducciones u otros gastos externos pueden variar y no se presumen incluidos sin confirmación.</p></section>
      <div class="article-callout"><span class="callout-mark" aria-hidden="true">N.</span><div><h2>Solicite una propuesta para su situación.</h2><p>Comparta un resumen de su caso y le indicaremos cómo continuar con la evaluación.</p><a class="button-primary" href="contacto.html">Solicitar información <span aria-hidden="true">↗</span></a></div></div>'''

NOTICE = '''<div class="page-heading"><span class="eyebrow">Aviso legal</span><h1>Información para utilizar este sitio.</h1></div>
      <section class="content-section"><h2>Contenido informativo</h2><p>Los contenidos de Naturalízate.pa ofrecen información general sobre la naturalización panameña. No sustituyen la evaluación de una situación individual, no constituyen una opinión jurídica para una persona determinada y pueden requerir actualización cuando cambien normas o criterios administrativos.</p></section>
      <section class="content-section"><h2>Relación profesional y comunicaciones</h2><p>El envío de un mensaje, una consulta por WhatsApp o el uso de la lista de verificación no establece por sí solo una relación de representación. El alcance del trabajo y los honorarios deben quedar acordados directamente con el despacho antes de iniciar un servicio.</p><p>No incluya información especialmente sensible en el formulario inicial. Si se requiere documentación personal, el despacho le indicará un canal y un procedimiento apropiados para compartirla.</p></section>
      <section class="content-section"><h2>Resultados y plazos</h2><p>La aprobación de una solicitud y los tiempos de tramitación dependen de las autoridades panameñas. Naturalízate.pa no garantiza la concesión de la nacionalidad ni un plazo exacto.</p></section>
      <section class="content-section" id="sitios-externos"><h2>Sitios externos</h2><p>Algunos enlaces dirigen a servicios de terceros, como WhatsApp, Google Maps o sitios institucionales. Cada sitio aplica sus propias condiciones. Esos enlaces se ofrecen por conveniencia y no implican control sobre el contenido externo.</p></section>
      <section class="content-section"><h2>Contacto</h2><p>Para obtener información sobre su caso, escriba a <a href="mailto:villarreallawyers@proton.me">villarreallawyers@proton.me</a> o visite la <a href="contacto.html">página de contacto</a>.</p></section>'''

INFORMATION = '''<div class="page-heading"><span class="eyebrow">Información legal gratuita</span><h1>Recursos para empezar con claridad.</h1><p>Una biblioteca breve para entender el proceso antes de tomar decisiones. Los artículos son de carácter general y deben contrastarse con la situación personal y las fuentes oficiales vigentes.</p></div>
      <section class="content-section" id="articulos"><h2>Artículos y novedades</h2><div class="article-list"><a href="''' + GUIDE + '''"><span>Guía del despacho · Lectura completa</span><strong>Requisitos de naturalización en Panamá: Cédula E y solvencia</strong><small>Documentación, rutas de evaluación y fases del procedimiento. →</small></a><a href="#proceso"><span>Guía breve</span><strong>Las etapas del trámite de naturalización</strong><small>Un recorrido orientativo desde la evaluación inicial hasta las etapas finales. →</small></a><a href="verificacion.html"><span>Herramienta interactiva</span><strong>Qué tener a mano para una primera consulta</strong><small>Lista de comprobación documental; no determina elegibilidad. →</small></a></div></section>
      <section class="content-section" id="requisitos"><h2>Requisitos y situación personal</h2><p>El análisis suele comenzar por la residencia, el historial migratorio y la documentación disponible. Los requisitos concretos dependen de la vía aplicable. Consulte la <a href="''' + GUIDE + '''">guía detallada del despacho</a> y solicite una revisión si tiene dudas sobre fechas o documentos.</p></section>
      <section class="content-section" id="documentos"><h2>Documentos del expediente</h2><p>Antes de solicitar se revisan documentos de identidad, constancias de residencia y otras pruebas personales o económicas que correspondan. Evite dar por completa una carpeta documental a partir de una lista genérica.</p></section>
      <section class="content-section" id="solvencia"><h2>Solvencia económica</h2><p>La acreditación de medios de vida se analiza con los soportes documentales aplicables. La guía del despacho explica ejemplos de pruebas; su pertinencia debe confirmarse para cada expediente.</p></section>
      <section class="content-section" id="examen"><h2>Evaluación y examen</h2><p>El proceso puede incluir una evaluación de conocimientos y otras actuaciones ante las autoridades. La preparación debe basarse en las indicaciones vigentes comunicadas para el expediente.</p></section>
      <section class="content-section" id="proceso"><h2>Etapas del proceso</h2><ol class="process-steps"><li><span>01</span><div><strong>Evaluación y preparación</strong><p>Revisión de la ruta legal y organización del expediente.</p></div></li><li><span>02</span><div><strong>Gestiones migratorias</strong><p>Verificación de los antecedentes y soportes que correspondan.</p></div></li><li><span>03</span><div><strong>Presentación y seguimiento</strong><p>Trámite mediante abogado ante el Tribunal Electoral.</p></div></li><li><span>04</span><div><strong>Resolución y juramentación</strong><p>Etapas finales, cuando corresponda y según decisión estatal.</p></div></li></ol></section>
      <section class="content-section" id="enlaces-oficiales"><h2>Enlaces institucionales</h2><p>Consulte siempre las fuentes oficiales para verificar procedimientos y comunicaciones vigentes.</p><ul class="official-links"><li><a href="https://www.tribunal-electoral.gob.pa/" target="_blank" rel="noopener noreferrer">Tribunal Electoral de Panamá <span aria-hidden="true">↗</span></a></li><li><a href="https://www.migracion.gob.pa/" target="_blank" rel="noopener noreferrer">Servicio Nacional de Migración <span aria-hidden="true">↗</span></a></li></ul></section>'''

VERIFICATION = '''<div class="page-heading"><span class="eyebrow">Herramienta orientativa</span><h1>Lista de verificación para su primera consulta.</h1><p>Marque los elementos que ya tiene a mano. Esta lista solo organiza la conversación: <strong>no evalúa elegibilidad, no guarda respuestas y no sustituye asesoría jurídica.</strong></p></div>
      <div class="checklist" id="checklist"><section class="checklist-group"><div class="checklist-heading"><span>01</span><h2>Identidad y residencia</h2></div><label><input type="checkbox" data-check-item /> Tengo a mano mi documento de identidad o pasaporte.</label><label><input type="checkbox" data-check-item /> Puedo consultar la fecha de emisión de mi Cédula E.</label></section><section class="checklist-group"><div class="checklist-heading"><span>02</span><h2>Historia migratoria</h2></div><label><input type="checkbox" data-check-item /> Tengo anotadas mis fechas de residencia y ausencias relevantes.</label><label><input type="checkbox" data-check-item /> Sé si existe alguna circunstancia familiar o de reciprocidad que deba comentar.</label></section><section class="checklist-group"><div class="checklist-heading"><span>03</span><h2>Documentación de respaldo</h2></div><label><input type="checkbox" data-check-item /> Puedo identificar mis constancias de trabajo, ingresos u otros medios de vida.</label><label><input type="checkbox" data-check-item /> Tengo documentos personales que podrían ser relevantes para la revisión.</label></section><section class="checklist-group"><div class="checklist-heading"><span>04</span><h2>Su siguiente paso</h2></div><p>Si faltan elementos, puede consultar igualmente. El despacho le indicará qué información conviene reunir según su caso.</p></section></div>
      <div class="checklist-summary" aria-live="polite"><div><span class="eyebrow">Preparación orientativa</span><p id="checklist-count">0 de 6 elementos marcados</p><small>Un número mayor no equivale a una solicitud aprobable.</small></div><div class="progress-track" role="progressbar" aria-label="Elementos revisados" aria-valuemin="0" aria-valuemax="6" aria-valuenow="0"><span id="checklist-progress"></span></div><a id="checklist-whatsapp" class="button-primary" href="''' + WHATSAPP + '''" target="_blank" rel="noopener noreferrer">Conversar por WhatsApp <span aria-hidden="true">↗</span></a></div>
      <p class="legal-small">La lista no transmite ningún dato por sí sola. Si pulsa el enlace de WhatsApp, se abrirá un mensaje genérico que puede revisar antes de enviarlo.</p>'''

CONTACT = '''<div class="page-heading"><span class="eyebrow">Contáctenos</span><h1>Cuéntenos sobre su caso.</h1><p>Comparta una descripción breve y le indicaremos cómo continuar con la evaluación. No incluya en este primer mensaje números de documentos ni información especialmente sensible.</p></div>
      <p class="contact-hint">La evaluación profesional es la <a href="index.html#auditoria"><strong>Auditoría Jurídica de Caso (US$49)</strong></a>. Si prefiere una clasificación inicial sin costo, use el <a href="index.html#calificacion">formulario de calificación</a>.</p>
      <form class="contact-form contact-main-form" data-wa-form><div class="form-row"><label for="main-name">Nombre <span aria-hidden="true">*</span></label><input id="main-name" name="nombre" type="text" autocomplete="name" required /></div><div class="form-row"><label for="main-email">Correo electrónico <span aria-hidden="true">*</span></label><input id="main-email" name="correo" type="email" autocomplete="email" required /></div><div class="form-row"><label for="main-phone">Teléfono o WhatsApp</label><input id="main-phone" name="telefono" type="tel" autocomplete="tel" /></div><div class="form-row"><label for="main-country">País de origen (opcional)</label><input id="main-country" name="pais" type="text" autocomplete="country-name" /></div><div class="form-row"><label for="main-message">Mensaje <span aria-hidden="true">*</span></label><textarea id="main-message" name="mensaje" rows="5" required></textarea></div><label class="check-line"><input type="checkbox" name="novedades" value="Sí" /> Me interesa recibir novedades legales por correo</label><div class="contact-form-actions"><button class="form-submit" type="submit">Enviar consulta <span aria-hidden="true">→</span></button><a class="text-action" href="''' + WHATSAPP + '''" target="_blank" rel="noopener noreferrer">Prefiero WhatsApp ↗</a></div><p class="form-note" data-form-status role="status">Al enviar, se abrirá WhatsApp con sus datos para que revise y confirme el mensaje. La página no almacena su información.</p></form>
      <section class="content-section" id="mapa"><h2>Visítenos en Ciudad de Panamá</h2><p><strong>Scotia Plaza, Piso 7</strong> · Avenida Federico Boyd, Ciudad de Panamá. Coordine su visita previamente con el despacho.</p><div class="map-load" data-map-container><div class="map-load-inner"><span aria-hidden="true">⌖</span><p>Mapa interactivo disponible bajo solicitud.</p><button type="button" data-load-map>Cargar mapa de ubicación</button><small>Al cargarlo, Google Maps recibirá información técnica de su navegador.</small></div></div></section>'''

HOME_BODY = columns(
    HOME,
    [
        ("#auditoria", "Auditoría Jurídica · US$49"),
        ("#calificacion", "Evaluar mi situación"),
        ("#quien-puede", "Quién puede solicitar la nacionalidad"),
        ("#riesgos", "Por qué revisar su caso antes de presentar"),
        ("#como-trabajamos", "Cómo trabajamos, paso a paso"),
        ("#preguntas", "Preguntas frecuentes"),
        ("#contratacion", "Servicios posteriores"),
        ("informacion-legal.html#proceso", "Etapas del proceso"),
        ("honorarios.html", "Honorarios del despacho"),
    ],
    extra="home-columns",
    share=False,
) + DOORS + VIAS_HOME + RISKS + AUDIT + STEPS + PROFILE + faq_section() + CONTRACT + qualification_section() + CLOSING

PAGES = {
    "index.html": {"title": "Naturalización panameña · Auditoría Jurídica de Caso US$49 | Naturalízate.pa", "description": "Su camino hacia la nacionalidad panameña comienza con una evaluación jurídica seria. Orientación inicial gratuita y Auditoría Jurídica de Caso por US$49 con el Lic. Alfonso Villarreal.", "active": "inicio", "home": True, "robots": "index, follow", "body": HOME_BODY},
    "servicios.html": {"title": "Áreas de práctica | Naturalízate.pa", "description": "Evaluación de viabilidad, expediente, representación y seguimiento para procesos de naturalización en Panamá.", "active": "servicios", "body": columns(SERVICES)},
    "vias.html": {"title": "Vías de naturalización | Naturalízate.pa", "description": "Información general sobre residencia, reciprocidad y vínculos a considerar en una solicitud de naturalización panameña.", "active": "vias", "body": columns(VIAS)},
    "honorarios.html": {"title": "Honorarios y alcance | Naturalízate.pa", "description": "Auditoría Jurídica de Caso por US$49 y propuesta de honorarios personalizada para los servicios posteriores de naturalización en Panamá.", "active": "honorarios", "body": columns(HONORARIOS)},
    "aviso-legal.html": {"title": "Aviso legal | Naturalízate.pa", "description": "Alcance de la información del sitio, comunicación con el despacho, resultados y enlaces externos.", "active": "aviso", "body": columns(NOTICE)},
    "informacion-legal.html": {"title": "Información legal gratuita | Naturalízate.pa", "description": "Guías, etapas, requisitos generales y fuentes institucionales sobre la naturalización panameña.", "active": "informacion", "body": columns(INFORMATION, [("informacion-legal.html#articulos", "Guías del despacho"), ("informacion-legal.html#proceso", "Etapas del proceso"), ("informacion-legal.html#enlaces-oficiales", "Fuentes oficiales"), ("verificacion.html", "Lista de verificación"), ("contacto.html", "Solicitar orientación")], "Recursos relacionados")},
    "verificacion.html": {"title": "Lista de verificación | Naturalízate.pa", "description": "Organice la información y documentación que puede tener a mano antes de conversar con un abogado sobre naturalización en Panamá.", "active": "verificacion", "body": columns(VERIFICATION, [("informacion-legal.html#requisitos", "Requisitos generales"), ("vias.html", "Vías de naturalización"), ("servicios.html#evaluacion", "Evaluación de viabilidad"), ("contacto.html", "Contactar al despacho")], "Para continuar")},
    "contacto.html": {"title": "Contáctenos | Naturalízate.pa", "description": "Escriba al despacho Naturalízate.pa, consulte el teléfono WhatsApp y la ubicación en Scotia Plaza, Ciudad de Panamá.", "active": "contacto", "body": columns(CONTACT, [("index.html#auditoria", "Auditoría Jurídica · US$49"), ("servicios.html", "Servicios jurídicos"), ("honorarios.html", "Honorarios"), ("informacion-legal.html", "Información legal"), ("aviso-legal.html", "Aviso legal")], "Enlaces del despacho")},
}
