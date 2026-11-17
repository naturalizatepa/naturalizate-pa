#!/usr/bin/env python3
"""
Ficha de caso: REQUISITOS PARA UNA AMA DE CASA (solicitante dependiente).
Reutiliza el sistema de diseño de build_requisitos.py (mismo brand book).

Salida: requisitos-ama-de-casa.html
Uso:    python3 build_requisitos_dependiente.py
"""
from build_requisitos import (
    CSS, FONT_INTER, FONT_PLAYFAIR, FONT_PLAYFAIR_IT, LOGO_NAVY, LOGO_WHITE,
    SITE, WA, TEL_DEPTO, FUENTE, head, topbar, nav, footer, ROOT,
)

OUT = ROOT / "requisitos-ama-de-casa.html"

EXTRA_CSS = """
  .lead-box{max-width:820px;margin:0 auto 34px;background:var(--g50);border:1px solid var(--g200);
    border-left:3px solid var(--navy);border-radius:8px;padding:24px 26px;}
  .lead-box .label{display:block;font-size:.68rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--g600);margin-bottom:8px;}
  .lead-box p{font-size:1rem;margin:0;color:var(--g700);}
  .lead-box strong{color:var(--navy);}

  .ficha-body h4.sub{font-size:.72rem;font-weight:700;letter-spacing:1.8px;text-transform:uppercase;
    color:var(--navy-2);margin:24px 0 8px;padding:0;border:0;}
  .ficha ul.req li small{display:block;color:var(--g600);font-size:.84rem;margin-top:3px;}
  .dos{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:18px 0 0;}
  @media (max-width:720px){.dos{grid-template-columns:1fr;}}
  .esc{border:1px solid var(--g200);border-radius:8px;padding:20px 20px 18px;background:#fff;}
  .esc .k{font-size:.66rem;font-weight:700;letter-spacing:1.8px;text-transform:uppercase;color:var(--g600);margin-bottom:6px;}
  .esc h5{font-family:var(--serif);font-size:1.05rem;font-weight:600;color:var(--navy);line-height:1.3;margin-bottom:10px;}
  .esc ul{list-style:none;}
  .esc li{position:relative;padding:6px 0 6px 18px;font-size:.89rem;border-bottom:1px solid var(--g200);}
  .esc li:last-child{border-bottom:none;}
  .esc li::before{content:"·";position:absolute;left:4px;color:var(--navy);font-weight:700;}
  .esc .foot{margin-top:10px;font-size:.78rem;color:var(--g600);}
  .mini{max-width:940px;margin:22px auto;border:1px solid var(--g200);border-radius:8px;overflow:hidden;}
  .mini table{min-width:520px;font-size:.88rem;}
  .mini td:first-child{white-space:nowrap;font-weight:600;color:var(--navy);width:1%;}
  .checklist.compact li{padding:9px 0;font-size:.92rem;}
  @media print{
    .notas,.lead-box,.mini{page-break-inside:avoid;}
    /* las dos vías caben juntas en la misma página al imprimir */
    .dos{grid-template-columns:1fr 1fr;gap:10px;page-break-inside:avoid;}
    .esc{padding:12px 12px 10px;}
    .esc h5{font-size:10.5pt;margin-bottom:6px;}
    .esc li{font-size:8.4pt;padding:3px 0 3px 14px;}
    .esc .k{font-size:6.6pt;}
    .esc .foot{font-size:7pt;margin-top:6px;}
    .ficha ul.req li{page-break-inside:avoid;}
    .ficha-body h4{page-break-after:avoid;}
    .sec-head{page-break-inside:avoid;page-break-after:avoid;}
    .sec>p{page-break-before:avoid;}
    .chips{page-break-inside:avoid;}
  }
"""

HTML_BODY = """
<section class="hero">
  <div class="wrap">
    <img class="hero-logo" src="data:image/svg+xml;base64,__LOGO_WHITE__" alt="Naturalízate.pa" width="196" height="26" />
    <div class="kicker">Caso · Solicitante dependiente · Ama de casa</div>
    <h1>Ama de casa: los requisitos para naturalizarse <em>sin ingresos propios</em></h1>
    <p class="lead">La ley no exige que la solicitante tenga ingresos: exige que los acredite un responsable y que exista un vínculo familiar comprobable. Esta ficha reúne los documentos de esa vía y los que se suman del expediente general.</p>
    <div class="byline">
      <span>Preparado por <strong>Lic. Alfonso Villarreal</strong></span>
      <span>·</span>
      <span>Fuente: NAT 2-1, numeral 6 (dependientes)</span>
    </div>
    <div class="hero-cta">
      <a class="btn btn-white" href="#ficha">Ver los requisitos</a>
      <a class="btn btn-outline-w" href="{WA}" target="_blank" rel="noopener">Consultar mi caso</a>
    </div>
  </div>
</section>

<main>
  <div class="wrap">

    <div class="lead-box">
      <span class="label">En una frase</span>
      <p>Una ama de casa se naturaliza con <strong>la solvencia de un responsable</strong> —normalmente el cónyuge—, una <strong>carta de responsabilidad</strong>, la <strong>prueba del vínculo</strong> entre ambas y el resto del expediente que aplica a cualquier solicitante. No presenta ingresos propios.</p>
    </div>

    <div class="article">
      <section class="ficha" id="ficha" style="margin-top:0;">
        <div class="ficha-head">
          <div class="fnum">Ficha de caso · solicitante dependiente</div>
          <h3>Requisitos para una ama de casa</h3>
          <div class="legal">Artículo 10 de la Constitución Política · documento NAT 2-1, numeral 6 (apartado «en caso de que el solicitante sea dependiente») · numerales 1 a 14 del expediente general</div>
        </div>

        <div class="ficha-body">
          <p>El documento oficial trata a la ama de casa como <strong>solicitante dependiente</strong>, junto con el estudiante. La solvencia económica no se acredita con ingresos de la solicitante, sino con los de la persona responsable, y se exige además demostrar el vínculo con esa persona.</p>

          <h4>1 · Documentos propios de la solicitud como dependiente</h4>
          <ul class="req">
            <li>Carta de responsabilidad, con presentación personal o notariada.
              <small>La firma el responsable; conviene notariarla para evitar requerimientos.</small></li>
            <li>Copia autenticada y timbrada de la cédula del responsable o de su carné de residente permanente, según sea el caso.
              <small>B/.2.00 en timbres.</small></li>
            <li>Solvencia económica del responsable: dos (2) de las opciones del bloque 2.</li>
            <li>Paz y salvo de la DGI del responsable.
              <small>El documento oficial lo exige de forma expresa en la lista de dependientes.</small></li>
            <li>Comprobación de vínculos con el responsable (bloque 3).</li>
          </ul>

          <h4>2 · Solvencia económica del responsable · dos (2) de estas opciones</h4>
          <p style="font-size:.92rem;margin:0 0 4px;">No se presentan todas: se eligen <strong>dos</strong> y se presentan completas. Deben corresponder al responsable, no a la solicitante.</p>
          <ul class="req">
            <li>Declaración de renta de los dos (2) años anteriores al de la presentación, con certificado de recepción y su respectivo recibo de pago.
              <small>Si es copia, debe venir notariada; firmada por Contador Público Autorizado y autenticada por notario.</small></li>
            <li>Carta bancaria de cuatro (4) cifras medias en adelante, firmada y con sello fresco.
              <small>Dirigida al Servicio Nacional de Migración; 30 días de vigencia.</small></li>
            <li>Carta de trabajo del responsable con su ficha de la Caja de Seguro Social notariada.
              <small>La ficha debe estar actualizada, con el carné de residente permanente del responsable.</small></li>
            <li>Certificación de jubilación, cuando el responsable esté pensionado.</li>
            <li>Propiedad inmobiliaria a nombre del responsable, de una sociedad o de una fundación cuyo beneficiario final sea él.</li>
            <li>Capital invertido en un negocio: documentos que prueben que opera (declaraciones de renta, permiso de operación), acciones o participación con el responsable como beneficiario final.</li>
            <li>Paz y salvo de la DGI del responsable.</li>
          </ul>

          <h4>3 · Comprobación del vínculo con el responsable</h4>
          <ul class="req">
            <li>Certificado de matrimonio. Si se celebró en el extranjero, debe estar inscrito en la Dirección Nacional del Registro Civil de Panamá.</li>
            <li>Si el responsable fuese el padre o la madre de la solicitante, solo procede cuando esta tiene entre dieciocho (18) y veinticinco (25) años, estudia de forma regular y depende económicamente de él o de ella.</li>
          </ul>

          <div class="chips">
            <span class="chip">Cédula del responsable: B/.2.00 en timbres</span>
            <span class="chip">Carta bancaria: 30 días</span>
            <span class="chip">Dos de las opciones de solvencia</span>
          </div>
        </div>

        <div class="notas">
          <span class="label">Criterio del despacho · no forma parte del documento oficial</span>
          <ul>
            <li>La solvencia del responsable se puede sostener en el tiempo: el trámite dura meses, así que conviene elegir pruebas que no venzan antes de la presentación.</li>
            <li>Si el matrimonio se celebró fuera de Panamá y aún no está inscrito en el Registro Civil, esa inscripción es el primer paso: sin ella el vínculo no se acredita.</li>
            <li>Cuando el responsable es el cónyuge residente, la solicitante suele además necesitar la certificación de estatus migratorio (numeral 11) para acreditar los años de residencia.</li>
          </ul>
        </div>
      </section>

      <section class="sec" id="via">
        <div class="sec-head">
          <div class="num">Según su vía</div>
          <h2>Cambia el tiempo de residencia y <em>algunos certificados</em></h2>
        </div>
        <p>Ser ama de casa no define la vía constitucional: la define el vínculo y la nacionalidad del cónyuge. Los requisitos de dependencia del bloque 1 se mantienen; lo que cambia es el tiempo de residencia y los certificados familiares.</p>

        <div class="dos">
          <div class="esc">
            <div class="k">Vía del numeral 2</div>
            <h5>Casada con un panameño</h5>
            <ul>
              <li>Tres (3) años de residencia permanente ininterrumpida.</li>
              <li>Certificado de matrimonio (B/.3.00 en timbres).</li>
              <li>Certificado de nacimiento del cónyuge panameño (B/.3.00).</li>
              <li>Certificados de nacimiento de los hijos panameños, si los hay (B/.3.00).</li>
              <li>Certificado de inscripción de naturalización, si el cónyuge es naturalizado (B/.3.00).</li>
            </ul>
            <div class="foot">Numerales 5 y 6 del documento oficial.</div>
          </div>
          <div class="esc">
            <div class="k">Vía general</div>
            <h5>Casada con un residente permanente extranjero</h5>
            <ul>
              <li>Cinco (5) años de residencia permanente ininterrumpida.</li>
              <li>No se presentan los certificados familiares del numeral 5.</li>
              <li>Se mantiene la solvencia por dependencia del bloque 1.</li>
              <li>Se acredita la residencia con la certificación de estatus migratorio.</li>
            </ul>
            <div class="foot">Numerales 1, 3, 4, 6, 8 y 11 del documento oficial.</div>
          </div>
        </div>

        <div class="callout info">
          <span class="label">Si el cónyuge aún no es residente permanente</span>
          <p>La solicitud exige que la solicitante tenga residencia permanente propia. Si su condición migratoria es de dependiente del cónyuge y no de residente permanente, primero hay que resolver esa situación: sin Cédula E no corre el tiempo que la naturalización exige.</p>
        </div>
      </section>

      <section class="sec" id="resto">
        <div class="sec-head">
          <div class="num">Expediente completo</div>
          <h2>Lo demás también <em>aplica</em></h2>
        </div>
        <p>La dependencia económica solo sustituye la prueba de ingresos. El resto de los numerales se presenta igual que en cualquier solicitud:</p>

        <div class="mini table-wrap">
          <table>
            <thead><tr><th scope="col">No.</th><th scope="col">Documento</th></tr></thead>
            <tbody>
              <tr><td>01</td><td>Poder y solicitud mediante abogado, con declaración jurada ante notario (B/.8.00 en timbres, 1 año de vigencia).</td></tr>
              <tr><td>02</td><td>Acreditación de ausencia de antecedentes penales en el país de residencia de los últimos años o en el país de origen.</td></tr>
              <tr><td>03</td><td>Antecedentes penales de Panamá, a nombre de la solicitante, con carné de residente permanente y uso de naturalización (30 días).</td></tr>
              <tr><td>04</td><td>Copia del carné de residente permanente autenticada por el Tribunal Electoral (B/.2.00).</td></tr>
              <tr><td>05</td><td>Certificados familiares: matrimonio, nacimiento del cónyuge y de los hijos panameños, según la vía.</td></tr>
              <tr><td>07</td><td>Formato de entrevista de naturalización, completado a mano con bolígrafo azul.</td></tr>
              <tr><td>08</td><td>Paz y salvo de la DGI de la solicitante.</td></tr>
              <tr><td>09</td><td>Copia completa del pasaporte, con sello de registro de extranjería, autenticada y traducida si corresponde.</td></tr>
              <tr><td>10</td><td>Certificado médico general de buena salud (90 días).</td></tr>
              <tr><td>11</td><td>Certificación de estatus migratorio para uso de naturalización (B/.8.00, 90 días).</td></tr>
              <tr><td>13</td><td>Fotos tamaño carné 3.5 × 4.5 cm, con vestido formal.</td></tr>
              <tr><td>14</td><td>Examen de conocimientos básicos del Tribunal Electoral, salvo exoneración acreditada.</td></tr>
            </tbody>
          </table>
        </div>
        <p class="disclaimer" style="margin-top:14px;">El numeral 12 (ley de reciprocidad) solo aplica si la solicitud se fundamenta en el numeral 3 del artículo 10.</p>
      </section>

      <section class="sec" id="checklist">
        <div class="sec-head">
          <div class="num">Control</div>
          <h2>Checklist de la <em>dependiente</em></h2>
        </div>
        <ul class="checklist compact">
          <li><span>1</span><span>Carta de responsabilidad (presentación personal o notariada).</span></li>
          <li><span>2</span><span>Copia autenticada y timbrada (B/.2.00) de la cédula o carné de residente del responsable.</span></li>
          <li><span>3</span><span>Dos (2) pruebas de solvencia del responsable, completas y vigentes.</span></li>
          <li><span>4</span><span>Paz y salvo de la DGI del responsable.</span></li>
          <li><span>5</span><span>Certificado de matrimonio inscrito en el Registro Civil de Panamá.</span></li>
          <li><span>6</span><span>Certificados familiares de la vía (numeral 5), si aplica.</span></li>
          <li><span>7</span><span>Certificación de estatus migratorio de la solicitante.</span></li>
          <li><span>8</span><span>Poder, solicitud y declaración jurada ante notario.</span></li>
          <li><span>9</span><span>Antecedentes penales de Panamá y del exterior, según corresponda.</span></li>
          <li><span>10</span><span>Paz y salvo de la DGI de la solicitante.</span></li>
          <li><span>11</span><span>Pasaporte completo, autenticado y traducido si aplica.</span></li>
          <li><span>12</span><span>Certificado médico, fotos y formato de entrevista.</span></li>
        </ul>
      </section>

      <section class="sec">
        <div class="sec-head">
          <div class="num">Fuente</div>
          <h2>De dónde sale esta <em>ficha</em></h2>
        </div>
        <p>Los bloques 1, 2 y 3 transcriben el apartado de dependientes del numeral 6 de <strong>__FUENTE__</strong>. El resto proviene de los numerales 1 a 14 del mismo documento. El orden, los avisos de vigencia y los criterios del despacho son aportes de Naturalízate.pa.</p>
        <p class="disclaimer">Aviso legal: documento de trabajo con fines informativos. El documento oficial prevalece; requisitos, timbres y vigencias pueden cambiar y deben confirmarse con el Departamento de Naturalización (Tel. __TEL__) o con su abogado al momento de presentar. No constituye asesoría legal para un caso particular y no garantiza resultados.</p>
      </section>
    </div>
  </div>

  <section class="final">
    <div class="wrap">
      <div class="eyebrow">Revisión previa · sin costo</div>
      <h2>¿Su caso es de dependencia? <em>Conviene confirmarlo antes de reunir papeles.</em></h2>
      <p>Revisamos el vínculo, la solvencia del responsable y la vía constitucional aplicable, y le indicamos por escrito qué falta antes de presentar.</p>
      <div class="hero-cta">
        <a class="btn btn-white" href="{SITE}">Solicitar revisión</a>
        <a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">Hablar por WhatsApp</a>
      </div>
    </div>
  </section>
</main>
"""


def main():
    css = (CSS.replace("__FONT_INTER__", FONT_INTER)
              .replace("__FONT_PLAYFAIR_IT__", FONT_PLAYFAIR_IT)
              .replace("__FONT_PLAYFAIR__", FONT_PLAYFAIR)) + EXTRA_CSS

    html = head(
        "Requisitos para una ama de casa · Naturalización panameña | Naturalízate.pa",
        "Ama de casa solicitante dependiente: carta de responsabilidad, solvencia del responsable (2 de 7 opciones), comprobación del vínculo y el resto del expediente. NAT 2-1, numeral 6.",
        "requisitos-ama-de-casa.html")

    html += topbar()
    html += nav("requisitos-carta-de-naturaleza.html", "Consultar mi caso")
    body = (HTML_BODY.replace("{WA}", WA)
                     .replace("{SITE}", SITE)
                     .replace("__FUENTE__", FUENTE)
                     .replace("__TEL__", TEL_DEPTO))
    html += body
    html += footer("requisitos-carta-de-naturaleza.html").replace(
        "Requisitos de la Carta de Naturaleza, organizados numeral por numeral. Documento de trabajo del despacho, con la marca de Naturalízate.pa.",
        "Requisitos para una solicitante dependiente (ama de casa). Documento de trabajo del despacho, con la marca de Naturalízate.pa.")
    html += "</body>\n</html>\n"

    html = (html.replace("__CSS__", css)
                .replace("__LOGO_NAVY__", LOGO_NAVY)
                .replace("__LOGO_WHITE__", LOGO_WHITE))

    OUT.write_text(html, encoding="utf-8")
    print(f"OK → {OUT.name} ({OUT.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
