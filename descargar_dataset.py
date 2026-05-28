from servicio.dataset import DatasetCaries


def main():
    dataset = DatasetCaries()
    resultado = dataset.descargar()

    print(resultado["mensaje"])
    if resultado["ruta"]:
        print("Path to dataset files:", resultado["ruta"])


if __name__ == "__main__":
    main()
