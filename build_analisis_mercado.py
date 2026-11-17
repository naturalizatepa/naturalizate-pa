#!/usr/bin/env python3
"""
Análisis de mercado y estructura de honorarios para naturalización panameña.
Documento interno de Naturalízate.pa (marca del despacho).

Salida: analisis-mercado-honorarios.html
Uso:    python3 build_analisis_mercado.py
"""
from build_requisitos import (
    CSS, FONT_INTER, FONT_PLAYFAIR, FONT_PLAYFAIR_IT, LOGO_NAVY, LOGO_WHITE,
    SITE, WA, head, footer, ROOT,
)

OUT = ROOT / "analisis-mercado-honorarios.html"

EXTRA_CSS = """
  .internal{background:#8A6A2F;color:#fff;font-size:.72rem;letter-spacing:1.6px;text-transform:uppercase;
    text-align:center;padding:6px 12px;font-weight:700;}
  .hero h1{max-width:820px;}
  .kpi{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;max-width:1000px;margin:26px auto 0;}
  .kpi>div{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.16);border-radius:8px;padding:16px 16px 14px;}
  .kpi .n,.kpi .l{background:none;border:0;padding:0;border-radius:0;}
  .kpi .n{font-family:var(--serif);font-size:1.55rem;font-weight:600;color:#fff;line-height:1.1;}
  .kpi .l{font-size:.7rem;letter-spacing:1.2px;text-transform:uppercase;color:rgba(255,255,255,.62);margin-top:6px;line-height:1.4;}
  @media (max-width:820px){.kpi{grid-template-columns:1fr 1fr;}}

  .rec{max-width:1000px;margin:30px auto;border:2px solid var(--navy);border-radius:10px;overflow:hidden;}
  .rec-head{background:var(--navy);color:#fff;padding:18px 24px;}
  .rec-head .k{font-size:.68rem;letter-spacing:2px;text-transform:uppercase;color:rgba(255,255,255,.7);}
  .rec-head h3{font-family:var(--serif);font-size:1.3rem;font-weight:600;margin-top:4px;}
  .rec-body{padding:22px 24px;}
  .rec-body p{font-size:.96rem;margin-bottom:14px;}
  .rec-body p:last-child{margin-bottom:0;}

  .price-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;max-width:1000px;margin:26px auto;}
  @media (max-width:860px){.price-grid{grid-template-columns:1fr;}}
  .pr{border:1px solid var(--g200);border-radius:10px;padding:22px 20px;background:#fff;display:flex;flex-direction:column;}
  .pr.new{border:2px solid var(--navy);box-shadow:0 14px 34px rgba(13,27,42,.09);}
  .pr .tag{font-size:.62rem;font-weight:700;letter-spacing:1.4px;text-transform:uppercase;color:var(--g600);margin-bottom:6px;}
  .pr.new .tag{color:var(--navy);}
  .pr h4{font-family:var(--serif);font-size:1.05rem;color:var(--navy);font-weight:600;margin-bottom:2px;}
  .pr .amount{font-family:var(--serif);font-size:2.1rem;font-weight:700;color:var(--navy);line-height:1.1;margin:8px 0 2px;}
  .pr .was{font-size:.78rem;color:var(--g600);}
  .pr .was s{color:var(--g400);}
  .pr ul{list-style:none;margin-top:12px;}
  .pr li{font-size:.86rem;padding:6px 0 6px 20px;position:relative;border-bottom:1px solid var(--g200);}
  .pr li:last-child{border-bottom:none;}
  .pr li::before{content:"·";position:absolute;left:6px;color:var(--navy);font-weight:700;}
  .pr .note{margin-top:auto;padding-top:12px;font-size:.76rem;color:var(--g600);}

  /* barras de posicionamiento */
  .bars{max-width:1000px;margin:26px auto;border:1px solid var(--g200);border-radius:10px;padding:24px 24px 18px;background:#fff;}
  .bar-row{display:grid;grid-template-columns:190px 1fr 88px;gap:12px;align-items:center;margin-bottom:10px;font-size:.85rem;}
  .bar-row .lb{color:var(--g700);}
  .bar-row .track{display:block;background:var(--g100);border-radius:3px;height:20px;position:relative;overflow:hidden;}
  .bar-row .fill{display:block;height:20px;background:var(--navy-2);border-radius:3px;}
  .bar-row.you .fill{background:var(--navy);}
  .bar-row.you .lb{font-weight:700;color:var(--navy);}
  .bar-row .val{text-align:right;font-variant-numeric:tabular-nums;color:var(--navy);font-weight:600;}
  .bars .foot{margin-top:14px;font-size:.78rem;color:var(--g600);border-top:1px solid var(--g200);padding-top:12px;}

  .addons{max-width:1000px;margin:24px auto;}
  .addons table{min-width:560px;}
  .tag-pill{display:inline-block;font-size:.62rem;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;
    border:1px solid var(--g300);border-radius:20px;padding:2px 9px;color:var(--g600);background:var(--g50);}
  .tag-pill.hot{border-color:var(--navy);color:var(--navy);background:#fff;}

  .steps{max-width:1000px;margin:24px auto;counter-reset:s;}
  .steps li{list-style:none;position:relative;padding:0 0 18px 44px;border-left:1px solid var(--g200);margin-left:12px;}
  .steps li:last-child{border-left-color:transparent;padding-bottom:0;}
  .steps li::before{counter-increment:s;content:counter(s);position:absolute;left:-13px;top:-2px;width:26px;height:26px;
    border-radius:50%;background:var(--navy);color:#fff;font-size:.78rem;font-weight:700;display:grid;place-items:center;}
  .steps strong{display:block;color:var(--navy);font-size:.95rem;margin-bottom:2px;}
  .steps p{font-size:.9rem;margin:0;}
  .steps .when{font-size:.72rem;font-weight:700;letter-spacing:1.4px;text-transform:uppercase;color:var(--g600);margin-bottom:4px;}

  .src{max-width:1000px;margin:20px auto 0;font-size:.85rem;}
  .src li{padding:7px 0;border-bottom:1px solid var(--g200);list-style:none;}
  .src li:last-child{border-bottom:none;}
  .src a{word-break:break-word;}
  .warn-list{max-width:1000px;margin:20px auto;}
  .warn-list li{font-size:.93rem;padding:8px 0 8px 26px;position:relative;border-bottom:1px solid var(--g200);list-style:none;}
  .warn-list li::before{content:"!";position:absolute;left:0;top:8px;width:16px;height:16px;border-radius:50%;
    background:#FBF7F0;border:1px solid #EADFC8;color:#8A6A2F;font-size:.66rem;font-weight:700;display:grid;place-items:center;}
  @media print{
    .internal{background:#fff!important;color:#8A6A2F;border-bottom:1px solid #ddd;}
    .kpi>div{background:#f5f5f5!important;border-color:#ddd;}
    .kpi .n,.kpi .l{color:#0D1B2A!important;}
    .bars,.pr,.rec,.steps li{page-break-inside:avoid;}
    .price-grid,.kpi{page-break-inside:avoid;}
  }
"""

BODY = """
<div class="internal">Documento interno · uso del despacho · no publicar</div>

<header class="nav">
  <div class="wrap">
    <a class="nav-logo" href="{SITE}" aria-label="Naturalízate.pa">
      <img src="data:image/svg+xml;base64,__LOGO_NAVY__" alt="Naturalízate.pa" width="164" height="22" />
    </a>
    <nav class="nav-links" aria-label="Navegación">
      <a href="#mercado">Mercado</a>
      <a href="#posicion">Posición</a>
      <a href="#economia">Economía</a>
      <a href="#propuesta">Propuesta</a>
      <a class="nav-cta" href="#plan">Plan de acción</a>
    </nav>
  </div>
</header>

<section class="hero">
  <div class="wrap">
    <img class="hero-logo" src="data:image/svg+xml;base64,__LOGO_WHITE__" alt="Naturalízate.pa" width="196" height="26" />
    <div class="kicker">Análisis de mercado · noviembre de 2026</div>
    <h1>Cuánto cobrar por una naturalización: <em>lo que dice el mercado y lo que conviene hacer</em></h1>
    <p class="lead">Comparación de honorarios de siete despachos, el mínimo del baremo oficial, los gastos del Estado que el cliente paga aparte y una propuesta de estructura de precios para Naturalízate.pa.</p>
    <div class="kpi">
      <div><div class="n">$3,500</div><div class="l">Mínimo del baremo para naturalización</div></div>
      <div><div class="n">$3,000–6,000</div><div class="l">Rango de honorarios observado</div></div>
      <div><div class="n">$1,300–2,100</div><div class="l">Gastos del Estado, aparte</div></div>
      <div><div class="n">$6,300–7,950</div><div class="l">Costo total que ve el cliente</div></div>
    </div>
  </div>
</section>

<main>
  <div class="wrap">
    <article class="article">

      <section>
        <div class="sec-head">
          <div class="num">Resumen ejecutivo</div>
          <h2>La conclusión, primero</h2>
        </div>
        <p>Su Modalidad Esencial ($3,800) está bien ubicada: queda apenas por encima del mínimo legal y en el mismo tramo que los despachos que publican precio. La <strong>Modalidad Integral ($5,500)</strong> sí está por debajo de lo que el mercado cobra por un servicio equivalente y de lo que cuesta su propio tiempo.</p>
        <p>Tres movimientos, en orden de impacto:</p>
        <ol class="clean">
          <li><strong>Subir la Integral a $5,900</strong> para clientes nuevos (hoy $5,500): queda en la banda alta sin cruzar el umbral psicológico de los $6,000 y antes de impuestos y gastos del Estado.</li>
          <li><strong>Crear un tercer nivel de $3,500</strong> («Solo expediente») para capturar al cliente sensible al precio sin bajar del mínimo del baremo. Es el piso legal: no se puede cobrar menos.</li>
          <li><strong>Vender servicios sueltos</strong> —preparación del examen, atención de requerimientos, cédula y pasaporte— que hoy regala dentro de la Integral o pierde frente a quien los cobra aparte.</li>
        </ol>
      </section>

      <section class="sec" id="mercado">
        <div class="sec-head">
          <div class="num">01 · Mercado</div>
          <h2>Quién cobra cuánto, y <em>qué incluye</em></h2>
        </div>
        <p>Honorarios publicados por despachos que tramitan naturalización panameña. Todos excluyen los gastos del Estado, que el cliente paga aparte.</p>

        <div class="table-wrap">
          <table>
            <thead><tr><th scope="col">Despacho</th><th scope="col">Honorarios</th><th scope="col">Estructura de pago</th><th scope="col">Nota</th></tr></thead>
            <tbody>
              <tr><th scope="row">Chen Lee y Asociados</th><td class="num-cell">$3,000</td><td>No publicada</td><td>Precio de lista en su portal de honorarios.</td></tr>
              <tr><th scope="row">Legalys</th><td class="num-cell">$3,500 + $300</td><td>No publicada</td><td>Su propia guía menciona un rango de $3,500 a $8,000 según el baremo.</td></tr>
              <tr><th scope="row">Kery Cruz</th><td class="num-cell">$3,990</td><td>50 / 25 / 25</td><td>Más ≈$272 iniciales y ≈$786 al concederse la carta.</td></tr>
              <tr><th scope="row"><strong>Naturalízate.pa</strong></th><td class="num-cell"><strong>$3,800 · $5,500</strong></td><td>Fraccionado por fases</td><td>Esencial e Integral; Integral incluye recursos y post-jura.</td></tr>
              <tr><th scope="row">Kraemer &amp; Kraemer</th><td class="num-cell">$5,000</td><td>3 pagos</td><td>Total publicado $6,300 con gastos del Estado.</td></tr>
              <tr><th scope="row">Studio Panamá Italia</th><td class="num-cell">$6,000</td><td>3 × $2,000</td><td>Total estimado $7,500–$7,950 con gastos.</td></tr>
              <tr><th scope="row">Rango citado por guías 2026</th><td class="num-cell">$4,500–6,000</td><td>3 pagos</td><td>Total $6,300–$7,840; gastos del Estado ≈$2,100.</td></tr>
            </tbody>
          </table>
        </div>

        <div class="callout">
          <span class="label">Lectura del cuadro</span>
          <p>El mercado tiene tres bandas: <strong>baja</strong> ($3,000–3,500, despachos que compiten por precio), <strong>media</strong> ($3,800–5,000) y <strong>alta</strong> ($5,000–6,000+, firmas internacionales o con marca). La Esencial está en el borde bajo de la banda media; la Integral, en el borde bajo de la alta.</p>
        </div>

        <h3>El piso legal: el baremo</h3>
        <p>La <strong>Tarifa de Honorarios Profesionales Mínimos de los Abogados de la República de Panamá</strong> fija la naturalización en <strong>B/.3,500</strong>. Cobrar menos es una falta ética, no una estrategia comercial. Ese dato hace dos cosas: protege su precio frente al cliente que «consiguió $2,500 en otro lado» y le pone un límite claro a cualquier descuento.</p>

        <div class="callout warn">
          <span class="label">Advertencia sobre el competidor de $3,000</span>
          <p>Si el dato de Chen Lee es exacto, están por debajo del mínimo del baremo. No conviene seguirlos: el cliente que compra por precio en un trámite de dos años es el que más consultas consume y el que más probablemente abandona a mitad de expediente.</p>
        </div>
      </section>

      <section class="sec" id="posicion">
        <div class="sec-head">
          <div class="num">02 · Posición</div>
          <h2>Dónde queda su precio <em>hoy</em></h2>
        </div>
        <div class="bars">
          <div class="bar-row"><span class="lb">Chen Lee</span><span class="track"><span class="fill" style="width:43%"></span></span><span class="val">$3,000</span></div>
          <div class="bar-row"><span class="lb">Legalys</span><span class="track"><span class="fill" style="width:50%"></span></span><span class="val">$3,500</span></div>
          <div class="bar-row you"><span class="lb">Su Esencial</span><span class="track"><span class="fill" style="width:54%"></span></span><span class="val">$3,800</span></div>
          <div class="bar-row"><span class="lb">Kery Cruz</span><span class="track"><span class="fill" style="width:57%"></span></span><span class="val">$3,990</span></div>
          <div class="bar-row"><span class="lb">Kraemer</span><span class="track"><span class="fill" style="width:71%"></span></span><span class="val">$5,000</span></div>
          <div class="bar-row you"><span class="lb">Su Integral</span><span class="track"><span class="fill" style="width:79%"></span></span><span class="val">$5,500</span></div>
          <div class="bar-row"><span class="lb">Studio Panamá Italia</span><span class="track"><span class="fill" style="width:86%"></span></span><span class="val">$6,000</span></div>
          <div class="bars-foot foot">Barras proporcionales sobre una escala de $7,000. Honorarios sin gastos del Estado.</div>
        </div>

        <p>El hueco está a la vista: entre <strong>$4,000 y $5,000</strong> no hay nadie publicando, y su Integral —que es el servicio más completo del cuadro, con recursos y acompañamiento posterior a la jura— está $500 por debajo de una firma que no incluye nada de eso.</p>
        <p>Hay, además, una asimetría de información a su favor: casi ningún competidor publica qué incluye. Usted publica dos modalidades con alcance definido, consulta gratuita con veredicto escrito y honorarios fijos. Eso sostiene un precio por encima del promedio.</p>
      </section>

      <section class="sec" id="economia">
        <div class="sec-head">
          <div class="num">03 · Economía</div>
          <h2>Lo que cuesta su <em>propio tiempo</em></h2>
        </div>
        <p>El proceso dura entre 19 y 22 meses en su estimación (el mercado habla de 2 a 3 años). Ese plazo se traduce en horas reales: armado, revisiones, seguimiento institucional, preparación del examen, jura y cédula.</p>

        <div class="table-wrap">
          <table>
            <thead><tr><th scope="col">Escenario</th><th scope="col">Horas por caso</th><th scope="col">Honorario</th><th scope="col">Valor hora efectivo</th></tr></thead>
            <tbody>
              <tr><th scope="row">Integral · caso limpio</th><td>70 h</td><td>$5,500</td><td class="num-cell">≈ $79</td></tr>
              <tr><th scope="row">Integral · con requerimientos</th><td>100 h</td><td>$5,500</td><td class="num-cell">≈ $55</td></tr>
              <tr><th scope="row">Integral a $5,900 · con requerimientos</th><td>100 h</td><td>$5,900</td><td class="num-cell">≈ $59</td></tr>
              <tr><th scope="row">Esencial · caso limpio</th><td>50 h</td><td>$3,800</td><td class="num-cell">≈ $76</td></tr>
            </tbody>
          </table>
        </div>
        <p class="disclaimer">Las horas son un supuesto de trabajo para comparar escenarios, no una medición del despacho. Ajústelas con su registro real antes de fijar el precio definitivo.</p>

        <p>Tome como referencia la propia tarifa mínima: la consulta verbal con examen de documentos se tarifa en <strong>B/.150 por hora</strong>. Con eso, un caso de 100 horas «vale» $15,000 en tiempo de abogado. El mercado no paga eso —paga un precio de producto, no de hora— pero el dato explica por qué conviene <strong>acotar el alcance</strong> en lugar de bajar el precio.</p>

        <div class="callout info">
          <span class="label">El costo que no se ve</span>
          <p>Un requerimiento mal atendido no cuesta un correo: cuesta meses de un expediente que ya está pagado. Por eso la Integral, que incluye la atención de requerimientos y los recursos, no puede costar lo mismo que una Esencial sin ellos. Si se igualan, el cliente exigirá lo máximo por el precio de lo mínimo.</p>
        </div>
      </section>

      <section class="sec" id="propuesta">
        <div class="sec-head">
          <div class="num">04 · Propuesta</div>
          <h2>Tres niveles, <em>un piso claro</em></h2>
        </div>
        <p>La estructura recomendada conserva lo que ya funciona y añade una puerta de entrada al precio del baremo. Ningún nivel baja de $3,500.</p>

        <div class="price-grid">
          <div class="pr">
            <div class="tag">Nuevo · entrada</div>
            <h4>Solo expediente</h4>
            <div class="amount">$3,500</div>
            <div class="was">Piso del baremo</div>
            <ul>
              <li>Evaluación de viabilidad por escrito</li>
              <li>Lista de documentos y modelos de cartas</li>
              <li>Revisión del expediente antes de firmar</li>
              <li>Poder y memorial redactados</li>
              <li>Sin seguimiento institucional ni examen</li>
            </ul>
            <div class="note">Para quien va a gestionar solo. Alcance cerrado por escrito.</div>
          </div>
          <div class="pr new">
            <div class="tag">Recomendada · mantener</div>
            <h4>Esencial</h4>
            <div class="amount">$3,800</div>
            <div class="was">Precio actual</div>
            <ul>
              <li>Todo lo anterior</li>
              <li>Presentación del expediente</li>
              <li>Seguimiento ante el Tribunal Electoral</li>
              <li>Guía y simulacro del examen</li>
              <li>Comunicación directa con el abogado</li>
            </ul>
            <div class="note">Su producto de volumen. No tocar.</div>
          </div>
          <div class="pr">
            <div class="tag">Actualización</div>
            <h4>Integral</h4>
            <div class="amount">$5,900</div>
            <div class="was"><s>$5,500</s> · +7%</div>
            <ul>
              <li>Todo lo incluido en Esencial</li>
              <li>Poderes, notaría y legalizaciones coordinadas</li>
              <li>Atención de requerimientos y recursos</li>
              <li>Preparación 1 a 1 del examen</li>
              <li>Cédula y pasaporte después de la jura</li>
            </ul>
            <div class="note">Sigue por debajo de la firma internacional ($6,000).</div>
          </div>
        </div>

        <h3>Servicios sueltos que hoy no cobra</h3>
        <div class="addons table-wrap">
          <table>
            <thead><tr><th scope="col">Servicio</th><th scope="col">Precio sugerido</th><th scope="col">Para quién</th></tr></thead>
            <tbody>
              <tr><th scope="row">Auditoría de expediente <span class="tag-pill">puerta de entrada</span></th><td class="num-cell">$350–450</td><td>Quien ya tiene abogado o viene de otro despacho. Se abona al honorario si contrata.</td></tr>
              <tr><th scope="row">Preparación intensiva del examen <span class="tag-pill hot">alta demanda</span></th><td class="num-cell">$450–650</td><td>Clientes propios y de terceros; el examen es la etapa que más ansiedad genera.</td></tr>
              <tr><th scope="row">Atención de requerimiento</th><td class="num-cell">$600–900</td><td>Expedientes de otros despachos que llegaron con observaciones.</td></tr>
              <tr><th scope="row">Recurso de reconsideración</th><td class="num-cell">$1,200–1,500</td><td>Casos con negativa o devolución; incluye memorial y seguimiento.</td></tr>
              <tr><th scope="row">Cédula y pasaporte post-jura</th><td class="num-cell">$350–450</td><td>Hoy incluido en la Integral; véndalo aparte a los clientes Esencial.</td></tr>
              <tr><th scope="row">Segundo solicitante del mismo núcleo</th><td class="num-cell">–20% sobre Integral</td><td>Cónyuge o hijo que inicia después: comparte expediente y documentos.</td></tr>
            </tbody>
          </table>
        </div>

        <h3>Cómo se cobra y cómo se defiende</h3>
        <ul class="clean">
          <li><strong>Pago 50 / 30 / 20:</strong> a la firma del poder, a la presentación y a la resolución. Cobra temprano el trabajo que se hace temprano y deja el último tramo atado al resultado del trámite.</li>
          <li><strong>Gastos del Estado siempre aparte</strong> ($1,300–2,100: presentación, Tribunal Electoral, resolución, juramentación y cédula). Se presupuestan por escrito y se pagan contra comprobante: nunca se absorben en el honorario.</li>
          <li><strong>Descuento máximo: 10%</strong> y solo en efectivo si el cliente paga más del 70% al inicio. Jamás por debajo de $3,500.</li>
          <li><strong>Revisión anual de honorarios</strong> por inflación, con fecha de corte (por ejemplo, cada enero). Comuníquela a los clientes en curso y aplíquela a nuevas contrataciones.</li>
          <li><strong>Recargo por reactivación:</strong> $450 si el expediente se detuvo por falta de documentos del cliente. Desincentiva el abandono y reconoce el trabajo repetido.</li>
        </ul>

        <div class="callout warn">
          <span class="label">Qué no hacer</span>
          <ul class="warn-list" style="margin-top:6px;">
            <li>No publicar «desde $3,500» sin explicar qué incluye: atrae exactamente al cliente que solo compara cifras.</li>
            <li>No igualar el precio del competidor de $3,000: está por debajo del baremo y le traslada su estructura de costos.</li>
            <li>No prometer plazos para justificar un precio alto. El plazo depende del Estado; el precio se justifica por alcance y riesgo.</li>
            <li>No mezclar honorarios y gastos del Estado en una sola cifra: el cliente compara totales y el suyo se ve más caro de lo que es.</li>
          </ul>
        </div>
      </section>

      <section class="sec" id="plan">
        <div class="sec-head">
          <div class="num">05 · Implementación</div>
          <h2>Qué cambiar y <em>en qué orden</em></h2>
        </div>

        <ol class="steps">
          <li><p class="when">Semana 1</p><strong>Fijar la lista de precios</strong><p>Esencial $3,800 · Integral $5,900 · Solo expediente $3,500, con el alcance de cada uno por escrito en una página. Sin esta hoja, cualquier conversación de precio se pierde.</p></li>
          <li><p class="when">Semana 1</p><strong>Ajustar la landing</strong><p>Actualizar la Integral a $5,900 y añadir el nivel de entrada. Mostrar la Integral primero (ancla) y la Esencial como opción de volumen. Añadir la línea «gastos del Estado aparte, presupuestados por escrito».</p></li>
          <li><p class="when">Semana 2</p><strong>Guion de WhatsApp y consulta</strong><p>Tres frases: qué incluye cada nivel, cuánto son los gastos del Estado y por qué el precio no se negocia (baremo). Enviar la tabla antes de la llamada para que el cliente llegue informado.</p></li>
          <li><p class="when">Mes 1</p><strong>Activar servicios sueltos</strong><p>Empezar por la preparación del examen y la auditoría de expediente: son los dos que se venden sin comprometer el trámite completo y alimentan el embudo.</p></li>
          <li><p class="when">Mes 2</p><strong>Medir y revisar</strong><p>Tasa de cierre por nivel, tiempo medio por caso y número de requerimientos. Si la Integral a $5,900 mantiene la tasa de cierre del mes anterior, el precio anterior estaba regalado.</p></li>
        </ol>

        <div class="callout">
          <span class="label">Una prueba antes de subir todo</span>
          <p>Si prefiere moverse con cautela: mantenga la Esencial y suba solo la Integral a $5,900 durante 30 días. Con 8 a 10 consultas se ve si la tasa de cierre se mueve. Si cae más de 15 puntos, vuelva a $5,500 y compense con servicios sueltos.</p>
        </div>
      </section>

      <section class="sec" id="fuentes">
        <div class="sec-head">
          <div class="num">Fuentes</div>
          <h2>De dónde sale cada <em>cifra</em></h2>
        </div>
        <ul class="src">
          <li><strong>Tarifa de Honorarios Profesionales Mínimos de los Abogados de la República de Panamá</strong> (Acuerdo 609-A): «4.2.1.3 Naturalización — B/.3,500»; consulta verbal con examen de documentos, B/.150/hora. <a href="https://www.organojudicial.gob.pa/uploads/wp_repo/uploads/2010/12/tarifas_abogados.pdf" target="_blank" rel="noopener">organojudicial.gob.pa</a></li>
          <li><strong>Vida Pública Panamá</strong> (marzo de 2026): gastos del Estado ≈ B/.2,100; honorarios de mercado B/.4,500–6,000; total B/.6,300–7,840. <a href="https://panama.vidapublica.co/naturalizacion-panama-requisitos/" target="_blank" rel="noopener">panama.vidapublica.co</a></li>
          <li><strong>Kery Cruz</strong>: honorarios B/.3,990 en tres pagos (50/25/25) más gastos estimados. <a href="https://www.kerycruz.com/es/naturalizacion" target="_blank" rel="noopener">kerycruz.com</a></li>
          <li><strong>Kraemer &amp; Kraemer</strong>: honorario base $5,000; total $6,300 con gastos del Estado. <a href="https://kraemerlaw.com/en/immigration/panamanian-citizenship/naturalization/" target="_blank" rel="noopener">kraemerlaw.com</a></li>
          <li><strong>Studio Panamá Italia</strong>: $2,000 por tramo (total $6,000) más gastos; total estimado $7,500–7,950. <a href="https://studiopanamaitalia.com/en/panama/migratorio/cittadinanza-a-panama/" target="_blank" rel="noopener">studiopanamaitalia.com</a></li>
          <li><strong>Chen Lee y Asociados</strong>: lista de honorarios, naturalización $3,000. <a href="https://www.chenleeyasociados.com/ssl/order/order.html" target="_blank" rel="noopener">chenleeyasociados.com</a></li>
          <li><strong>Legalys</strong>: naturalización $3,500 + $300 en gastos. <a href="https://panama.legalys.com/en" target="_blank" rel="noopener">panama.legalys.com</a> · su guía menciona honorarios de $3,500 a $8,000 y tasas de $300 a $700.</li>
          <li><strong>Panamá América</strong>: cerca de mil cartas en trámite; Colombia, Venezuela y España como principales países de origen. <a href="https://www.panamaamerica.com.pa/sociedad/alrededor-mil-cartas-naturalizacion-estan-en-tramites-en-servicio-nacional-migracion" target="_blank" rel="noopener">panamaamerica.com.pa</a></li>
          <li><strong>Panamizate</strong>: más de 4,000 expedientes pendientes de firma (agosto de 2024); plazos de hasta nueve años reportados. <a href="https://panamizate.com/en/guide/panamanian-citizenship/" target="_blank" rel="noopener">panamizate.com</a></li>
        </ul>
        <p class="disclaimer">Los precios de competidores se tomaron de sus sitios y publicaciones públicas en noviembre de 2026 y pueden variar. Este documento es un análisis interno de fijación de precios; no constituye asesoría legal ni contable, y las horas por caso son un supuesto de trabajo que debe validarse con el registro real del despacho.</p>
      </section>

    </article>
  </div>
</main>
"""


def main():
    css = (CSS.replace("__FONT_INTER__", FONT_INTER)
              .replace("__FONT_PLAYFAIR_IT__", FONT_PLAYFAIR_IT)
              .replace("__FONT_PLAYFAIR__", FONT_PLAYFAIR)) + EXTRA_CSS

    html = head(
        "Análisis de mercado y honorarios · Naturalización panameña | Naturalízate.pa",
        "Comparación de honorarios de siete despachos, mínimo del baremo, gastos del Estado y propuesta de estructura de precios para la naturalización panameña. Documento interno.",
        "analisis-mercado-honorarios.html")

    html += BODY.replace("{SITE}", SITE).replace("{WA}", WA)
    html += footer(SITE).replace(
        "Requisitos de la Carta de Naturaleza, organizados numeral por numeral. Documento de trabajo del despacho, con la marca de Naturalízate.pa.",
        "Análisis interno de mercado y estructura de honorarios para la naturalización panameña. Documento de trabajo del despacho.")
    html += "</body>\n</html>\n"

    html = (html.replace("__CSS__", css)
                .replace("__LOGO_NAVY__", LOGO_NAVY)
                .replace("__LOGO_WHITE__", LOGO_WHITE))

    OUT.write_text(html, encoding="utf-8")
    print(f"OK → {OUT.name} ({OUT.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
