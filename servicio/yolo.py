import os
from pathlib import Path
from uuid import uuid4

from werkzeug.utils import secure_filename


class MotorYoloV8:
    def __init__(self, rutaModelo=None, carpetaResultados=None):
        self.rutaModelo = Path(rutaModelo or os.environ.get("YOLO_MODEL_PATH", "models/caries_yolov8.pt"))
        self.carpetaResultados = Path(carpetaResultados or "static/resultados")
        self.formatosPermitidos = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
        self.confianza = float(os.environ.get("YOLO_CONFIDENCE", "0.25"))
        self._modelo = None

    def obtenerEstado(self):
        modeloDisponible = self.rutaModelo.exists()

        return {
            "nombre": "YOLOv8",
            "rutaModelo": str(self.rutaModelo),
            "modeloDisponible": modeloDisponible,
            "estado": "Modelo clinico disponible" if modeloDisponible else "Esperando modelo entrenado",
            "confianza": self.confianza,
            "descripcion": "Motor de deteccion preparado para analizar imagenes dentales con un modelo YOLOv8 entrenado en caries.",
        }

    def analizar(self, archivos):
        archivosValidos = [archivo for archivo in archivos if archivo and archivo.filename]

        if not archivosValidos:
            return {
                "ok": False,
                "titulo": "Sin imagenes",
                "mensaje": "Debes seleccionar al menos una imagen antes de enviar.",
                "resultados": [],
            }

        if not self.rutaModelo.exists():
            return {
                "ok": False,
                "titulo": "Modelo YOLOv8 pendiente",
                "mensaje": f"El sistema ya esta preparado para YOLOv8. Coloca el modelo entrenado en {self.rutaModelo} para activar la deteccion de caries.",
                "resultados": [],
            }

        try:
            modelo = self._cargarModelo()
        except Exception as error:
            return {
                "ok": False,
                "titulo": "No se pudo cargar YOLOv8",
                "mensaje": f"Revisa la instalacion de Ultralytics o la ruta del modelo. Detalle: {error}",
                "resultados": [],
            }

        self.carpetaResultados.mkdir(parents=True, exist_ok=True)
        resultados = []

        for archivo in archivosValidos:
            extension = Path(archivo.filename).suffix.lower()
            if extension not in self.formatosPermitidos:
                resultados.append(
                    {
                        "archivo": archivo.filename,
                        "estado": "Formato no admitido",
                        "detecciones": 0,
                        "imagen": "",
                    }
                )
                continue

            nombreSeguro = secure_filename(archivo.filename)
            rutaTemporal = self.carpetaResultados / f"entrada_{uuid4().hex}_{nombreSeguro}"
            archivo.save(rutaTemporal)

            predicciones = modelo.predict(source=str(rutaTemporal), conf=self.confianza, verbose=False)
            prediccion = predicciones[0]
            imagenAnotada = prediccion.plot()
            nombreResultado = f"resultado_{uuid4().hex}{extension}"
            rutaResultado = self.carpetaResultados / nombreResultado

            try:
                import cv2

                cv2.imwrite(str(rutaResultado), imagenAnotada)
            except Exception:
                from PIL import Image

                Image.fromarray(imagenAnotada).save(rutaResultado)

            detecciones = len(prediccion.boxes) if prediccion.boxes is not None else 0
            resultados.append(
                {
                    "archivo": archivo.filename,
                    "estado": "Analizado",
                    "detecciones": detecciones,
                    "imagen": f"resultados/{nombreResultado}",
                }
            )

            try:
                rutaTemporal.unlink()
            except OSError:
                pass

        return {
            "ok": True,
            "titulo": "Analisis YOLOv8 completado",
            "mensaje": "El sistema proceso las imagenes y genero resultados visuales de apoyo.",
            "resultados": resultados,
        }

    def _cargarModelo(self):
        if self._modelo is None:
            from ultralytics import YOLO

            self._modelo = YOLO(str(self.rutaModelo))

        return self._modelo
