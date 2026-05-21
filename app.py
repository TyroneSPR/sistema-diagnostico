import os

from flask import Flask, redirect, render_template, request, session, url_for

from servicio.analisis import AnalisisDental


app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = os.environ.get("SECRET_KEY", "diagnosticoDentalDemo")
analisis = AnalisisDental()


@app.route("/", methods=["GET", "POST"])
def login():
    correo = ""
    mensaje = ""

    if request.method == "POST":
        correo = request.form.get("correo", "").strip()
        accesoValido = analisis.validarCorreo(correo)

        if accesoValido:
            session["correo"] = correo
            return redirect(url_for("inicio"))

        mensaje = "El correo electronico no tiene un formato valido."

    return render_template("login.html", correo=correo, mensaje=mensaje, tituloPagina="Ingreso al Sistema")


@app.route("/inicio")
def inicio():
    if "correo" not in session:
        return redirect(url_for("login"))

    datosVista = {
        "titulo": "Diagnostico Dental Asistido",
        "subtitulo": "Sistema de apoyo clinico para la deteccion de caries en imagenes y radiografias dentales.",
        "correo": session.get("correo", ""),
    }
    return render_template("index.html", datosVista=datosVista, tituloPagina="Diagnostico Dental Asistido")


@app.route("/acerca-de")
def acercaDe():
    datosProyecto = analisis.obtenerResumenProyecto()
    return render_template("acerca.html", datosProyecto=datosProyecto, tituloPagina="Acerca del Proyecto")


@app.route("/servicio", methods=["GET", "POST"])
def servicio():
    if "correo" not in session:
        return redirect(url_for("login"))

    datosServicio = analisis.obtenerEstadoServicio()
    mensajeProceso = ""

    if request.method == "POST":
        archivos = request.files.getlist("imagenes")
        mensajeProceso = analisis.prepararCargaTemporal(archivos)

    return render_template(
        "servicio.html",
        datosServicio=datosServicio,
        mensajeProceso=mensajeProceso,
        tituloPagina="Servicio en Desarrollo",
    )


@app.route("/salir")
def salir():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
