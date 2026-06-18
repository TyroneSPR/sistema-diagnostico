class AnalisisDental:
    def __init__(self):
        self.modeloActivo = "YOLOv8 proximamente"
        self.estadoIntegracion = "YOLOv8 sera el evento estrella del sistema: el modulo de inteligencia artificial para deteccion asistida de caries se mantiene anunciado como proxima integracion."

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

    def obtenerEstadoYoloProximo(self):
        return {
            "nombre": "YOLOv8",
            "rutaModelo": "Lanzamiento proximamente",
            "modeloDisponible": False,
            "estado": "Proximamente",
            "confianza": 0,
            "descripcion": "El modulo YOLOv8 sera el evento estrella de la plataforma: una futura experiencia de vision artificial para apoyar la deteccion de caries en estudios dentales.",
        }

    def obtenerApartados(self):
        return [
            {
                "titulo": "Deteccion de caries",
                "descripcion": "Apartado para orientar la identificacion temprana de signos visuales compatibles con caries.",
                "endpoint": "deteccionCaries",
            },
            {
                "titulo": "Analisis radiografico",
                "descripcion": "Pagina dedicada a la revision ordenada de estudios radiograficos dentales.",
                "endpoint": "radiografias",
            },
            {
                "titulo": "Revision clinica",
                "descripcion": "Herramientas para preparar imagenes intraorales antes de una evaluacion profesional.",
                "endpoint": "revisionClinica",
            },
            {
                "titulo": "YOLOv8",
                "descripcion": "El lanzamiento estrella de inteligencia artificial, anunciado como proxima etapa del sistema.",
                "endpoint": "yoloProximamente",
            },
        ]

    def obtenerApartado(self, clave):
        apartados = {
            "deteccion": {
                "insignia": "Apartado clinico",
                "titulo": "Deteccion de caries",
                "descripcion": "Organiza criterios visuales para reconocer lesiones sospechosas y preparar una evaluacion odontologica mas clara.",
                "imagen": "img/deteccion.svg",
                "acciones": [
                    "Registrar manchas oscuras persistentes.",
                    "Observar sensibilidad asociada a frio, dulce o masticacion.",
                    "Priorizar controles cuando exista cavidad visible o retencion de alimento.",
                ],
                "destacado": "Este apartado no reemplaza el diagnostico profesional; ayuda a ordenar la observacion antes de usar el centro de analisis.",
                "estrella": False,
            },
            "radiografias": {
                "insignia": "Imagenologia dental",
                "titulo": "Analisis de radiografias",
                "descripcion": "Espacio para preparar radiografias, revisar calidad visual y organizar hallazgos antes de la interpretacion clinica.",
                "imagen": "img/radiografia.svg",
                "acciones": [
                    "Verificar contraste y nitidez del estudio.",
                    "Confirmar que las piezas dentales relevantes sean visibles.",
                    "Separar imagenes por paciente, fecha y tipo de estudio.",
                ],
                "destacado": "Una buena radiografia mejora la lectura del especialista y prepara mejor la futura inferencia asistida.",
                "estrella": False,
            },
            "revision": {
                "insignia": "Control de estudio",
                "titulo": "Revision de imagenes clinicas",
                "descripcion": "Modulo enfocado en revisar fotografias clinicas, comprobar privacidad y preparar archivos antes de cargarlos.",
                "imagen": "img/analisis.svg",
                "acciones": [
                    "Evitar datos personales visibles en la imagen.",
                    "Revisar encuadre, iluminacion y enfoque.",
                    "Seleccionar solo archivos utiles para el flujo clinico.",
                ],
                "destacado": "La preparacion correcta reduce errores y mejora la utilidad del centro de analisis.",
                "estrella": False,
            },
            "yolo": {
                "insignia": "Evento estrella",
                "titulo": "YOLOv8 proximamente",
                "descripcion": "La gran novedad de la plataforma sera la integracion de YOLOv8 para deteccion asistida de caries en imagenes dentales.",
                "imagen": "img/analisis.svg",
                "acciones": [
                    "Deteccion visual asistida sobre estudios dentales.",
                    "Resultados graficos con zonas sospechosas resaltadas.",
                    "Base preparada para evolucionar hacia reportes clinicos mas completos.",
                ],
                "destacado": "YOLOv8 queda anunciado como el evento estrella: pronto sera el modulo principal de inteligencia artificial del sistema.",
                "estrella": True,
            },
        }

        return apartados.get(clave, apartados["deteccion"])

    def prepararCargaTemporal(self, archivos):
        archivosValidos = [archivo for archivo in archivos if archivo and archivo.filename]

        if not archivosValidos:
            return "Debes seleccionar al menos una imagen antes de enviar."

        return "Las imagenes fueron recibidas correctamente. El motor de analisis clinico se activara en la siguiente etapa del sistema."

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
                    "estado": "Preparado para revision previa",
                    "detecciones": "YOLOv8 proximamente",
                    "imagen": "",
                }
            )

        return {
            "ok": True,
            "titulo": "Estudio preparado",
            "mensaje": "Las imagenes quedaron listas para revision. La deteccion automatica con YOLOv8 sera el evento estrella de una proxima version.",
            "resultados": resultados,
        }
