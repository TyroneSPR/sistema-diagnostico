class AnalisisDental:
    def __init__(self):
        self.modeloActivo = "YOLOv8 proximamente"
        self.estadoIntegracion = "La experiencia de inteligencia artificial mas esperada de la plataforma llegara con YOLOv8 para potenciar la revision visual de estudios dentales."

    def validarCorreo(self, correo):
        if not correo:
            return False

        if "@" not in correo or "." not in correo:
            return False

        return True

    def obtenerResumenProyecto(self):
        return {
            "nombre": "Salud Oral Digital",
            "objetivo": "Un entorno clinico para organizar estudios dentales, orientar la revision visual y acompanar decisiones profesionales con mayor claridad.",
            "alcance": "Gestion de estudios, evaluacion preliminar, priorizacion de casos y una experiencia visual orientada al trabajo odontologico moderno.",
            "estadoModelo": self.modeloActivo,
            "pendienteModelo": self.estadoIntegracion,
        }

    def obtenerEstadoServicio(self):
        return {
            "titulo": "Centro de analisis odontologico",
            "descripcion": "Carga radiografias o imagenes clinicas, revisa su calidad y ordena la prioridad de atencion desde un panel profesional.",
            "pendientes": [
                "Recepcion ordenada de imagenes clinicas y radiografias dentales.",
                "Control de calidad antes de la revision profesional.",
                "Priorizacion clara para orientar el siguiente paso clinico.",
            ],
            "formatos": ["JPG", "JPEG", "PNG", "BMP", "WEBP"],
        }

    def obtenerEstadoYoloProximo(self):
        return {
            "nombre": "YOLOv8",
            "rutaModelo": "Lanzamiento proximamente",
            "modeloDisponible": False,
            "estado": "Proximamente",
            "confianza": 0,
            "descripcion": "El lanzamiento estrella de la plataforma incorporara vision artificial YOLOv8 para resaltar posibles zonas de interes en estudios dentales.",
        }

    def obtenerApartados(self):
        return [
            {
                "titulo": "Deteccion de caries",
                "descripcion": "Orienta la revision de signos visuales relevantes para detectar lesiones cariosas con mayor orden.",
                "endpoint": "deteccionCaries",
            },
            {
                "titulo": "Analisis radiografico",
                "descripcion": "Revisa la calidad, visibilidad y preparacion de radiografias dentales.",
                "endpoint": "radiografias",
            },
            {
                "titulo": "Revision clinica",
                "descripcion": "Prepara imagenes intraorales con criterios de privacidad, enfoque y utilidad.",
                "endpoint": "revisionClinica",
            },
            {
                "titulo": "YOLOv8",
                "descripcion": "La experiencia estrella de inteligencia artificial para el analisis visual dental.",
                "endpoint": "yoloProximamente",
            },
        ]

    def obtenerApartado(self, clave):
        apartados = {
            "deteccion": {
                "insignia": "Apartado clinico",
                "titulo": "Deteccion de caries",
                "descripcion": "Prioriza signos visuales y sintomas asociados para orientar una revision odontologica mas precisa.",
                "imagen": "img/deteccion.svg",
                "acciones": [
                    "Manchas oscuras o cambios de color.",
                    "Sensibilidad al frio, dulce o presion.",
                    "Cavidades visibles o retencion de alimento.",
                ],
                "destacado": "Una revision temprana facilita decisiones preventivas y tratamientos menos invasivos.",
                "estrella": False,
            },
            "radiografias": {
                "insignia": "Imagenologia dental",
                "titulo": "Analisis de radiografias",
                "descripcion": "Controla la calidad del estudio radiografico antes de avanzar con la evaluacion clinica.",
                "imagen": "img/radiografia.svg",
                "acciones": [
                    "Contraste y nitidez suficientes.",
                    "Piezas dentales relevantes visibles.",
                    "Archivos ordenados por fecha y tipo de estudio.",
                ],
                "destacado": "La calidad de imagen es clave para una lectura profesional clara.",
                "estrella": False,
            },
            "revision": {
                "insignia": "Control de estudio",
                "titulo": "Revision de imagenes clinicas",
                "descripcion": "Prepara fotografias clinicas con criterios de enfoque, privacidad y utilidad para consulta.",
                "imagen": "img/analisis.svg",
                "acciones": [
                    "Datos personales fuera de la imagen.",
                    "Encuadre, iluminacion y enfoque correctos.",
                    "Seleccion de imagenes utiles para revision.",
                ],
                "destacado": "Un estudio bien preparado acelera la revision y reduce repeticiones.",
                "estrella": False,
            },
            "yolo": {
                "insignia": "Evento estrella",
                "titulo": "YOLOv8 proximamente",
                "descripcion": "La proxima experiencia premium de Salud Oral Digital incorporara vision artificial para resaltar posibles zonas de interes.",
                "imagen": "img/analisis.svg",
                "acciones": [
                    "Analisis visual asistido de estudios dentales.",
                    "Zonas de interes resaltadas sobre la imagen.",
                    "Reportes visuales mas claros para consulta profesional.",
                ],
                "destacado": "YOLOv8 sera el gran lanzamiento de la plataforma.",
                "estrella": True,
            },
        }

        return apartados.get(clave, apartados["deteccion"])

    def prepararCargaTemporal(self, archivos):
        archivosValidos = [archivo for archivo in archivos if archivo and archivo.filename]

        if not archivosValidos:
            return "Debes seleccionar al menos una imagen antes de enviar."

        return "Las imagenes fueron recibidas correctamente y quedaron disponibles para revision clinica."

    def prepararEstudio(self, archivos):
        archivosValidos = [archivo for archivo in archivos if archivo and archivo.filename]

        if not archivosValidos:
            return {
                "ok": False,
                "titulo": "Sin imagenes",
                "mensaje": "Debes seleccionar al menos una imagen antes de preparar el estudio.",
                "resultados": [],
            }

        resultados = []
        for archivo in archivosValidos:
            resultados.append(
                {
                    "archivo": archivo.filename,
                    "estado": "Listo para revision",
                    "detecciones": "Prioridad registrada",
                    "imagen": "",
                }
            )

        return {
            "ok": True,
            "titulo": "Estudio listo",
            "mensaje": "Las imagenes fueron recibidas y quedaron organizadas para su revision.",
            "resultados": resultados,
        }
