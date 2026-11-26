const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.getElementById("nav-links");
const dropdowns = [...document.querySelectorAll("[data-dropdown]")];
const mobileView = window.matchMedia("(max-width: 860px)");

function closeDropdowns(except = null) {
  dropdowns.forEach((item) => {
    if (item === except) return;
    item.classList.remove("is-open");
    const button = item.querySelector(".nav-caret");
    button.setAttribute("aria-expanded", "false");
    button.setAttribute("aria-label", button.getAttribute("aria-label").replace("Cerrar", "Abrir"));
  });
}

function closeMenu() {
  navLinks.classList.remove("is-open");
  document.body.classList.remove("menu-open");
  menuToggle.setAttribute("aria-expanded", "false");
  menuToggle.setAttribute("aria-label", "Abrir menú");
  closeDropdowns();
}

menuToggle.addEventListener("click", () => {
  const open = navLinks.classList.toggle("is-open");
  document.body.classList.toggle("menu-open", open && mobileView.matches);
  menuToggle.setAttribute("aria-expanded", String(open));
  menuToggle.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
  if (!open) closeDropdowns();
});

dropdowns.forEach((item) => {
  const button = item.querySelector(".nav-caret");
  button.addEventListener("click", () => {
    const open = !item.classList.contains("is-open");
    closeDropdowns(item);
    item.classList.toggle("is-open", open);
    button.setAttribute("aria-expanded", String(open));
    button.setAttribute("aria-label", `${open ? "Cerrar" : "Abrir"} submenú de ${item.querySelector(".nav-link").textContent.trim()}`);
  });
});

navLinks.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    if (mobileView.matches) closeMenu();
    else closeDropdowns();
  });
});
mobileView.addEventListener("change", () => closeMenu());

const searchForm = document.getElementById("site-search");
const searchInput = document.getElementById("search-input");
const searchResults = document.getElementById("search-results");
const searchEntries = [
  { title: "El despacho", detail: "Lic. Alfonso Villarreal", href: "index.html", terms: "inicio abogado oficina perfil" },
  { title: "Áreas de práctica", detail: "Servicios de naturalización", href: "servicios.html", terms: "evaluacion expediente representacion seguimiento" },
  { title: "Evaluación de viabilidad", detail: "Revisión inicial del caso", href: "servicios.html#evaluacion", terms: "cedula e residencia elegibilidad" },
  { title: "Vías de naturalización", detail: "Residencia, reciprocidad y vínculos", href: "vias.html", terms: "pais origen arraigo familiar" },
  { title: "Auditoría Jurídica de Caso", detail: "US$49 · evaluación profesional", href: "index.html#auditoria", terms: "precio costo 49 auditoria abogado llamada" },
  { title: "Evaluar mi situación", detail: "Formulario de calificación", href: "index.html#calificacion", terms: "formulario preguntas whatsapp calificacion" },
  { title: "Honorarios", detail: "Alcance y propuesta por escrito", href: "honorarios.html", terms: "precios tarifas costos" },
  { title: "Guía de requisitos", detail: "Guía completa del despacho", href: "guia.html", terms: "cedula e documentos requisitos" },
  { title: "Solvencia económica", detail: "Pruebas documentales", href: "informacion-legal.html#solvencia", terms: "ingresos carta bancaria trabajo" },
  { title: "Etapas del proceso", detail: "Presentación y juramentación", href: "informacion-legal.html#proceso", terms: "tribunal electoral migracion examen" },
  { title: "Enlaces oficiales", detail: "Tribunal Electoral y Migración", href: "informacion-legal.html#enlaces-oficiales", terms: "gobierno instituciones" },
  { title: "Lista de verificación", detail: "Prepárese para una consulta", href: "verificacion.html", terms: "herramienta checklist revisar" },
  { title: "Contáctenos", detail: "Formulario, WhatsApp y ubicación", href: "contacto.html", terms: "correo telefono direccion scotia plaza" },
  { title: "Aviso legal", detail: "Información y enlaces externos", href: "aviso-legal.html", terms: "descargo privacidad" },
];

function normalize(text) {
  return text.normalize("NFD").replace(/\p{M}/gu, "").toLowerCase();
}

function hideSearch() {
  searchResults.hidden = true;
  searchResults.replaceChildren();
}

function renderSearch() {
  const query = searchInput.value.trim();
  if (query.length < 2) return hideSearch();
  const words = normalize(query).split(/\s+/).filter(Boolean);
  const matches = searchEntries.filter((entry) => {
    const text = normalize(`${entry.title} ${entry.detail} ${entry.terms}`);
    return words.every((word) => text.includes(word));
  });
  searchResults.replaceChildren();
  if (!matches.length) {
    const empty = document.createElement("p");
    empty.textContent = "Sin resultados. Pruebe con “requisitos”, “servicios” o “contacto”.";
    searchResults.append(empty);
  } else {
    matches.forEach((entry) => {
      const link = document.createElement("a");
      link.href = entry.href;
      const label = document.createElement("span");
      const title = document.createElement("strong");
      const detail = document.createElement("small");
      title.textContent = entry.title;
      detail.textContent = entry.detail;
      label.append(title, detail);
      const arrow = document.createElement("span");
      arrow.textContent = "↗";
      arrow.setAttribute("aria-hidden", "true");
      link.append(label, arrow);
      link.addEventListener("click", hideSearch);
      searchResults.append(link);
    });
  }
  searchResults.hidden = false;
}

searchInput.addEventListener("input", renderSearch);
searchInput.addEventListener("focus", renderSearch);
searchInput.addEventListener("keydown", (event) => {
  if (event.key === "ArrowDown" && !searchResults.hidden) {
    const first = searchResults.querySelector("a");
    if (first) {
      event.preventDefault();
      first.focus();
    }
  }
  if (event.key === "Escape") hideSearch();
});
searchForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const first = searchResults.querySelector("a");
  if (first) first.click();
  else renderSearch();
});

document.addEventListener("click", (event) => {
  if (!searchForm.contains(event.target) && !searchResults.contains(event.target)) hideSearch();
  if (!event.target.closest("[data-dropdown]")) closeDropdowns();
  if (mobileView.matches && !event.target.closest(".site-nav")) closeMenu();
});
document.addEventListener("keydown", (event) => {
  if (event.key === "Escape") {
    hideSearch();
    closeMenu();
  }
  if (event.key === "/" && !/^(INPUT|TEXTAREA)$/.test(document.activeElement.tagName)) {
    event.preventDefault();
    searchInput.focus();
  }
});

const WA_NUMBER = "50762557583";

function openWhatsApp(message) {
  const anchor = document.createElement("a");
  anchor.href = `https://wa.me/${WA_NUMBER}?text=${encodeURIComponent(message)}`;
  anchor.target = "_blank";
  anchor.rel = "noopener noreferrer";
  anchor.hidden = true;
  document.body.append(anchor);
  anchor.click();
  anchor.remove();
}

const formLabels = {
  nombre: "Nombre",
  correo: "Correo electrónico",
  telefono: "Teléfono o WhatsApp",
  pais: "País de origen",
  mensaje: "Mensaje",
};

for (const form of document.querySelectorAll("[data-wa-form]")) {
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    const values = new FormData(form);
    const lines = ["Hola, les escribo desde el sitio de Naturalízate.pa."];
    for (const [key, value] of values.entries()) {
      if (key === "novedades") continue;
      const text = String(value).trim();
      if (text) lines.push(`${formLabels[key] || key}: ${text}`);
    }
    lines.push(`Novedades legales: ${values.has("novedades") ? "Sí" : "No"}`);
    openWhatsApp(lines.join("\n"));
    form.querySelector("[data-form-status]").textContent = "Se abrió WhatsApp con sus datos. Revise el mensaje y envíelo desde su aplicación; si no se abre, escriba al +507 6255-7583.";
  });
}

const checkboxes = [...document.querySelectorAll("[data-check-item]")];
if (checkboxes.length) {
  const count = document.getElementById("checklist-count");
  const bar = document.querySelector(".progress-track");
  const fill = document.getElementById("checklist-progress");
  const contact = document.getElementById("checklist-whatsapp");
  const update = () => {
    const checked = checkboxes.filter((item) => item.checked).length;
    count.textContent = `${checked} de ${checkboxes.length} elementos marcados`;
    bar.setAttribute("aria-valuenow", String(checked));
    fill.style.width = `${checked / checkboxes.length * 100}%`;
    const message = `Hola, estoy organizando mi consulta sobre naturalización en Panamá. Revisé ${checked} de ${checkboxes.length} puntos de su lista orientativa y quisiera hablar de mi caso.`;
    contact.href = `https://wa.me/50762557583?text=${encodeURIComponent(message)}`;
  };
  checkboxes.forEach((checkbox) => checkbox.addEventListener("change", update));
  update();
}

const mapButton = document.querySelector("[data-load-map]");
if (mapButton) {
  mapButton.addEventListener("click", () => {
    const iframe = document.createElement("iframe");
    iframe.title = "Mapa de Scotia Plaza, Avenida Federico Boyd, Ciudad de Panamá";
    iframe.loading = "lazy";
    iframe.referrerPolicy = "no-referrer-when-downgrade";
    iframe.src = "https://www.google.com/maps?q=Scotia+Plaza+Av+Federico+Boyd+Panama&output=embed";
    mapButton.closest("[data-map-container]").replaceChildren(iframe);
  });
}

for (const button of document.querySelectorAll("[data-share]")) {
  button.addEventListener("click", async () => {
    const status = button.parentElement.querySelector("[data-share-status]");
    if (navigator.share) {
      try {
        await navigator.share({ title: document.title, url: location.href });
        status.textContent = "Página compartida desde su dispositivo.";
        return;
      } catch (error) {
        if (error.name === "AbortError") return;
      }
    }
    try {
      await navigator.clipboard.writeText(location.href);
      status.textContent = "Enlace copiado al portapapeles.";
    } catch {
      status.textContent = "Copie el enlace desde la barra de direcciones.";
    }
  });
}

for (const item of document.querySelectorAll(".faq-item")) {
  const button = item.querySelector(".faq-q");
  const panel = item.querySelector(".faq-a");
  button.addEventListener("click", () => {
    const open = button.getAttribute("aria-expanded") !== "true";
    button.setAttribute("aria-expanded", String(open));
    panel.hidden = !open;
  });
}

const qualForm = document.querySelector("[data-qual-form]");
if (qualForm) {
  const fields = [...qualForm.querySelectorAll("[data-qual-field]")];
  const countLabel = document.getElementById("qual-count");
  const bar = qualForm.querySelector(".progress-track");
  const fill = document.getElementById("qual-progress");
  const status = qualForm.querySelector("[data-qual-status]");
  const update = () => {
    const filled = fields.filter((field) => field.value).length;
    countLabel.textContent = `${filled} de ${fields.length} respondidas`;
    bar.setAttribute("aria-valuenow", String(filled));
    fill.style.width = `${(filled / fields.length) * 100}%`;
  };
  fields.forEach((field) => field.addEventListener("change", update));
  update();
  qualForm.addEventListener("submit", (event) => {
    event.preventDefault();
    if (!qualForm.reportValidity()) return;
    const lines = fields.map((field) => `${field.name}: ${field.value}`);
    const message = [
      "Hola, completé el formulario de calificación de Naturalízate.pa.",
      "",
      ...lines,
    ].join("\n");
    openWhatsApp(message);
    status.textContent = "Se preparó el mensaje de WhatsApp con sus respuestas. Revíselo y envíelo desde su aplicación.";
  });
}

document.getElementById("year").textContent = new Date().getFullYear();
