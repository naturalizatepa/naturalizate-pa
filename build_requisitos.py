#!/usr/bin/env python3
"""
Genera el documento de REQUISITOS DE LA CARTA DE NATURALEZA (NAT 2-1, Migración)
con la marca de Naturalízate.pa:

  · requisitos-carta-de-naturaleza.html   → documento maestro (índice + 14 fichas)
  · fichas/numeral-01.html … 14.html      → una ficha independiente por numeral
  · requisitos-fichas-numerales.zip       → las 14 fichas + índice, para enviar

Uso: python3 build_requisitos.py
"""
import base64
import pathlib
import zipfile

ROOT = pathlib.Path(__file__).parent
OUT_MASTER = ROOT / "requisitos-carta-de-naturaleza.html"
DIR_FICHAS = ROOT / "fichas"
ZIP_PATH = ROOT / "requisitos-fichas-numerales.zip"


def b64(p):
    return base64.b64encode(p.read_bytes()).decode("ascii")


FONT_INTER = b64(ROOT / "fonts/inter-latin-wght-normal.woff2")
FONT_PLAYFAIR = b64(ROOT / "fonts/playfair-display-latin-wght-normal.woff2")
FONT_PLAYFAIR_IT = b64(ROOT / "fonts/playfair-display-latin-wght-italic.woff2")
LOGO_NAVY = b64(ROOT / "svg/logo-principal-navy.svg")
LOGO_WHITE = b64(ROOT / "svg/logo-principal-blanco.svg")

SITE = "https://naturalizatepa.github.io/naturalizate-pa/"
WA = ("https://wa.me/50762557583?text=Hola%2C%20necesito%20revisar%20los%20requisitos"
      "%20de%20mi%20solicitud%20de%20Carta%20de%20Naturaleza.")
FUENTE = ("Servicio Nacional de Migración · «Requisitos de solicitud de Carta de Naturaleza», "
          "documento NAT 2-1 (abril de 2026)")
TEL_DEPTO = "520-1264"

# --------------------------------------------------------------------------------------
# CONTENIDO: transcripción organizada del documento oficial, numeral por numeral
# --------------------------------------------------------------------------------------
NUMERALES = [
    {
        "n": 1,
        "title": "Poder y solicitud mediante abogado",
        "legal": "Artículo 10, numerales 1, 2 y 3 de la Constitución Política · Título XIII, Capítulo II · Decreto Ley 3 de 22 de febrero de 2008",
        "intro": "El poder y la solicitud se dirigen al Excelentísimo Presidente de la República. El resto de la documentación se dirige al Servicio Nacional de Migración.",
        "groups": [
            {"h": "Poder", "items": [
                "Nombre completo del peticionario(a), tal como aparece en el pasaporte, el estatus migratorio y el carné de residente permanente.",
                "Dirección completa de domicilio del peticionario(a).",
                "Sexo, edad y estado civil del peticionario(a).",
                "Lugar de nacimiento y nacionalidad (de origen o adquirida) del peticionario(a).",
                "Número de carné de residente permanente del peticionario(a).",
                "Número de pasaporte del peticionario(a).",
                "Correo electrónico y números telefónicos del peticionario(a) y del abogado(a).",
                "Nombres y nacionalidad de los padres del peticionario(a), como aparecen en el estatus migratorio.",
                "Renuncia expresa e irrevocable a la nacionalidad (de origen o adquirida) del peticionario(a).",
                "Manifestación del deseo libre y espontáneo de acogerse a la nacionalidad panameña.",
            ]},
            {"h": "Solicitud", "items": [
                "Nombre del abogado con todas sus generales (dirección completa, teléfonos y correo electrónico), sustentada con hechos y pruebas respectivas.",
                "Fundamento de derecho en el que se especifique el numeral (1, 2 o 3) del artículo 10 de la Constitución Política que sirve de base a la solicitud, y el Decreto Ley 3 de 22 de febrero de 2008.",
                "Constancia de servicio público: luz, agua, contrato de arriendo u otros.",
                "Copia de la cédula e idoneidad del abogado, o carné de idoneidad del abogado.",
                "Autorización notariada (copia del carné de trabajo o cédula del autorizado).",
            ]},
            {"h": "Declaración jurada", "items": [
                "Motivos o razones de la petición.",
                "Renuncia expresa e irrevocable a la nacionalidad (de origen o adquirida).",
                "Manifestación del deseo libre y espontáneo de acogerse a la nacionalidad panameña.",
                "Mención del artículo 385 del Código Penal.",
                "Huella del peticionario(a).",
                "Se otorga ante notario y en papel.",
            ]},
        ],
        "chips": ["B/.8.00 en timbres", "1 año de vigencia"],
        "notas": [
            "Los datos del poder deben coincidir literalmente con el pasaporte, el estatus migratorio y el carné de residente permanente. Una diferencia de nombre o de número de carné obliga a rehacer el poder.",
            "La declaración jurada se firma ante notario: conviene coordinarla junto con el poder para no repetir la visita.",
        ],
        "resumen": "Poder, solicitud y declaración jurada ante notario",
    },
    {
        "n": 2,
        "title": "Acreditación de ausencia de antecedentes penales",
        "legal": "Artículo 10 de la Constitución Política · documento NAT 2-1, numeral 2",
        "intro": "Se debe acreditar la ausencia de antecedentes penales en el país de residencia de los últimos cinco años o en el país de origen, según sea el caso.",
        "groups": [
            {"h": "Regla general", "items": [
                "Antecedentes penales del país de residencia de los últimos cinco años o del país de origen, según corresponda al numeral invocado.",
                "Los documentos emitidos en el exterior deben presentarse autenticados o apostillados y traducidos al español cuando corresponda.",
            ]},
            {"h": "Excepción por permanencia continua", "items": [
                "Si la persona no ha salido del país por más de tres meses en los últimos cinco, tres o dos años —según el numeral correspondiente—, puede acreditar la ausencia de antecedentes penales mediante una declaración jurada que lo justifique.",
                "La declaración jurada debe explicar de forma expresa esa permanencia continua en el territorio nacional.",
            ]},
        ],
        "chips": [],
        "notas": [
            "El numeral aplicable (1, 2 o 3) define el período que se revisa: no es lo mismo cinco, tres o dos años. Verifique primero su vía, y después solicite el antecedente con ese alcance.",
            "Si su historial migratorio muestra ausencias, la excepción de permanencia continua no aplica: se exige el antecedente del país donde estuvo.",
        ],
        "resumen": "Antecedentes penales del país de residencia u origen",
    },
    {
        "n": 3,
        "title": "Antecedentes penales de Panamá",
        "legal": "Documento NAT 2-1, numeral 3",
        "intro": "Certificación de antecedentes penales emitida en Panamá, con los datos del peticionario y el uso declarado.",
        "groups": [
            {"h": "Contenido exigido", "items": [
                "Nombre completo del peticionario(a).",
                "Número de carné de residente permanente.",
                "Para uso de Migración o Naturalización.",
            ]},
        ],
        "chips": ["30 días de vigencia"],
        "notas": [
            "Es uno de los documentos con vigencia más corta: se solicita cuando el expediente ya está listo para presentarse, no al inicio del armado.",
            "Verifique que el certificado diga expresamente «Naturalización» o «Migración» en el uso; un certificado genérico puede ser devuelto.",
        ],
        "resumen": "Antecedentes penales de Panamá",
    },
    {
        "n": 4,
        "title": "Copia del carné de residente permanente",
        "legal": "Documento NAT 2-1, numeral 4",
        "intro": "Copia del carné de residente permanente autenticada por el Tribunal Electoral.",
        "groups": [
            {"h": "Documento", "items": [
                "Copia del carné de residente permanente (Cédula E).",
                "Autenticada por el Tribunal Electoral.",
            ]},
        ],
        "chips": ["B/.2.00 en timbres"],
        "notas": [
            "La autenticación es del Tribunal Electoral, no del notario. Es un error frecuente presentar una copia notariada cuando el documento exige autenticación del Tribunal.",
            "Revise también la vigencia de su carné: si está próximo a vencer, conviene renovarlo antes de presentar.",
        ],
        "resumen": "Copia del carné autenticada por el Tribunal Electoral",
    },
    {
        "n": 5,
        "title": "Certificado de matrimonio y vínculos familiares",
        "legal": "Artículo 10, numeral 2 de la Constitución Política · documento NAT 2-1, numeral 5",
        "intro": "Documentación que acredita el vínculo familiar panameño, aplicable a las solicitudes por matrimonio o por hijos panameños.",
        "groups": [
            {"h": "Para el numeral 2", "items": [
                "Certificado de matrimonio (B/.3.00 en timbres).",
                "Certificado de nacimiento del cónyuge (B/.3.00 en timbres).",
                "Certificado de nacimiento de hijos panameños y certificado de nacimiento de la madre o el padre panameño (B/.3.00 en timbres).",
                "Certificado de inscripción de naturalización (B/.3.00 en timbres) cuando el cónyuge, padre o madre sea naturalizado.",
            ]},
            {"h": "Regla de forma", "items": [
                "Toda la documentación aportada deberá llevar el nombre completo del peticionario(a).",
                "Los certificados emitidos en el extranjero deben estar inscritos en la Dirección Nacional del Registro Civil de Panamá y presentarse con las autenticaciones que correspondan.",
            ]},
        ],
        "chips": ["B/.3.00 en timbres por certificado"],
        "notas": [
            "Este numeral solo tiene sentido si su vía es la del numeral 2 (cónyuge o hijos panameños). En la vía general no se presenta.",
            "El certificado de inscripción de naturalización se pide en el Registro Civil y suele tardar: inícielo con antelación.",
        ],
        "resumen": "Certificados de matrimonio, nacimiento y naturalización",
    },
    {
        "n": 6,
        "title": "Solvencia económica",
        "legal": "Documento NAT 2-1, numeral 6",
        "intro": "La solvencia se prueba con dos (2) de las opciones siguientes. No se exigen todas: se eligen dos y se presentan correctamente.",
        "groups": [
            {"h": "Opción A · Declaración de renta", "items": [
                "Declaración de renta de los dos (2) años anteriores al de la presentación.",
                "Con certificado de recepción y su respectivo recibo de pago.",
                "Si es copia, debe venir notariada.",
                "Firmada por Contador Público Autorizado y debidamente autenticada por un notario.",
            ]},
            {"h": "Opción B · Carta bancaria", "items": [
                "Dirigida al Servicio Nacional de Migración.",
                "De cuatro (4) cifras medias en adelante.",
                "Firmada y con sello fresco del banco.",
            ]},
            {"h": "Opción C · Carta de trabajo con ficha de la CSS", "items": [
                "Dirigida al Servicio Nacional de Migración.",
                "Nombre completo del solicitante con su identificación (carné de residente permanente).",
                "En papel membretado de la empresa.",
                "Firmada por el representante legal o el jefe de Recursos Humanos; si la firma es digital, con sello fresco de la empresa.",
                "Debe certificar el cargo, el salario y las deducciones.",
                "Ficha de la Caja de Seguro Social actualizada, con nueve (09) cuotas, que contenga el carné de residente permanente del solicitante y esté notariada.",
            ]},
            {"h": "Otras opciones admitidas", "items": [
                "Certificación de jubilación, según sea el caso.",
                "Por inversión · propiedad inmobiliaria: constancia de propiedad del bien inmueble a nombre del titular, o de una sociedad o fundación cuyo beneficiario final sea el solicitante.",
                "Por inversión · capital en un negocio: documentos que demuestren que el negocio está operando (declaraciones de renta, permiso de operación), acciones o participación que indique que el beneficiario final es el solicitante.",
            ]},
            {"h": "Si el solicitante es dependiente (ama de casa o estudiante)", "items": [
                "Carta de responsabilidad (presentación personal o notariada).",
                "Copia autenticada y timbrada (B/.2.00) de la cédula o del carné de residente permanente del responsable, según sea el caso.",
                "Solvencia económica del responsable: dos de las opciones anteriores.",
                "Paz y salvo de la DGI del responsable.",
                "Comprobación de vínculos: certificado de matrimonio en el extranjero, inscrito en la Dirección Nacional del Registro Civil de Panamá.",
                "El padre o la madre solo puede ser responsable si el solicitante es mayor de dieciocho (18) años y hasta los veinticinco (25) años, estudia de forma regular y depende económicamente del residente o nacional.",
            ]},
        ],
        "chips": ["Carta bancaria: 30 días", "Ficha CSS: 90 días y notariada", "9 cuotas de CSS"],
        "notas": [
            "Elija las dos pruebas que su situación real pueda sostener a largo plazo: el proceso dura meses y un documento con fecha vieja obliga a repetirlo.",
            "La ficha de la CSS debe reflejar nueve cuotas y el número de carné de residente permanente del solicitante. Es el punto donde más expedientes se devuelven.",
            "Si es dependiente, la solvencia del responsable se evalúa con la misma regla de dos de tres; conviene revisar ambas fichas a la vez.",
        ],
        "resumen": "Dos (2) de las opciones de solvencia",
    },
    {
        "n": 7,
        "title": "Formato de entrevista de naturalización",
        "legal": "Documento NAT 2-1, numeral 7",
        "intro": "Formulario oficial de entrevista, completado por el solicitante y adjuntado al expediente.",
        "groups": [
            {"h": "Cómo se completa", "items": [
                "Descargar el formato desde el sitio web del Servicio Nacional de Migración.",
                "Completado por el solicitante con bolígrafo de color azul, letra imprenta y legible.",
                "El formulario debe ser llenado por el interesado, no por un tercero.",
                "Con la finalidad de ser mejor evaluado, aportar los requisitos que se indican en el propio formulario de entrevista.",
            ]},
        ],
        "chips": [],
        "notas": [
            "El formato se completa a mano: no se acepta llenado digital ni con otro color de tinta.",
            "Los requisitos que el formulario menciona son parte de la evaluación de la entrevista. Léalos antes de completarlo, no después.",
        ],
        "resumen": "Formato de entrevista completado a mano",
    },
    {
        "n": 8,
        "title": "Paz y salvo de la DGI",
        "legal": "Documento NAT 2-1, numeral 8",
        "intro": "Certificación de paz y salvo emitida por la Dirección General de Ingresos.",
        "groups": [
            {"h": "Contenido exigido", "items": [
                "Nombre completo del peticionario(a).",
                "Número de carné de residente permanente.",
                "Número de confirmación, nombre y firma.",
            ]},
        ],
        "chips": [],
        "notas": [
            "Se solicita en la DGI y refleja la situación tributaria del solicitante: si tiene declaraciones pendientes, conviene regularizarlas antes de pedirlo.",
            "Verifique que el documento incluya el número de confirmación; una copia simple sin ese dato puede no ser aceptada.",
        ],
        "resumen": "Paz y salvo de la DGI",
    },
    {
        "n": 9,
        "title": "Copia completa del pasaporte",
        "legal": "Documento NAT 2-1, numeral 9",
        "intro": "Copia íntegra del pasaporte de origen, con el sello de registro de extranjería y las autenticaciones correspondientes.",
        "groups": [
            {"h": "Documento", "items": [
                "Copia completa del pasaporte, donde debe aparecer el sello de registro de extranjería.",
                "Autenticada por el cónsul o la embajada del país correspondiente.",
                "Con certificación del Ministerio de Relaciones Exteriores.",
            ]},
            {"h": "Si el pasaporte no está en español", "items": [
                "Traducir las generales del pasaporte y la hoja de certificación al idioma español.",
            ]},
        ],
        "chips": [],
        "notas": [
            "«Copia completa» significa todas las páginas, no solo la hoja de datos: así se solicita y así se revisa.",
            "La cadena de autenticaciones (consulado y luego Cancillería) depende de terceros y suele ser el trámite más lento del expediente. Inícielo primero.",
        ],
        "resumen": "Pasaporte completo, autenticado y con registro de extranjería",
    },
    {
        "n": 10,
        "title": "Certificado médico general de buena salud",
        "legal": "Documento NAT 2-1, numeral 10",
        "intro": "Certificación de buena salud emitida por un médico, con los datos del peticionario y el registro profesional.",
        "groups": [
            {"h": "Contenido exigido", "items": [
                "Nombre completo del peticionario(a).",
                "Número de carné de residente permanente.",
                "Fecha de emisión.",
                "Sello de registro y firma del doctor.",
            ]},
        ],
        "chips": ["90 días de vigencia"],
        "notas": [
            "Con 90 días de vigencia, se emite cerca de la presentación: no lo solicite al inicio del armado del expediente.",
            "Confirme que el médico incluya su sello de registro y firma: un certificado sin sello no acredita nada.",
        ],
        "resumen": "Certificado médico de buena salud",
    },
    {
        "n": 11,
        "title": "Certificación de estatus migratorio",
        "legal": "Documento NAT 2-1, numeral 11",
        "intro": "Certificación del estatus migratorio emitida por el Servicio Nacional de Migración, para uso de naturalización.",
        "groups": [
            {"h": "Contenido exigido", "items": [
                "Número de carné de residente permanente del peticionario(a).",
                "Para uso de Naturalización.",
            ]},
        ],
        "chips": ["B/.8.00 en timbres", "90 días de vigencia"],
        "notas": [
            "Es la constancia que confirma la categoría y el tiempo de residencia permanente: es la base del cómputo de los años exigidos.",
            "Solicítela cuando ya tenga claras las fechas de su historial; es el documento con el que se verifica la vía aplicable.",
        ],
        "resumen": "Certificación de estatus migratorio para naturalización",
    },
    {
        "n": 12,
        "title": "Ley de reciprocidad",
        "legal": "Artículo 10, numeral 3 de la Constitución Política · documento NAT 2-1, numeral 12",
        "intro": "Documentación que acredita la existencia y vigencia de la ley de reciprocidad del país de origen. Aplica a la vía del numeral 3.",
        "groups": [
            {"h": "Para el numeral 3", "items": [
                "Fotocopia de la ley de reciprocidad debidamente autenticada ante el consulado panameño del país interesado, con certificación del Ministerio de Relaciones Exteriores.",
                "O bien, certificación de existencia y vigencia de la ley de reciprocidad expedida por el consulado del país de origen del interesado acreditado en la República de Panamá, con certificación del Ministerio de Relaciones Exteriores.",
            ]},
        ],
        "chips": [],
        "notas": [
            "Solo aplica si su solicitud se fundamenta en el numeral 3. Si su vía es la general o la familiar, este numeral no se presenta.",
            "Las dos opciones son alternativas: elija la que su consulado pueda emitir más rápido, y no olvide la certificación de Cancillería.",
        ],
        "resumen": "Ley de reciprocidad autenticada y certificada por Cancillería",
    },
    {
        "n": 13,
        "title": "Fotos tamaño carné",
        "legal": "Documento NAT 2-1, numeral 13",
        "intro": "Fotografías recientes con las medidas y el atuendo exigidos.",
        "groups": [
            {"h": "Especificaciones", "items": [
                "Medida: 3.5 cm x 4.5 cm.",
                "Damas: vestido formal, camisa, blazer u otros equivalentes.",
                "Caballeros: formal, con saco y corbata.",
            ]},
        ],
        "chips": ["3.5 × 4.5 cm"],
        "notas": [
            "El requisito de vestimenta es formal y se revisa en la recepción del expediente. Una foto informal obliga a repetirla.",
            "Lleve juegos adicionales: se usan también para el trámite posterior a la jura.",
        ],
        "resumen": "Fotos 3.5 × 4.5 cm con atuendo formal",
    },
    {
        "n": 14,
        "title": "Examen de conocimientos básicos del Tribunal Electoral",
        "legal": "Decreto N° 13 del 1 de agosto de 2025, artículo 1, párrafos tercero y cuarto · documento NAT 2-1, numeral 14",
        "intro": "El examen de conocimientos básicos de la Constitución Política se rinde ante el Tribunal Electoral. La norma prevé exoneraciones y pruebas que deben aportarse.",
        "groups": [
            {"h": "Exoneraciones", "items": [
                "Nacionales de España y de cualquier otro país latinoamericano que acrediten, mediante certificación autenticada, que su país de origen exime a los ciudadanos panameños de este requisito con base en el principio de reciprocidad.",
                "Quienes hayan cursado estudios en escuelas, colegios o universidades —oficiales o particulares— dentro del territorio nacional, sobre las materias exigidas por la Constitución Política.",
                "Personas con discapacidad comprobada mediante certificación de médico idóneo que enfrenten dificultades para realizar el examen: se les aplicará una prueba conforme a sus necesidades individuales, elaborada por la Oficina de Equiparación de Oportunidades del Tribunal Electoral.",
            ]},
            {"h": "Pruebas que se aportan", "items": [
                "Certificación autenticada del país de origen que exime del examen a los panameños, cuando se invoca reciprocidad.",
                "Certificados de créditos o diplomas autenticados de los estudios cursados en el territorio nacional.",
                "Certificado expedido por médico idóneo en los casos de personas con discapacidad.",
            ]},
        ],
        "chips": ["Decreto N° 13 de 1 de agosto de 2025"],
        "notas": [
            "La exoneración por estudios no es automática: hay que aportar créditos o diplomas autenticados y que las materias coincidan con las exigidas por la Constitución.",
            "Si no le aplica ninguna exoneración, el examen se prepara con tiempo. No superarlo retrasa el proceso completo y consume una convocatoria.",
        ],
        "resumen": "Examen del Tribunal Electoral o prueba de exoneración",
    },
]

NOTA_GENERAL = ("Toda la documentación aportada deberá ir con el nombre completo del peticionario(a). "
                f"Departamento de Naturalización · Tel. {TEL_DEPTO}.")

# --------------------------------------------------------------------------------------
# CSS compartido
# --------------------------------------------------------------------------------------
CSS = """
  @font-face { font-family:"Inter"; font-style:normal; font-weight:100 900; font-display:swap;
    src:url(data:font/woff2;base64,__FONT_INTER__) format("woff2"); }
  @font-face { font-family:"Playfair Display"; font-style:normal; font-weight:400 900; font-display:swap;
    src:url(data:font/woff2;base64,__FONT_PLAYFAIR__) format("woff2"); }
  @font-face { font-family:"Playfair Display"; font-style:italic; font-weight:400 900; font-display:swap;
    src:url(data:font/woff2;base64,__FONT_PLAYFAIR_IT__) format("woff2"); }

  :root{
    --navy:#0D1B2A; --navy-deep:#060F17; --navy-2:#1B3A57;
    --white:#FFFFFF; --g50:#F8F9FA; --g100:#F1F3F5; --g200:#E9ECEF; --g300:#DEE2E6;
    --g400:#ADB5BD; --g600:#5C6772; --g700:#495057; --g900:#212529;
    --wa-solid:#0F7A40; --wa-solid-hover:#0B6332;
    --serif:"Playfair Display", Georgia, "Times New Roman", serif;
    --sans:"Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  }
  *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
  html{scroll-behavior:smooth;-webkit-text-size-adjust:100%;}
  body{font-family:var(--sans);color:var(--g700);background:#fff;line-height:1.68;font-size:16.5px;-webkit-font-smoothing:antialiased;}
  a{color:var(--navy-2);text-decoration-color:rgba(27,58,87,.35);text-underline-offset:3px;}
  a:hover{color:var(--navy);text-decoration-color:var(--navy);}
  strong{color:var(--navy);font-weight:600;}
  img{max-width:100%;display:block;}

  .wrap{max-width:1000px;margin:0 auto;padding:0 26px;}
  .measure{max-width:760px;}

  .topbar{background:var(--navy-deep);color:rgba(255,255,255,.78);font-size:.76rem;}
  .topbar .wrap{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;padding-top:8px;padding-bottom:8px;}
  .topbar strong{color:#fff;}
  .topbar a{color:#fff;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.35);}

  .nav{position:sticky;top:0;z-index:90;background:rgba(255,255,255,.97);backdrop-filter:blur(10px);border-bottom:1px solid var(--g200);}
  .nav .wrap{display:flex;align-items:center;justify-content:space-between;height:64px;gap:18px;}
  .nav-logo{width:164px;flex-shrink:0;}
  .nav-links{display:flex;align-items:center;gap:20px;}
  .nav-links a{font-size:.85rem;font-weight:500;color:var(--g700);text-decoration:none;}
  .nav-links a:hover{color:var(--navy);}
  .nav-cta{background:var(--navy);color:#fff!important;padding:9px 16px;border-radius:6px;font-size:.83rem;font-weight:600;white-space:nowrap;}
  .cta-short{display:none;}

  .hero{background:linear-gradient(158deg,var(--navy-deep) 0%,var(--navy) 58%,var(--navy-2) 100%);color:#fff;padding:56px 0 60px;}
  .hero-logo{width:196px;margin-bottom:32px;}
  .kicker{display:inline-flex;align-items:center;gap:11px;font-size:.7rem;font-weight:600;letter-spacing:2.5px;text-transform:uppercase;color:var(--g400);margin-bottom:18px;}
  .kicker::before{content:"";width:28px;height:1px;background:var(--g400);}
  .hero h1{font-family:var(--serif);font-weight:600;font-size:clamp(1.9rem,4.4vw,2.85rem);line-height:1.15;letter-spacing:-.5px;max-width:760px;margin-bottom:18px;}
  .hero h1 em{font-style:italic;font-weight:400;color:#C9D3DC;}
  .hero .lead{font-size:1.03rem;color:rgba(255,255,255,.84);max-width:640px;margin-bottom:22px;}
  .byline{display:flex;flex-wrap:wrap;gap:8px 16px;font-size:.82rem;color:rgba(255,255,255,.66);border-top:1px solid rgba(255,255,255,.14);padding-top:16px;max-width:640px;}
  .byline strong{color:#fff;}
  .hero-cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:26px;}

  .btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:13px 22px;border-radius:6px;font-size:.92rem;font-weight:600;text-decoration:none;border:1.5px solid transparent;transition:background .18s,transform .18s,color .18s;}
  .btn-white{background:#fff;color:var(--navy);}
  .btn-white:hover{background:var(--g100);color:var(--navy);transform:translateY(-1px);}
  .btn-navy{background:var(--navy);color:#fff;}
  .btn-navy:hover{background:var(--navy-2);color:#fff;transform:translateY(-1px);}
  .btn-outline-w{background:transparent;color:#fff;border-color:rgba(255,255,255,.45);}
  .btn-outline-w:hover{border-color:#fff;background:rgba(255,255,255,.08);color:#fff;}
  .btn-wa{background:var(--wa-solid);border-color:var(--wa-solid);color:#fff;}
  .btn-wa:hover{background:var(--wa-solid-hover);border-color:var(--wa-solid-hover);color:#fff;}

  main{padding:56px 0 24px;}
  .article>*{max-width:var(--measure);margin-left:auto;margin-right:auto;}
  .article p{margin-bottom:18px;}
  .sec{margin-top:64px;}
  .sec-head{margin-bottom:22px;}
  .sec-head .num{display:inline-flex;align-items:center;gap:11px;font-size:.7rem;font-weight:700;letter-spacing:2.4px;text-transform:uppercase;color:var(--g600);margin-bottom:12px;}
  .sec-head .num::before{content:"";width:24px;height:1px;background:var(--navy);}
  .sec h2{font-family:var(--serif);font-weight:600;color:var(--navy);font-size:clamp(1.45rem,3.2vw,1.9rem);line-height:1.25;letter-spacing:-.3px;}
  .sec h2 em{font-style:italic;font-weight:400;color:var(--navy-2);}
  .eyebrow{font-size:.7rem;font-weight:700;letter-spacing:2.6px;text-transform:uppercase;color:var(--g600);}

  .callout{margin:26px auto;max-width:var(--measure);border:1px solid var(--g200);background:var(--g50);border-left:3px solid var(--navy);border-radius:8px;padding:22px 24px;font-size:.94rem;}
  .callout .label{display:block;font-size:.68rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--g600);margin-bottom:8px;}
  .callout p{margin-bottom:10px;}
  .callout p:last-child{margin-bottom:0;}
  .callout.warn{background:#FBF7F0;border-color:#EADFC8;border-left-color:#8A6A2F;}
  .callout.warn .label{color:#8A6A2F;}
  .callout.info{background:#F2F6FA;border-color:#D8E2EC;border-left-color:var(--navy-2);}

  /* índice / tabla resumen */
  .table-wrap{margin:24px auto;max-width:940px;border:1px solid var(--g200);border-radius:8px;overflow-x:auto;}
  table{width:100%;border-collapse:collapse;font-size:.9rem;background:#fff;min-width:560px;}
  thead th{background:var(--navy);color:#fff;text-align:left;font-size:.68rem;letter-spacing:1.4px;text-transform:uppercase;font-weight:600;padding:12px 16px;}
  td,tbody th{padding:12px 16px;border-bottom:1px solid var(--g200);text-align:left;vertical-align:top;}
  tbody th{font-weight:600;color:var(--navy);white-space:nowrap;font-variant-numeric:tabular-nums;}
  tbody tr:nth-child(even){background:var(--g50);}
  tbody tr:last-child th,tbody tr:last-child td{border-bottom:none;}
  td small{color:var(--g600);font-size:.82rem;}
  .toc-list{list-style:none;margin:22px auto;max-width:940px;display:grid;grid-template-columns:1fr 1fr;gap:0 40px;}
  .toc-list a{display:flex;gap:12px;align-items:baseline;padding:11px 0;border-bottom:1px solid var(--g200);text-decoration:none;color:var(--g700);font-size:.93rem;}
  .toc-list a:hover{color:var(--navy);}
  .toc-list .n{font-family:var(--serif);font-style:italic;color:var(--g400);min-width:20px;}
  @media (max-width:760px){.toc-list{grid-template-columns:1fr;}}

  /* ficha */
  .ficha{margin:0 auto 44px;max-width:820px;border:1px solid var(--g200);border-radius:10px;overflow:hidden;background:#fff;}
  .ficha-head{background:var(--navy);color:#fff;padding:24px 28px 22px;position:relative;}
  .ficha-head .fnum{font-family:var(--serif);font-style:italic;font-size:.98rem;color:rgba(255,255,255,.72);letter-spacing:.4px;}
  .ficha-head h3{font-family:var(--serif);font-weight:600;font-size:1.36rem;line-height:1.28;margin-top:6px;color:#fff;}
  .ficha-head .legal{font-size:.78rem;color:rgba(255,255,255,.66);margin-top:8px;line-height:1.5;}
  .ficha-body{padding:26px 28px 24px;}
  .ficha-body>p{font-size:.95rem;margin-bottom:18px;}
  .ficha h4{font-size:.7rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--g600);margin:22px 0 10px;padding-bottom:7px;border-bottom:1px solid var(--g200);}
  .ficha h4:first-of-type{margin-top:0;}
  .ficha ul.req{list-style:none;}
  .ficha ul.req li{position:relative;padding:9px 0 9px 28px;font-size:.93rem;border-bottom:1px dashed var(--g200);}
  .ficha ul.req li:last-child{border-bottom:none;}
  .ficha ul.req li::before{content:"";position:absolute;left:2px;top:15px;width:11px;height:11px;border:1.5px solid var(--g300);border-radius:2px;}
  .chips{display:flex;flex-wrap:wrap;gap:8px;margin:20px 0 0;}
  .chip{font-size:.7rem;font-weight:700;letter-spacing:1.2px;text-transform:uppercase;color:var(--navy);border:1px solid var(--g300);border-radius:20px;padding:5px 12px;background:var(--g50);}
  .notas{background:var(--g50);border-top:1px solid var(--g200);padding:20px 28px 22px;}
  .notas .label{display:block;font-size:.66rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:var(--g600);margin-bottom:10px;}
  .notas ul{list-style:none;}
  .notas li{position:relative;padding:7px 0 7px 20px;font-size:.9rem;color:var(--g700);}
  .notas li::before{content:"—";position:absolute;left:0;color:var(--navy-2);}
  @media (max-width:640px){.ficha-head{padding:20px 20px 18px;}.ficha-body{padding:20px;}.notas{padding:18px 20px;}}

  .ficha-nav{display:flex;justify-content:space-between;gap:12px;max-width:820px;margin:0 auto 10px;font-size:.86rem;}
  .ficha-nav a{text-decoration:none;color:var(--navy);font-weight:500;}
  .ficha-nav a:hover{text-decoration:underline;}

  .checklist{list-style:none;max-width:940px;margin:22px auto;}
  .checklist li{display:flex;gap:14px;align-items:flex-start;padding:11px 0;border-bottom:1px solid var(--g200);font-size:.94rem;}
  .checklist li::before{content:"";width:14px;height:14px;border:1.5px solid var(--g300);border-radius:2px;flex-shrink:0;margin-top:5px;}
  .checklist .cn{font-family:var(--serif);font-style:italic;color:var(--g400);min-width:22px;}

  .final{background:linear-gradient(158deg,var(--navy-deep) 0%,var(--navy) 55%,var(--navy-2) 100%);color:#fff;padding:64px 0;margin-top:56px;}
  .final .wrap{max-width:820px;}
  .final h2{font-family:var(--serif);font-weight:600;font-size:clamp(1.6rem,3.6vw,2.2rem);line-height:1.2;margin:12px 0 14px;}
  .final h2 em{font-style:italic;font-weight:400;color:#C9D3DC;}
  .final p{color:rgba(255,255,255,.82);max-width:560px;margin-bottom:24px;}
  .final .eyebrow{color:var(--g400);}

  footer{background:var(--navy-deep);color:rgba(255,255,255,.66);padding:44px 0 28px;font-size:.83rem;}
  footer .flogo{width:180px;margin-bottom:16px;}
  footer .fgrid{display:grid;grid-template-columns:1.4fr 1fr 1fr;gap:30px;}
  footer h5{color:#fff;font-size:.68rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:12px;}
  footer a{color:rgba(255,255,255,.82);text-decoration:none;}
  footer a:hover{color:#fff;text-decoration:underline;}
  footer ul{list-style:none;}
  footer li{padding:4px 0;}
  footer .fnote{border-top:1px solid rgba(255,255,255,.12);margin-top:28px;padding-top:18px;font-size:.76rem;color:rgba(255,255,255,.5);line-height:1.6;}
  @media (max-width:800px){footer .fgrid{grid-template-columns:1fr;gap:22px;}}

  .disclaimer{max-width:760px;margin:34px auto 0;font-size:.8rem;color:var(--g600);line-height:1.65;}

  a:focus-visible,summary:focus-visible,.btn:focus-visible{outline:2px solid var(--navy);outline-offset:3px;}
  .hero a:focus-visible,.final a:focus-visible{outline-color:#fff;}

  @media (max-width:900px){.nav-links a:not(.nav-cta){display:none;}.nav-logo{width:140px;}}
  @media (max-width:560px){
    .nav .wrap{height:60px;gap:10px;}
    .nav-logo{width:124px;}
    .nav-cta{padding:8px 12px;font-size:.78rem;}
    .cta-long{display:none;}.cta-short{display:inline;}
    .topbar{font-size:.7rem;}
    .hero{padding:40px 0 44px;}
    .hero-logo{width:162px;margin-bottom:24px;}
  }

  @media print{
    .topbar,.nav,.hero-cta,.final,.ficha-nav,.toc-list{display:none!important;}
    body{font-size:10pt;color:#111;line-height:1.5;}
    .wrap{max-width:none;padding:0;}
    .article>*{max-width:none;}
    .hero{background:#fff!important;color:#000;padding:0 0 12px;border-bottom:2px solid #0D1B2A;}
    .hero-logo{filter:invert(1) brightness(.2);width:140px;margin-bottom:14px;}
    .hero h1{color:#0D1B2A;font-size:22pt;}
    .hero h1 em{color:#1B3A57;}
    .hero .lead{color:#222;}
    .byline{color:#444;border-top:1px solid #ccc;}
    .byline strong{color:#000;}
    .ficha{page-break-before:always;page-break-inside:auto;border:1px solid #bbb;max-width:none;margin:0 0 12px;}
    .ficha:first-of-type{page-break-before:auto;}
    .ficha h4{page-break-after:avoid;}
    .toc-sec{display:none!important;}
    /* ficha suelta: nada de saltos forzados ni portada que desborde */
    body.single .hero{padding:0 0 10px;}
    body.single .hero-logo{width:118px;margin-bottom:10px;}
    body.single .hero h1{font-size:18pt;}
    body.single .ficha{page-break-before:auto;page-break-inside:auto;margin-top:10px;}
    .ficha-head{background:#0D1B2A!important;color:#fff!important;-webkit-print-color-adjust:exact;print-color-adjust:exact;}
    .ficha-body>p,.ficha ul.req li,.notas li{font-size:9.6pt;}
    .callout,.table-wrap,.checklist li{page-break-inside:avoid;}
    .table-wrap{max-width:none;overflow:visible;border:1px solid #ccc;}
    table{min-width:0;font-size:9pt;}
    thead{display:table-header-group;}
    footer{background:#fff;color:#333;border-top:1px solid #ccc;}
    footer h5,footer a{color:#000;}
    footer .flogo{filter:invert(1) brightness(.2);width:140px;}
    footer .fnote{color:#555;}
  }
"""


# --------------------------------------------------------------------------------------
# Bloques HTML reutilizables
# --------------------------------------------------------------------------------------
def head(title, desc, canonical_file):
    return f"""<!DOCTYPE html>
<html lang="es-PA">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="robots" content="index, follow" />
<meta name="author" content="Lic. Alfonso Villarreal · Naturalízate.pa" />
<meta name="theme-color" content="#0D1B2A" />
<link rel="canonical" href="{SITE}{canonical_file}" />
<meta property="og:type" content="article" />
<meta property="og:locale" content="es_PA" />
<meta property="og:site_name" content="Naturalízate.pa" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:image" content="{SITE}og-image.png" />
<meta name="twitter:card" content="summary_large_image" />
<style>__CSS__</style>
</head>
<body>
"""


def topbar():
    return f"""<div class="topbar">
  <div class="wrap">
    <span><strong>Naturalízate.pa</strong> · Scotia Plaza, Piso 7. Av. Federico Boyd, Panamá</span>
    <span>Depto. de Naturalización (Migración) · Tel. {TEL_DEPTO} · WhatsApp <a href="{WA}" target="_blank" rel="noopener">+507 6255-7583</a></span>
  </div>
</div>
"""


def nav(home, cta="Precalificar mi caso"):
    return f"""<header class="nav">
  <div class="wrap">
    <a class="nav-logo" href="{home}" aria-label="Naturalízate.pa">
      <img src="data:image/svg+xml;base64,__LOGO_NAVY__" alt="Naturalízate.pa" width="164" height="22" />
    </a>
    <nav class="nav-links" aria-label="Navegación">
      <a href="{home}#numerales">Los 14 numerales</a>
      <a href="{home}#resumen">Resumen</a>
      <a href="{home}#checklist">Checklist</a>
      <a class="nav-cta" href="{WA}" target="_blank" rel="noopener"><span class="cta-long">{cta}</span><span class="cta-short">WhatsApp</span></a>
    </nav>
  </div>
</header>
"""


def footer(home):
    return f"""<footer>
  <div class="wrap">
    <div class="fgrid">
      <div>
        <img class="flogo" src="data:image/svg+xml;base64,__LOGO_WHITE__" alt="Naturalízate.pa" width="180" height="24" />
        <p style="max-width:36ch;">Requisitos de la Carta de Naturaleza, organizados numeral por numeral. Documento de trabajo del despacho, con la marca de Naturalízate.pa.</p>
      </div>
      <div>
        <h5>Contacto</h5>
        <ul>
          <li><a href="{WA}" target="_blank" rel="noopener">WhatsApp · +507 6255-7583</a></li>
          <li><a href="mailto:Villarreallawyers@proton.me">Villarreallawyers@proton.me</a></li>
          <li>Scotia Plaza, Piso 7.<br />Av. Federico Boyd, Panamá</li>
          <li>Lun–Vie · 8:00 a.m. – 5:00 p.m.</li>
        </ul>
      </div>
      <div>
        <h5>Enlaces</h5>
        <ul>
          <li><a href="{home}">Índice de numerales</a></li>
          <li><a href="{SITE}">Sitio principal</a></li>
          <li><a href="{SITE}guia-naturalizacion-completa.html">Guía completa de naturalización</a></li>
        </ul>
      </div>
    </div>
    <div class="fnote">
      © 2026 Naturalízate.pa · Lic. Alfonso Villarreal · Scotia Plaza, Piso 7. Av. Federico Boyd, Panamá.<br />
      Documento de trabajo elaborado a partir de los requisitos publicados por el Servicio Nacional de Migración (NAT 2-1, abril de 2026). No sustituye el documento oficial ni constituye asesoría legal para un caso particular; los requisitos, timbres y vigencias pueden variar y deben confirmarse al momento de presentar.
    </div>
  </div>
</footer>
"""


def ficha_html(item, standalone=False):
    groups = ""
    for g in item["groups"]:
        items = "".join(f"<li>{i}</li>" for i in g["items"])
        groups += f'<h4>{g["h"]}</h4>\n<ul class="req">{items}</ul>\n'
    chips = ""
    if item["chips"]:
        chips = '<div class="chips">' + "".join(
            f'<span class="chip">{c}</span>' for c in item["chips"]) + "</div>"
    notas = ""
    if item["notas"]:
        notas = ('<div class="notas"><span class="label">Criterio del despacho · no forma parte del documento oficial</span><ul>'
                 + "".join(f"<li>{n}</li>" for n in item["notas"]) + "</ul></div>")
    return f"""<section class="ficha" id="num-{item['n']}">
  <div class="ficha-head">
    <div class="fnum">Numeral {item['n']:02d} de 14</div>
    <h3>{item['title']}</h3>
    <div class="legal">{item['legal']}</div>
  </div>
  <div class="ficha-body">
    <p>{item['intro']}</p>
    {groups}
    {chips}
  </div>
  {notas}
</section>"""


# --------------------------------------------------------------------------------------
# Documento maestro
# --------------------------------------------------------------------------------------
def build_master():
    toc = "".join(
        f'<li><a href="#num-{i["n"]}"><span class="n">{i["n"]}</span><span>{i["title"]}</span></a></li>'
        for i in NUMERALES)
    rows = "".join(
        f'<tr><th scope="row">{i["n"]}</th><td><a href="#num-{i["n"]}" style="text-decoration:none;color:inherit;">{i["resumen"]}</a></td>'
        f'<td><small>{", ".join(i["chips"]) if i["chips"] else "—"}</small></td></tr>'
        for i in NUMERALES)
    fichas = "\n".join(ficha_html(i) for i in NUMERALES)
    checklist = "".join(
        f'<li><span class="cn">{i["n"]}</span><span>{i["resumen"]}</span></li>' for i in NUMERALES)

    html = head(
        "Requisitos de la Carta de Naturaleza, numeral por numeral | Naturalízate.pa",
        "Los 14 numerales de requisitos de la solicitud de Carta de Naturaleza (NAT 2-1, Migración), organizados uno por uno, con vigencias, timbres y criterio del despacho. Lic. Alfonso Villarreal.",
        "requisitos-carta-de-naturaleza.html")
    html += topbar()
    html += nav("#numerales")
    html += f"""
<section class="hero">
  <div class="wrap">
    <img class="hero-logo" src="data:image/svg+xml;base64,__LOGO_WHITE__" alt="Naturalízate.pa" width="196" height="26" />
    <div class="kicker">Documento de trabajo · NAT 2-1 · Migración, abril de 2026</div>
    <h1>Requisitos de la Carta de Naturaleza, <em>numeral por numeral</em></h1>
    <p class="lead">Los catorce numerales del documento oficial, cada uno en su propia ficha: qué exige, con qué vigencia, cuántos timbres lleva y en qué punto suele devolverse el expediente.</p>
    <div class="byline">
      <span>Organizado por <strong>Lic. Alfonso Villarreal</strong></span>
      <span>·</span>
      <span>Naturalízate.pa · Ciudad de Panamá</span>
      <span>·</span>
      <span>Fuente: Servicio Nacional de Migración</span>
    </div>
    <div class="hero-cta">
      <a class="btn btn-white" href="#numerales">Ver los 14 numerales</a>
      <a class="btn btn-outline-w" href="#checklist">Checklist imprimible</a>
    </div>
  </div>
</section>

<main>
  <div class="wrap">
    <article class="article">

      <section>
        <div class="sec-head">
          <div class="num">Antes de empezar</div>
          <h2>Qué es este documento y qué <em>no es</em></h2>
        </div>
        <p>Esta es una transcripción organizada —no una reinterpretación— de los requisitos que el Servicio Nacional de Migración publica para la solicitud de Carta de Naturaleza. Cada numeral oficial se presenta en una ficha independiente, con sus requisitos en formato de lista verificable, para que el expediente se arme sin depender de la memoria.</p>
        <p>Cada ficha lleva dos bloques que conviene distinguir: los <strong>requisitos</strong>, que provienen del documento oficial, y el <strong>criterio del despacho</strong>, rotulado en gris al pie de cada ficha, que recoge la práctica y los errores observados. Lo segundo no forma parte del documento oficial.</p>

        <div class="callout warn">
          <span class="label">Advertencia importante</span>
          <p>El documento oficial prevalece siempre sobre esta versión de trabajo. Los timbres, vigencias y requisitos pueden actualizarse: confirme cada punto con el Departamento de Naturalización (Tel. {TEL_DEPTO}) o con su abogado al momento de presentar. Esta guía no constituye asesoría legal para un caso particular.</p>
        </div>

        <div class="callout">
          <span class="label">Regla que aplica a todos los numerales</span>
          <p>{NOTA_GENERAL}</p>
        </div>
      </section>

      <section class="sec" id="resumen">
        <div class="sec-head">
          <div class="num">Vista de conjunto</div>
          <h2>Los 14 numerales en una <em>tabla</em></h2>
        </div>
        <p>Una lectura rápida para ubicar qué documento resuelve cada numeral y cuáles tienen vigencia corta.</p>
        <div class="table-wrap">
          <table>
            <thead><tr><th scope="col">No.</th><th scope="col">Qué se presenta</th><th scope="col">Vigencia / timbres</th></tr></thead>
            <tbody>{rows}</tbody>
          </table>
        </div>

        <div class="callout info">
          <span class="label">Fichas independientes</span>
          <p>Cada numeral tiene también su propio archivo HTML, listo para imprimir o enviar solo: <code>fichas/numeral-01.html</code> a <code>fichas/numeral-14.html</code>, incluidos en <code>requisitos-fichas-numerales.zip</code>. Puede compartir el numeral 6 con un cliente sin enviar el documento completo.</p>
        </div>
      </section>

      <section class="sec toc-sec" id="numerales">
        <div class="sec-head">
          <div class="num">Fichas</div>
          <h2>Un numeral, una <em>ficha</em></h2>
        </div>
        <ul class="toc-list">{toc}</ul>
      </section>

      {fichas}

      <section class="sec" id="checklist">
        <div class="sec-head">
          <div class="num">Control</div>
          <h2>Checklist <em>imprimible</em></h2>
        </div>
        <p>Marque cada numeral cuando el documento esté reunido, verificado y vigente. Si imprime esta página, las casillas quedan listas para usar.</p>
        <ul class="checklist">{checklist}</ul>
        <div class="callout">
          <span class="label">Recuerde</span>
          <p>{NOTA_GENERAL} Los documentos con vigencia de 30 o 90 días se solicitan al final: presentar un expediente con documentos vencidos equivale a empezar de nuevo.</p>
        </div>
      </section>

      <section class="sec">
        <div class="sec-head">
          <div class="num">Fuente</div>
          <h2>De dónde sale esta <em>versión</em></h2>
        </div>
        <p>El contenido de las fichas proviene de <strong>{FUENTE}</strong>, publicado por el Servicio Nacional de Migración. Las fichas 5 y 12 conservan además la indicación oficial de la vía constitucional a la que pertenecen (numeral 2 y numeral 3 del artículo 10).</p>
        <p>La organización en fichas, los avisos de vigencia destacados y los criterios del despacho son aportes de Naturalízate.pa.</p>
        <p class="disclaimer">Aviso legal: documento de trabajo con fines informativos. Los requisitos oficiales, timbres y vigencias pueden cambiar sin previo aviso; la autoridad migratoria decide sobre la admisión de cada documento. Naturalízate.pa es una práctica jurídica privada, independiente del Estado panameño, y no garantiza resultados.</p>
      </section>

    </article>
  </div>

  <section class="final">
    <div class="wrap">
      <div class="eyebrow">Revisión previa · sin costo</div>
      <h2>¿Ya tiene los documentos? <em>Conviene revisarlos antes de presentar.</em></h2>
      <p>Auditamos su expediente numeral por numeral, verificamos vigencias y le indicamos por escrito qué falta antes de radicar la solicitud.</p>
      <div class="hero-cta">
        <a class="btn btn-white" href="{SITE}">Solicitar revisión</a>
        <a class="btn btn-wa" href="{WA}" target="_blank" rel="noopener">Hablar por WhatsApp</a>
      </div>
    </div>
  </section>
</main>
"""
    html += footer("#numerales")
    html += "</body>\n</html>\n"
    return html


# --------------------------------------------------------------------------------------
# Fichas independientes
# --------------------------------------------------------------------------------------
def build_ficha(item):
    prev_n, next_n = item["n"] - 1, item["n"] + 1
    prev_link = (f'<a href="numeral-{prev_n:02d}.html">← Numeral {prev_n:02d}</a>'
                 if prev_n >= 1 else '<a href="index.html">← Índice</a>')
    next_link = (f'<a href="numeral-{next_n:02d}.html">Numeral {next_n:02d} →</a>'
                 if next_n <= len(NUMERALES) else '<a href="index.html">Índice →</a>')
    html = head(
        f"Numeral {item['n']:02d} · {item['title']} | Requisitos de la Carta de Naturaleza",
        f"{item['title']}: requisitos del numeral {item['n']} de la solicitud de Carta de Naturaleza (NAT 2-1, Migración). Naturalízate.pa.",
        f"fichas/numeral-{item['n']:02d}.html")
    html = html.replace('<body>', '<body class="single">', 1)
    html += topbar()
    html += nav("index.html", "Consultar mi caso")
    html += f"""
<section class="hero" style="padding:40px 0 44px;">
  <div class="wrap">
    <img class="hero-logo" src="data:image/svg+xml;base64,__LOGO_WHITE__" alt="Naturalízate.pa" width="180" height="24" />
    <div class="kicker">Requisitos de la Carta de Naturaleza · Ficha {item['n']:02d} de 14</div>
    <h1>Numeral {item['n']:02d}: <em>{item['title']}</em></h1>
  </div>
</section>

<main>
  <div class="wrap">
    <div class="ficha-nav" style="margin-top:0;">
      {prev_link}
      <a href="index.html">Índice de los 14 numerales</a>
      {next_link}
    </div>
    {ficha_html(item, standalone=True)}
    <p class="disclaimer">Transcripción organizada de <strong>{FUENTE}</strong>. El documento oficial prevalece. Los criterios del despacho no forman parte del documento oficial. Requisitos, timbres y vigencias deben confirmarse al momento de presentar.</p>
    <div class="callout" style="margin-top:24px;">
      <span class="label">Contacto del despacho</span>
      <p>Lic. Alfonso Villarreal · Scotia Plaza, Piso 7. Av. Federico Boyd, Panamá · <a href="{WA}" target="_blank" rel="noopener">WhatsApp +507 6255-7583</a> · Villarreallawyers@proton.me</p>
    </div>
  </div>
</main>
"""
    html += footer("index.html")
    html += "</body>\n</html>\n"
    return html


def main():
    CSS_FINAL = (CSS.replace("__FONT_INTER__", FONT_INTER)
                 .replace("__FONT_PLAYFAIR_IT__", FONT_PLAYFAIR_IT)
                 .replace("__FONT_PLAYFAIR__", FONT_PLAYFAIR))

    def finish(html):
        return (html.replace("__CSS__", CSS_FINAL)
                .replace("__LOGO_NAVY__", LOGO_NAVY)
                .replace("__LOGO_WHITE__", LOGO_WHITE))

    master = finish(build_master())
    OUT_MASTER.write_text(master, encoding="utf-8")
    print(f"OK → {OUT_MASTER.name} ({OUT_MASTER.stat().st_size/1024:.0f} KB)")

    DIR_FICHAS.mkdir(exist_ok=True)
    files = []
    for item in NUMERALES:
        p = DIR_FICHAS / f"numeral-{item['n']:02d}.html"
        p.write_text(finish(build_ficha(item)), encoding="utf-8")
        files.append(p)
    print(f"OK → {len(files)} fichas en {DIR_FICHAS.name}/")

    # índice de la carpeta de fichas (versión mínima, para abrir desde el zip)
    idx = f"""<!DOCTYPE html>
<html lang="es-PA"><head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>Requisitos de la Carta de Naturaleza · Fichas por numeral</title>
<style>
 :root{{--navy:#0D1B2A;--g200:#E9ECEF;--g400:#ADB5BD;--g600:#5C6772;}}
 body{{margin:0;font-family:Georgia,serif;background:#0D1B2A;color:#fff;display:flex;min-height:100vh;align-items:center;justify-content:center;padding:40px 24px;}}
 .box{{max-width:620px;width:100%;background:#fff;color:#212529;border-radius:12px;padding:40px;}}
 h1{{font-size:1.5rem;line-height:1.25;margin:0 0 6px;color:#0D1B2A;}}
 .k{{font-family:Arial,Helvetica,sans-serif;font-size:.7rem;letter-spacing:2px;text-transform:uppercase;color:#5C6772;margin-bottom:14px;}}
 p{{font-family:Arial,Helvetica,sans-serif;font-size:.9rem;color:#495057;line-height:1.6;}}
 ol{{font-family:Arial,Helvetica,sans-serif;font-size:.92rem;line-height:1.7;padding-left:22px;margin:18px 0 0;}}
 a{{color:#1B3A57;}}
 li{{margin-bottom:4px;}}
</style></head><body><div class="box">
<div class="k">Naturalízate.pa · Documento de trabajo</div>
<h1>Requisitos de la Carta de Naturaleza: una ficha por numeral</h1>
<p>Catorce archivos independientes, basados en el documento NAT 2-1 del Servicio Nacional de Migración. Abra el numeral que necesite; cada ficha conserva la marca y puede imprimirse sola.</p>
<ol>
""" + "".join(f'<li><a href="numeral-{i["n"]:02d}.html">Numeral {i["n"]:02d} · {i["title"]}</a></li>' for i in NUMERALES) + """
</ol>
<p style="margin-top:22px;font-size:.8rem;color:#5C6772;">El documento oficial de Migración prevalece sobre esta versión de trabajo. Requisitos, timbres y vigencias deben confirmarse al presentar.</p>
</div></body></html>
"""
    (DIR_FICHAS / "index.html").write_text(idx, encoding="utf-8")

    with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(DIR_FICHAS.glob("*.html")):
            z.write(p, arcname=f"requisitos-naturalizacion-fichas/{p.name}")
    print(f"OK → {ZIP_PATH.name} ({ZIP_PATH.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
