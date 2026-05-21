class AnalisisDental:
    def __init__(self):
        self.modeloActivo = "Pendiente"
        self.estadoIntegracion = "La integracion con YOLOv8 se implementara en una siguiente etapa."

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
            "titulo": "Servicio de analisis en desarrollo",
            "descripcion": "El modulo de procesamiento para la deteccion de caries dental aun se encuentra en construccion. La interfaz ya esta preparada para recibir este componente en una siguiente etapa.",
            "pendientes": [
                "Integracion del modelo YOLOv8 para estudios odontologicos.",
                "Carga de imagenes clinicas y radiografias dentales.",
                "Visualizacion de resultados del analisis asistido.",
            ],
            "formatos": ["JPG", "JPEG", "PNG", "BMP", "WEBP"],
        }

    def prepararCargaTemporal(self, archivos):
        archivosValidos = [archivo for archivo in archivos if archivo and archivo.filename]

        if not archivosValidos:
            return "Debes seleccionar al menos una imagen antes de enviar."

        return "El servicio de procesamiento aun esta en desarrollo. La carga de imagenes fue recibida solo como demostracion visual."
