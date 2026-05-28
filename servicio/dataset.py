from pathlib import Path


class DatasetCaries:
    def __init__(self, identificador="mariamosamakhalifa/adult-caries-detection-dataset"):
        self.identificador = identificador
        self.nombre = "Adult Caries Detection Dataset"

    def obtenerEstado(self):
        return {
            "nombre": self.nombre,
            "identificador": self.identificador,
            "descripcion": "Dataset publico de Kaggle preparado para la etapa de entrenamiento del modelo de deteccion de caries.",
            "uso": "Se utilizara para revisar imagenes, etiquetas y preparar el entrenamiento futuro con YOLOv8.",
            "ruta": "Pendiente de descarga",
            "disponible": False,
            "indicadores": [
                {"valor": "Kaggle", "texto": "origen del dataset"},
                {"valor": "Caries", "texto": "clase clinica objetivo"},
                {"valor": "YOLOv8", "texto": "motor de entrenamiento"},
            ],
            "aplicaciones": [
                "Construir el conjunto de entrenamiento y validacion.",
                "Preparar etiquetas para deteccion de lesiones cariosas.",
                "Respaldar la evolucion del sistema hacia inferencia real.",
            ],
        }

    def descargar(self):
        try:
            import kagglehub
        except ImportError:
            return {
                "ok": False,
                "mensaje": "La dependencia kagglehub no esta instalada. Ejecuta: pip install -r requirements.txt",
                "ruta": "",
            }

        try:
            ruta = Path(kagglehub.dataset_download(self.identificador))
        except Exception as error:
            return {
                "ok": False,
                "mensaje": f"No se pudo descargar el dataset desde Kaggle: {error}",
                "ruta": "",
            }

        return {
            "ok": True,
            "mensaje": "Dataset descargado correctamente desde Kaggle.",
            "ruta": str(ruta),
        }
