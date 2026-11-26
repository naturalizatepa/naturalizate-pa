<script>
/* =====================================================================
   NATURALÍZATE.pa · Formulario interno — informe en PDF sin dependencias
   Todo el PDF se construye en el navegador (Helvetica + WinAnsi) y se
   descarga directamente. No requiere internet ni librerías externas.
   ===================================================================== */
(function () {
  "use strict";

  /* ══════════ 1. Utilidades de PDF ══════════ */
  var PDF_W = 612, PDF_H = 792, MARGEN = 48, ANCHO = PDF_W - MARGEN * 2; /* 516 */

  var HELV = { " ":278,"!":278,'"':355,"#":556,"$":556,"%":889,"&":667,"'":191,"(":333,")":333,"*":389,"+":584,",":278,"-":333,".":278,"/":278,
    "0":556,"1":556,"2":556,"3":556,"4":556,"5":556,"6":556,"7":556,"8":556,"9":556,":":278,";":278,"<":584,"=":584,">":584,"?":556,"@":1015,
    "A":667,"B":667,"C":722,"D":722,"E":667,"F":611,"G":778,"H":722,"I":278,"J":500,"K":667,"L":556,"M":833,"N":722,"O":778,"P":667,"Q":778,"R":722,"S":667,"T":611,"U":722,"V":667,"W":944,"X":667,"Y":667,"Z":611,
    "[":278,"\\":278,"]":278,"^":469,"_":556,"`":333,
    "a":556,"b":556,"c":500,"d":556,"e":556,"f":278,"g":556,"h":556,"i":222,"j":222,"k":500,"l":222,"m":833,"n":556,"o":556,"p":556,"q":556,"r":333,"s":500,"t":278,"u":556,"v":500,"w":722,"x":500,"y":500,"z":500,
    "{":334,"|":260,"}":334,"~":584 };

  var BASE_CHAR = { "á":"a","é":"e","í":"i","ó":"o","ú":"u","ñ":"n","ü":"u","Á":"A","É":"E","Í":"I","Ó":"O","Ú":"U","Ñ":"N","Ü":"U",
    "«":'"',"»":'"',"“":'"',"”":'"',"’":"'","‘":"'","–":"-","—":"-","·":".","…":".","¿":"?","¡":"!","°":"o","º":"o","ª":"a","§":"S" };

  var WINANSI_EXTRA = { "\u201A":130,"\u0192":131,"\u201E":132,"\u2026":133,"\u2020":134,"\u2021":135,"\u02C6":136,"\u2030":137,"\u0160":138,"\u2039":139,"\u0152":140,"\u017D":142,
    "\u2018":145,"\u2019":146,"\u201C":147,"\u201D":148,"\u2022":149,"\u2013":150,"\u2014":151,"\u02DC":152,"\u2122":153,"\u0161":154,"\u203A":155,"\u0153":156,"\u017E":158,"\u0178":159 };

  function anchoTexto(t, size, bold) {
    var w = 0;
    for (var i = 0; i < t.length; i++) {
      var ch = BASE_CHAR[t.charAt(i)] || t.charAt(i);
      var cw = HELV[ch];
      if (cw === undefined) cw = 556;
      w += cw;
    }
    w = w / 1000 * size;
    return bold ? w * 1.05 : w;
  }
  function envolver(t, size, bold, maxW) {
    var palabras = String(t === undefined || t === null ? "" : t).split(/\s+/);
    var lineas = [], actual = "";
    for (var i = 0; i < palabras.length; i++) {
      var p = palabras[i];
      var prueba = actual ? actual + " " + p : p;
      if (anchoTexto(prueba, size, bold) <= maxW) { actual = prueba; continue; }
      if (actual) lineas.push(actual);
      if (anchoTexto(p, size, bold) > maxW) {
        var trozo = "";
        for (var k = 0; k < p.length; k++) {
          if (anchoTexto(trozo + p.charAt(k), size, bold) > maxW) { lineas.push(trozo); trozo = p.charAt(k); }
          else trozo += p.charAt(k);
        }
        actual = trozo;
      } else { actual = p; }
    }
    if (actual) lineas.push(actual);
    return lineas.length ? lineas : [""];
  }
  function escaparPDF(s) {
    var out = "";
    for (var i = 0; i < s.length; i++) {
      var ch = s.charAt(i), code = s.charCodeAt(i);
      if (WINANSI_EXTRA[ch] !== undefined) code = WINANSI_EXTRA[ch];
      else if (code > 255) code = 63;
      if (code === 40) out += "\\(";
      else if (code === 41) out += "\\)";
      else if (code === 92) out += "\\\\";
      else if (code < 32 || code > 126) out += "\\" + ("000" + code.toString(8)).slice(-3);
      else out += ch;
    }
    return out;
  }
  function serializarPDF(paginas, titulo) {
    var N = paginas.length, numContenido = [], numPagina = [], n = 5;
    for (var i = 0; i < N; i++) { numContenido[i] = n++; numPagina[i] = n++; }
    var numInfo = n++;
    var objs = {};
    objs[1] = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica /Encoding /WinAnsiEncoding >>";
    objs[2] = "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold /Encoding /WinAnsiEncoding >>";
    objs[3] = "<< /Type /Pages /Kids [" + numPagina.map(function (x) { return x + " 0 R"; }).join(" ") + "] /Count " + N + " >>";
    objs[4] = "<< /Type /Catalog /Pages 3 0 R >>";
    for (var j = 0; j < N; j++) {
      var stream = paginas[j].join("\n");
      objs[numContenido[j]] = "<< /Length " + stream.length + " >>\nstream\n" + stream + "\nendstream";
      objs[numPagina[j]] = "<< /Type /Page /Parent 3 0 R /MediaBox [0 0 612 792] /Resources << /Font << /F1 1 0 R /F2 2 0 R >> >> /Contents " + numContenido[j] + " 0 R >>";
    }
    function p2(x) { return (x < 10 ? "0" : "") + x; }
    var ahora = new Date();
    var fecha = "D:" + ahora.getFullYear() + p2(ahora.getMonth() + 1) + p2(ahora.getDate()) + p2(ahora.getHours()) + p2(ahora.getMinutes()) + p2(ahora.getSeconds());
    var hexTitulo = "FEFF";
    var tLim = String(titulo || "Informe");
    for (var th = 0; th < tLim.length; th++) { hexTitulo += ("0000" + tLim.charCodeAt(th).toString(16).toUpperCase()).slice(-4); }
    objs[numInfo] = "<< /Title <" + hexTitulo + "> /Author (Naturalizate.pa) /Creator (Formulario interno Naturalizate.pa) /CreationDate (" + fecha + ") >>";
    var total = numInfo, out = "%PDF-1.7\n", offs = [];
    for (var m = 1; m <= total; m++) { offs[m] = out.length; out += m + " 0 obj\n" + objs[m] + "\nendobj\n"; }
    var xref = out.length;
    out += "xref\n0 " + (total + 1) + "\n0000000000 65535 f \n";
    for (var q = 1; q <= total; q++) { out += ("0000000000" + offs[q]).slice(-10) + " 00000 n \n"; }
    out += "trailer\n<< /Size " + (total + 1) + " /Root 4 0 R /Info " + numInfo + " 0 R >>\nstartxref\n" + xref + "\n%%EOF\n";
    var bytes = new Uint8Array(out.length);
    for (var b = 0; b < out.length; b++) bytes[b] = out.charCodeAt(b) & 0xFF;
    return bytes;
  }

  /* ══════════ 2. Lógica de veredicto (misma del sitio público) ══════════ */
  var RECIPROCIDAD = { "el salvador": 1, "argentina": 2, "ecuador": 2, "espana": 2, "honduras": 2, "mexico": 2, "nicaragua": 2, "peru": 2, "colombia": 2, "uruguay": 3 };
  function normPais(s) {
    try { return (s || "").toLowerCase().normalize("NFD").replace(/[\u0300-\u036f]/g, "").trim(); }
    catch (e) { return (s || "").toLowerCase().trim(); }
  }
  var ETIQUETAS = {
    cedula: { menos3: "Menos de 3 años", entre35: "Entre 3 y 5 años", mas5: "Más de 5 años", nose: "No está seguro(a)" },
    ausencias: { no: "No", menores: "Sí, menores a 6 meses", mayores: "Sí, mayores a 6 meses", nose: "No está seguro(a)" },
    examen: { si: "Sí, con disciplina", dudas: "Tiene dudas sobre el examen", no: "No" },
    civil: { soltero: "Soltero(a)", casado: "Casado(a)", unido: "Unido(a)", divorciado: "Divorciado(a)", viudo: "Viudo(a)" },
    objetivo: { iniciar: "Iniciar el proceso", evaluar: "Evaluar si califica", info: "Orientación general" },
    disponibilidad: { ahora: "De inmediato", "30dias": "Próximos 30 días", meses: "En 2 a 3 meses", nose: "Por confirmar" },
    modalidad: { esencial: "Proceso Esencial", todo: "Proceso Todo Incluido" }
  };
  function etiqueta(grupo, valor) {
    var g = ETIQUETAS[grupo] || {};
    return (g[valor] !== undefined && valor !== "") ? g[valor] : (valor || "—");
  }

  function calcularVeredicto(d) {
    var recip = RECIPROCIDAD[normPais(d.pais)] || 0;
    var docs = (d.doc_renta ? 1 : 0) + (d.doc_banco ? 1 : 0) + (d.doc_trabajo ? 1 : 0);
    if (!d.cedula) {
      return { clave: "incompleto", badge: "Complete el perfil", clase: "b-neutro",
        texto: "Faltan datos para calcular el veredicto (años de Cédula E).",
        recomendacion: "Complete el perfil migratorio y documental para emitir el veredicto." };
    }
    if (d.cedula === "menos3" && !recip) {
      return { clave: "computo", badge: "Aún no es el momento", clase: "b-no",
        texto: "La naturalización exige 5 años de residencia permanente. Con menos de 3 años de Cédula E y sin convenio de reciprocidad, presentar ahora carece de viabilidad.",
        recomendacion: "Orientar al solicitante y programar seguimiento para cuando se cumpla el cómputo legal." };
    }
    if (d.examen === "no") {
      return { clave: "examen", badge: "Requisito legal pendiente", clase: "b-no",
        texto: "El examen de naturalización ante el Tribunal Electoral es un requisito legal obligatorio.",
        recomendacion: "Explicar el alcance del examen y su preparación guiada." };
    }
    if (docs >= 2) {
      return { clave: "apto_2de3", badge: "Perfil apto · cumple 2 de 3", clase: "b-ok",
        texto: "Perfil apto para iniciar el acompañamiento jurídico. Solvencia acreditada con " + docs + " de las 3 pruebas admitidas.",
        recomendacion: "Definir la modalidad recomendada (Proceso Esencial o Proceso Todo Incluido) e iniciar pre-auditoría documental." };
    }
    if (docs === 1) {
      return { clave: "apto_falta_una", badge: "Perfil apto · falta 1 prueba", clase: "b-warn",
        texto: "Perfil apto, con una sola prueba de solvencia registrada. La norma exige dos de tres.",
        recomendacion: "Definir cuál segunda prueba tramitar y con qué vigencia antes de presentar." };
    }
    return { clave: "apto_sin_docs", badge: "Perfil apto · solvencia por definir", clase: "b-warn",
      texto: "Perfil apto en lo migratorio; pendiente seleccionar dos pruebas documentales de solvencia.",
      recomendacion: "Definir qué dos pruebas de solvencia tramitará el solicitante." };
  }

  /* ══════════ 3. Lectura del formulario ══════════ */
  function val(id) { var el = document.getElementById(id); return el ? el.value.trim() : ""; }
  function marcado(id) { var el = document.getElementById(id); return !!(el && el.checked); }
  function leerFormulario() {
    var pais = val("i_pais") === "otro" ? val("i_pais_otro") : val("i_pais");
    return {
      nombre: val("i_nombre"), whatsapp: val("i_whatsapp"), email: val("i_email"), pais: pais,
      cedula: val("i_cedula"), ausencias: val("i_ausencias"), civil: val("i_civil"), examen: val("i_examen"),
      dependiente: marcado("i_dependiente"), modalidad: val("i_modalidad"),
      doc_renta: marcado("i_doc_renta"), doc_banco: marcado("i_doc_banco"), doc_trabajo: marcado("i_doc_trabajo"),
      notas_docs: val("i_notas_docs"),
      objetivo: val("i_objetivo"), disponibilidad: val("i_disponibilidad"),
      asesor: val("i_asesor"), cita_fecha: val("i_cita_fecha"), cita_hora: val("i_cita_hora"), dia: val("i_dia"),
      notas: val("i_notas")
    };
  }
  function docsTexto(d) {
    var lista = [];
    if (d.doc_renta) lista.push("Declaración de Renta (2 años, CPA y notario)");
    if (d.doc_banco) lista.push("Carta bancaria al Servicio Nacional de Migración");
    if (d.doc_trabajo) lista.push("Carta de trabajo + ficha CSS");
    return lista.length ? lista.join(" · ") : "Ninguna registrada";
  }
  function fechaLegible(iso) {
    if (!iso) return "—";
    var p = iso.split("-");
    return p.length === 3 ? p[2] + "/" + p[1] + "/" + p[0] : iso;
  }
  function selloTiempo() {
    var d = new Date();
    function p(n) { return (n < 10 ? "0" : "") + n; }
    return p(d.getDate()) + "/" + p(d.getMonth() + 1) + "/" + d.getFullYear() + " · " + p(d.getHours()) + ":" + p(d.getMinutes());
  }

  /* ══════════ 4. Construcción del informe PDF ══════════ */
  function construirInformePDF(d) {
    var v = calcularVeredicto(d);
    var paginas = [], ops = null, y = 0, numeroPagina = 0;
    var generado = selloTiempo();

    function nuevaPagina() {
      numeroPagina++;
      ops = [];
      paginas.push(ops);
      /* Banda de cabecera */
      ops.push("0.051 0.106 0.165 rg");
      ops.push("0 716 612 76 re f");
      ops.push("1 1 1 rg");
      ops.push("BT /F2 15 Tf 1 0 0 1 48 764 Tm (" + escaparPDF("NATURALÍZATE.pa") + ") Tj ET");
      ops.push("0.70 0.75 0.80 rg");
      ops.push("BT /F1 8.5 Tf 1 0 0 1 48 749 Tm (" + escaparPDF("INFORME INTERNO DE PRECALIFICACIÓN · USO DEL DESPACHO") + ") Tj ET");
      var der = "Scotia Plaza, Piso 7. Av. Federico Boyd, Panamá, Provincia de Panamá";
      ops.push("BT /F1 8.5 Tf 1 0 0 1 " + (564 - anchoTexto(der, 8.5, false)).toFixed(1) + " 764 Tm (" + escaparPDF(der) + ") Tj ET");
      var der2 = "Generado: " + generado;
      ops.push("BT /F1 8.5 Tf 1 0 0 1 " + (564 - anchoTexto(der2, 8.5, false)).toFixed(1) + " 749 Tm (" + escaparPDF(der2) + ") Tj ET");
      y = 698;
    }
    function avanzar(dy) {
      if (y - dy < 92) { nuevaPagina(); }
      y -= dy;
    }
    function reservar(alto) { /* evita títulos huérfanos: exige espacio antes de dibujar */
      if (y - alto < 92) { nuevaPagina(); }
    }
    function textoLinea(s, size, bold, x, color) {
      ops.push((color || "0.13 0.16 0.20") + " rg");
      ops.push("BT /" + (bold ? "F2" : "F1") + " " + size + " Tf 1 0 0 1 " + x + " " + y.toFixed(1) + " Tm (" + escaparPDF(s) + ") Tj ET");
    }
    function seccion(titulo) {
      reservar(120);
      avanzar(24);
      ops.push("0.051 0.106 0.165 rg");
      ops.push("BT /F2 11 Tf 1 0 0 1 48 " + y.toFixed(1) + " Tm (" + escaparPDF(titulo) + ") Tj ET");
      ops.push("0.72 0.76 0.80 RG 0.8 w 48 " + (y - 6).toFixed(1) + " m 564 " + (y - 6).toFixed(1) + " l S");
      y -= 9;
    }
    function fila(clave, valor) {
      var txt = (valor === undefined || valor === null || valor === "") ? "—" : String(valor);
      var lineas = envolver(txt, 10, false, ANCHO - 150);
      for (var i = 0; i < lineas.length; i++) {
        avanzar(14);
        if (i === 0) textoLinea(clave, 8.5, true, 48, "0.42 0.46 0.50");
        textoLinea(lineas[i], 10, false, 198);
      }
      y -= 1;
    }
    function filaOpt(clave, valor) { /* solo se imprime si hay dato capturado */
      if (valor === undefined || valor === null || String(valor).trim() === "" || String(valor) === "—") return;
      fila(clave, valor);
    }
    function parrafo(txt, size, bold, color) {
      var s = size || 10;
      var lineas = envolver(txt, s, !!bold, ANCHO);
      for (var i = 0; i < lineas.length; i++) {
        avanzar(s * 1.30);
        textoLinea(lineas[i], s, !!bold, 48, color);
      }
    }
    function insignia(txt, colorRGB) {
      var w = anchoTexto(txt, 10, true) + 26;
      reservar(96);
      avanzar(26);
      ops.push(colorRGB + " rg");
      ops.push("48 " + (y - 7).toFixed(1) + " " + w.toFixed(1) + " 21 re f");
      ops.push("1 1 1 rg");
      ops.push("BT /F2 10 Tf 1 0 0 1 61 " + (y - 1).toFixed(1) + " Tm (" + escaparPDF(txt) + ") Tj ET");
      y -= 16;
    }
    function firmas() {
      avanzar(48);
      ops.push("0.55 0.58 0.62 RG 0.7 w");
      ops.push("48 " + y.toFixed(1) + " m 276 " + y.toFixed(1) + " l S");
      ops.push("324 " + y.toFixed(1) + " m 552 " + y.toFixed(1) + " l S");
      y -= 12;
      textoLinea("Atendido por: " + (d.asesor || "____________"), 8.5, false, 48, "0.35 0.39 0.43");
      textoLinea("Firma del solicitante (conforme)", 8.5, false, 324, "0.35 0.39 0.43");
    }
    function pieDePagina() {
      var i = paginas.length;
      paginas.forEach(function (p, idx) {
        p.push("0.88 0.90 0.92 RG 0.7 w 48 78 m 564 78 l S");
        p.push("0.35 0.39 0.43 rg");
        p.push("BT /F1 7.5 Tf 1 0 0 1 48 64 Tm (" + escaparPDF("Documento interno del despacho. No constituye asesoría legal al solicitante. Naturalízate.pa · Lic. Alfonso Villarreal.") + ") Tj ET");
        var pag = "Página " + (idx + 1) + " de " + paginas.length;
        p.push("BT /F2 7.5 Tf 1 0 0 1 " + (564 - anchoTexto(pag, 7.5, true)).toFixed(1) + " 64 Tm (" + escaparPDF(pag) + ") Tj ET");
      });
    }

    /* ---- Contenido ---- */
    nuevaPagina();
    avanzar(6);
    parrafo("Informe de precalificación de naturalización", 17, true, "0.051 0.106 0.165");
    avanzar(6);
    parrafo("Solicitante: " + (d.nombre || "—") + "  ·  Registrado el " + generado, 9.5, false, "0.42 0.46 0.50");
    avanzar(8);

    seccion("A · DATOS DEL SOLICITANTE");
    fila("Nombre completo", d.nombre || "—");
    fila("WhatsApp", d.whatsapp || "—");
    filaOpt("Correo", d.email);
    fila("País de origen", d.pais || "—");
    fila("Años con Cédula E", d.cedula ? etiqueta("cedula", d.cedula) : "—");
    filaOpt("Ausencias prolongadas", etiqueta("ausencias", d.ausencias));
    filaOpt("Estado civil", etiqueta("civil", d.civil));
    filaOpt("Disposición al examen", etiqueta("examen", d.examen));
    if (d.dependiente) fila("¿Dependiente?", "Sí · carta de responsabilidad + solvencia del responsable");
    filaOpt("Modalidad recomendada", etiqueta("modalidad", d.modalidad));

    seccion("B · SOLVENCIA ECONÓMICA");
    fila("Pruebas disponibles", docsTexto(d));
    filaOpt("Notas de verificación", d.notas_docs);

    seccion("C · SEGUIMIENTO Y CITA");
    filaOpt("Objetivo declarado", etiqueta("objetivo", d.objetivo));
    filaOpt("Disponibilidad", etiqueta("disponibilidad", d.disponibilidad));
    filaOpt("Atendido por", d.asesor);
    var citaTxt = (d.cita_fecha ? fechaLegible(d.cita_fecha) : "") + (d.cita_hora ? (d.cita_fecha ? " · " : "") + d.cita_hora : "");
    filaOpt("Cita", citaTxt);
    filaOpt("Preferencia del solicitante", d.dia);

    seccion("D · VEREDICTO");
    var color = v.clase === "b-ok" ? "0.118 0.420 0.290" : (v.clase === "b-warn" ? "0.541 0.427 0.122" : (v.clase === "b-no" ? "0.541 0.239 0.231" : "0.60 0.63 0.66"));
    insignia(v.badge, color);
    parrafo(v.texto, 10, false);
    avanzar(4);
    parrafo("Recomendación: " + v.recomendacion, 10, true, "0.051 0.106 0.165");

    if (d.notas) {
      seccion("E · NOTAS INTERNAS");
      parrafo(d.notas, 10, false);
    }

    firmas();
    pieDePagina();
    return serializarPDF(paginas, "Informe de precalificación — " + (d.nombre || "Solicitante"));
  }

  function nombreArchivo(d) {
    var base = (d.nombre || "solicitante").normalize("NFD").replace(/[\u0300-\u036f]/g, "")
      .replace(/[^A-Za-z0-9]+/g, "-").replace(/^-+|-+$/g, "").toLowerCase() || "solicitante";
    var hoy = new Date();
    function p(n) { return (n < 10 ? "0" : "") + n; }
    return "Informe-NZQ-" + base + "-" + hoy.getFullYear() + p(hoy.getMonth() + 1) + p(hoy.getDate()) + ".pdf";
  }

  /* ══════════ 5. Interfaz ══════════ */
  var form = document.getElementById("internoForm");
  var estado = document.getElementById("estado");
  var DRAFT_KEY = "nzq_interno_v1";

  function aviso(txt, esError) {
    estado.textContent = txt;
    estado.classList.toggle("error", !!esError);
    estado.hidden = false;
    clearTimeout(aviso._t);
    aviso._t = setTimeout(function () { estado.hidden = true; }, 6000);
  }

  /* Veredicto en vivo */
  function refrescarVeredicto() {
    var v = calcularVeredicto(leerFormulario());
    var badge = document.getElementById("vBadge");
    badge.textContent = v.badge;
    badge.className = "badge " + v.clase;
    document.getElementById("vTexto").textContent = v.texto + " " + v.recomendacion;
  }

  /* Borrador */
  function guardarBorrador() {
    try {
      var datos = {};
      Array.prototype.forEach.call(form.querySelectorAll("input, select, textarea"), function (el) {
        if (!el.id) return;
        datos[el.id] = el.type === "checkbox" ? el.checked : el.value;
      });
      sessionStorage.setItem(DRAFT_KEY, JSON.stringify(datos));
    } catch (e) {}
  }
  function restaurarBorrador() {
    var datos = null;
    try { datos = JSON.parse(sessionStorage.getItem(DRAFT_KEY) || "null"); } catch (e) {}
    if (!datos) return;
    Object.keys(datos).forEach(function (id) {
      var el = document.getElementById(id);
      if (!el) return;
      if (el.type === "checkbox") el.checked = !!datos[id];
      else el.value = datos[id];
    });
    if (document.getElementById("i_pais").value === "otro") document.getElementById("i_pais_otro").style.display = "block";
    refrescarVeredicto();
  }

  document.getElementById("i_pais").addEventListener("change", function () {
    var otro = this.value === "otro";
    document.getElementById("i_pais_otro").style.display = otro ? "block" : "none";
    if (!otro) document.getElementById("i_pais_otro").value = "";
    refrescarVeredicto();
  });
  form.addEventListener("input", function () { guardarBorrador(); refrescarVeredicto(); });
  form.addEventListener("change", function () { guardarBorrador(); refrescarVeredicto(); });

  /* Validación mínima para el informe */
  function validarParaInforme(d) {
    var faltan = [];
    if (!d.nombre) faltan.push("nombre completo");
    if (!d.whatsapp) faltan.push("WhatsApp");
    if (!d.pais) faltan.push("país de origen");
    if (!d.cedula) faltan.push("años de Cédula E");
    return faltan;
  }

  /* Generar informe */
  document.getElementById("btnPDF").addEventListener("click", function () {
    var d = leerFormulario();
    var faltan = validarParaInforme(d);
    if (faltan.length) { aviso("Complete: " + faltan.join(", ") + ".", true); return; }
    try {
      var bytes = construirInformePDF(d);
      var blob = new Blob([bytes], { type: "application/pdf" });
      var url = URL.createObjectURL(blob);
      var a = document.createElement("a");
      a.href = url;
      a.download = nombreArchivo(d);
      document.body.appendChild(a);
      a.click();
      setTimeout(function () { URL.revokeObjectURL(url); a.remove(); }, 1500);
      aviso("Informe PDF generado: " + a.download);
    } catch (e) {
      aviso("No se pudo generar el PDF: " + e.message, true);
    }
  });

  /* Copiar resumen */
  function resumenTexto() {
    var d = leerFormulario();
    var v = calcularVeredicto(d);
    var l = [
      "NATURALÍZATE.pa · RESUMEN DE EVALUACIÓN",
      "Registrado: " + selloTiempo(),
      "",
      "Solicitante: " + (d.nombre || "—"),
      "WhatsApp: " + (d.whatsapp || "—"),
      "País: " + (d.pais || "—") + " · Cédula E: " + etiqueta("cedula", d.cedula),
      "Pruebas de solvencia: " + docsTexto(d),
      "Objetivo: " + etiqueta("objetivo", d.objetivo),
      "Modalidad recomendada: " + etiqueta("modalidad", d.modalidad),
      "Cita: " + (d.cita_fecha ? fechaLegible(d.cita_fecha) : "—") + (d.cita_hora ? " " + d.cita_hora : ""),
      "",
      "VEREDICTO: " + v.badge,
      v.texto,
      "Siguiente paso: " + v.recomendacion
    ];
    return l.join("\n");
  }
  document.getElementById("btnResumen").addEventListener("click", function () {
    var txt = resumenTexto();
    function listo() { aviso("Resumen copiado al portapapeles."); }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(txt).then(listo, function () { copiaManual(txt); });
    } else { copiaManual(txt); }
  });
  function copiaManual(txt) {
    var t = document.createElement("textarea");
    t.value = txt; document.body.appendChild(t); t.select();
    try { document.execCommand("copy"); aviso("Resumen copiado al portapapeles."); }
    catch (e) { aviso("No se pudo copiar automáticamente.", true); }
    t.remove();
  }

  /* WhatsApp */
  document.getElementById("btnWA").addEventListener("click", function () {
    var d = leerFormulario();
    var v = calcularVeredicto(d);
    var msg = "Hola" + (d.nombre ? " " + d.nombre.split(" ")[0] : "") + ", le escribimos de Naturalízate.pa para coordinar su Evaluación Estratégica. Veredicto preliminar: " + v.badge + ". " + v.recomendacion;
    var num = (d.whatsapp || "").replace(/\D/g, "");
    var url = "https://wa.me/" + (num.length >= 7 ? (num.length <= 8 ? "507" + num : num) : "") + "?text=" + encodeURIComponent(msg);
    window.open(url, "_blank");
  });

  /* Limpiar */
  document.getElementById("btnLimpiar").addEventListener("click", function () {
    if (!confirm("¿Borrar todos los datos del formulario? (el informe ya generado no se afecta)")) return;
    form.reset();
    document.getElementById("i_pais_otro").style.display = "none";
    try { sessionStorage.removeItem(DRAFT_KEY); } catch (e) {}
    refrescarVeredicto();
    aviso("Formulario limpio.");
  });

  /* Arranque */
  restaurarBorrador();
  refrescarVeredicto();

  /* API para pruebas y automatizaciones */
  window.NZQ = {
    leerFormulario: leerFormulario,
    calcularVeredicto: calcularVeredicto,
    construirInformePDF: construirInformePDF,
    nombreArchivo: nombreArchivo,
    resumenTexto: resumenTexto
  };
})();
</script>
