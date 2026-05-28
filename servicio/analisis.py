class AnalisisDental:
    def __init__(self):
        self.modeloActivo = "En preparacion clinica"
        self.estadoIntegracion = "La plataforma se encuentra preparada para incorporar analisis asistido sobre imagenes odontologicas."

    def validarCorreo(self, correo):
        if not correo:
            return False

        if "@" not in correo or "." not in correo:
            return False

        return True

    def obtenerResumenProyecto(self):
        return {
            "nombre": "Sistema de Diagnostico Asistido por Computadora",
            "objetivo": "Apoyar al personal odontologico en la deteccion oportuna de caries dental mediante el analisis de imagenes clinicas y radiografias dentales.",
            "alcance": "La interfaz actual presenta el proyecto, organiza el acceso al servicio y deja preparado el punto de integracion futura con YOLOv8.",
            "estadoModelo": self.modeloActivo,
            "pendienteModelo": self.estadoIntegracion,
        }

    def obtenerEstadoServicio(self):
        return {
            "titulo": "Centro de analisis odontologico",
            "descripcion": "Carga estudios dentales en un entorno organizado para revision asistida. La experiencia esta disenada para presentar resultados de forma clara, sobria y alineada con un flujo clinico profesional.",
            "pendientes": [
                "Recepcion segura de imagenes clinicas y radiografias dentales.",
                "Preparacion del estudio para analisis asistido.",
                "Presentacion visual de hallazgos para apoyo profesional.",
            ],
            "formatos": ["JPG", "JPEG", "PNG", "BMP", "WEBP"],
        }

    def prepararCargaTemporal(self, archivos):
        archivosValidos = [archivo for archivo in archivos if archivo and archivo.filename]

        if not archivosValidos:
            return "Debes seleccionar al menos una imagen antes de enviar."

        return "Las imagenes fueron recibidas correctamente. El motor de analisis clinico se activara en la siguiente etapa del sistema."
