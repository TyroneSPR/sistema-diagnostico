import os
from datetime import timedelta
from functools import wraps

from flask import Flask, redirect, render_template, request, session, url_for

from servicio.analisis import AnalisisDental
from servicio.dataset import DatasetCaries


app = Flask(__name__, static_folder="static", template_folder="templates")
app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY", "diagnosticoDentalDemo"),
    PERMANENT_SESSION_LIFETIME=timedelta(hours=8),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
    SESSION_COOKIE_SECURE=os.environ.get("SESSION_COOKIE_SECURE", "false").lower() == "true",
)
analisis = AnalisisDental()
datasetCaries = DatasetCaries()


def requiereSesion(funcion):
    @wraps(funcion)
    def envoltura(*args, **kwargs):
        if "correo" not in session:
            session["siguiente"] = request.path
            return redirect(url_for("login"))

        return funcion(*args, **kwargs)

    return envoltura


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "GET" and "correo" in session:
        return redirect(url_for("inicio"))

    correo = ""
    mensaje = ""

    if request.method == "POST":
        correo = request.form.get("correo", "").strip()
        accesoValido = analisis.validarCorreo(correo)

        if accesoValido:
            session.permanent = True
            session["correo"] = correo
            destino = session.pop("siguiente", None)
            return redirect(destino or url_for("inicio"))

        mensaje = "El correo electronico no tiene un formato valido."

    return render_template("login.html", correo=correo, mensaje=mensaje, tituloPagina="Ingreso al Sistema")


@app.route("/inicio")
@requiereSesion
def inicio():
    datosVista = {
        "titulo": "Diagnostico Dental Asistido",
        "subtitulo": "Sistema de apoyo clinico para la deteccion de caries en imagenes y radiografias dentales.",
        "correo": session.get("correo", ""),
        "apartados": analisis.obtenerApartados(),
    }
    return render_template("index.html", datosVista=datosVista, tituloPagina="Diagnostico Dental Asistido")


@app.route("/acerca-de")
@requiereSesion
def acercaDe():
    datosProyecto = analisis.obtenerResumenProyecto()
    return render_template("acerca.html", datosProyecto=datosProyecto, tituloPagina="Acerca del Proyecto")


@app.route("/servicio", methods=["GET", "POST"])
@requiereSesion
def servicio():
    datosServicio = analisis.obtenerEstadoServicio()
    estadoYolo = analisis.obtenerEstadoYoloProximo()
    resultadoAnalisis = None

    if request.method == "POST":
        archivos = request.files.getlist("imagenes")
        resultadoAnalisis = analisis.prepararEstudio(archivos)

    return render_template(
        "servicio.html",
        datosServicio=datosServicio,
        estadoYolo=estadoYolo,
        resultadoAnalisis=resultadoAnalisis,
        tituloPagina="Centro de Analisis Odontologico",
    )


@app.route("/deteccion-caries")
@requiereSesion
def deteccionCaries():
    return render_template(
        "apartado.html",
        datosApartado=analisis.obtenerApartado("deteccion"),
        tituloPagina="Deteccion de Caries",
    )


@app.route("/radiografias")
@requiereSesion
def radiografias():
    return render_template(
        "apartado.html",
        datosApartado=analisis.obtenerApartado("radiografias"),
        tituloPagina="Analisis de Radiografias",
    )


@app.route("/revision-clinica")
@requiereSesion
def revisionClinica():
    return render_template(
        "apartado.html",
        datosApartado=analisis.obtenerApartado("revision"),
        tituloPagina="Revision de Imagenes Clinicas",
    )


@app.route("/yolov8-proximamente")
@requiereSesion
def yoloProximamente():
    return render_template(
        "apartado.html",
        datosApartado=analisis.obtenerApartado("yolo"),
        tituloPagina="YOLOv8 Proximamente",
    )


@app.route("/dataset", methods=["GET", "POST"])
@requiereSesion
def dataset():
    datosDataset = datasetCaries.obtenerEstado()
    resultadoDataset = None

    if request.method == "POST":
        resultadoDataset = datasetCaries.descargar()

    return render_template(
        "dataset.html",
        datosDataset=datosDataset,
        resultadoDataset=resultadoDataset,
        tituloPagina="Dataset de Caries",
    )


@app.route("/salir")
def salir():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", "5000"))
    modoDebug = os.environ.get("FLASK_DEBUG", "true").lower() == "true"
    app.run(host="0.0.0.0", port=puerto, debug=modoDebug)
