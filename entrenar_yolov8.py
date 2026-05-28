from pathlib import Path

from ultralytics import YOLO


def main():
    archivoDatos = Path("datasets/caries/data.yaml")

    if not archivoDatos.exists():
        raise FileNotFoundError(
            "No se encontro datasets/caries/data.yaml. Descarga el dataset, revisa su estructura y crea el data.yaml antes de entrenar."
        )

    modelo = YOLO("yolov8n.pt")
    modelo.train(
        data=str(archivoDatos),
        epochs=50,
        imgsz=640,
        batch=8,
        project="runs/caries",
        name="yolov8n_caries",
    )


if __name__ == "__main__":
    main()
