document.addEventListener("DOMContentLoaded", () => {
    prepararVistaPreviaArchivos();
    prepararChecklist();
    prepararPrioridadClinica();
    prepararEducacionDental();
});

function prepararVistaPreviaArchivos() {
    const entrada = document.querySelector("[data-visor-archivos]");
    const panel = document.querySelector("[data-panel-archivos]");
    if (!entrada || !panel) return;

    entrada.addEventListener("change", () => {
        const archivos = Array.from(entrada.files || []);
        if (!archivos.length) {
            panel.innerHTML = "<div><strong>Sin archivos seleccionados</strong><span>La vista previa aparecera aqui antes de preparar el estudio.</span></div>";
            return;
        }

        const totalMb = archivos.reduce((suma, archivo) => suma + archivo.size, 0) / 1024 / 1024;
        const elementos = archivos.slice(0, 6).map((archivo) => {
            const esImagen = archivo.type.startsWith("image/");
            const url = esImagen ? URL.createObjectURL(archivo) : "";
            const nombre = escaparHtml(archivo.name);
            return `
                <article class="archivoPreview">
                    ${url ? `<img src="${url}" alt="Vista previa de ${nombre}">` : "<span>IMG</span>"}
                    <div>
                        <strong>${nombre}</strong>
                        <small>${(archivo.size / 1024 / 1024).toFixed(2)} MB</small>
                    </div>
                </article>
            `;
        }).join("");

        panel.innerHTML = `
            <div class="resumenArchivos">
                <strong>${archivos.length} archivo(s) listos</strong>
                <span>Peso total aproximado: ${totalMb.toFixed(2)} MB</span>
            </div>
            <div class="rejillaPreview">${elementos}</div>
        `;
    });
}

function prepararChecklist() {
    const panel = document.querySelector("[data-checklist-estudio]");
    if (!panel) return;

    const items = Array.from(panel.querySelectorAll("[data-check-item]"));
    const progreso = panel.querySelector("[data-check-progress]");
    const texto = panel.querySelector("[data-check-texto]");

    const actualizar = () => {
        const completos = items.filter((item) => item.checked).length;
        const porcentaje = Math.round((completos / items.length) * 100);
        progreso.style.width = `${porcentaje}%`;
        texto.textContent = `${porcentaje}% listo para revision`;
    };

    items.forEach((item) => item.addEventListener("change", actualizar));
    actualizar();
}

function prepararPrioridadClinica() {
    const panel = document.querySelector("[data-prioridad-clinica]");
    if (!panel) return;

    const campos = Array.from(panel.querySelectorAll("[data-prioridad-campo]"));
    const resultado = panel.querySelector("[data-prioridad-resultado]");

    const actualizar = () => {
        const puntaje = campos.reduce((suma, campo) => suma + Number(campo.value), 0);
        if (puntaje >= 6) {
            resultado.textContent = "Alta prioridad: revisar el caso cuanto antes.";
            resultado.dataset.nivel = "alto";
        } else if (puntaje >= 3) {
            resultado.textContent = "Prioridad media: programar evaluacion clinica.";
            resultado.dataset.nivel = "medio";
        } else {
            resultado.textContent = "Baja prioridad: seguimiento preventivo.";
            resultado.dataset.nivel = "bajo";
        }
    };

    campos.forEach((campo) => campo.addEventListener("change", actualizar));
    actualizar();
}

function prepararEducacionDental() {
    const panel = document.querySelector("[data-educacion-dental]");
    if (!panel) return;

    const criterios = Array.from(panel.querySelectorAll("[data-criterio]"));
    const salida = panel.querySelector("[data-resultado-educacion]");

    const actualizar = () => {
        const puntaje = criterios.reduce((suma, criterio) => suma + (criterio.checked ? Number(criterio.value) : 0), 0);
        if (puntaje >= 6) {
            salida.textContent = "Prioridad alta: conviene llevar el estudio al centro de analisis.";
        } else if (puntaje >= 3) {
            salida.textContent = "Prioridad media: observa evolucion y prepara una revision.";
        } else if (puntaje > 0) {
            salida.textContent = "Prioridad baja: refuerza prevencion y seguimiento.";
        } else {
            salida.textContent = "Selecciona criterios para ver la prioridad sugerida.";
        }
    };

    criterios.forEach((criterio) => criterio.addEventListener("change", actualizar));
    actualizar();
}

function escaparHtml(texto) {
    const mapa = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#039;",
    };
    return texto.replace(/[&<>"']/g, (caracter) => mapa[caracter]);
}
