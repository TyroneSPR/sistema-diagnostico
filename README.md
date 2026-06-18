# Sistema de Diagnostico Dental Asistido

Aplicacion web desarrollada con Flask para presentar un sistema clinico de apoyo odontologico orientado a la deteccion de caries dental. La plataforma mantiene una estetica hospitalaria seria, usa navegacion protegida por sesion y organiza sus apartados principales en paginas independientes.

## Estado actual

El sistema esta listo para desplegarse en Render y mostrar los cambios actuales. YOLOv8 queda anunciado como el evento estrella de la plataforma y se presenta como una integracion proxima, no como inferencia activa en produccion.

Funcionalidades actuales:

- Login con validacion basica de correo electronico.
- Sesiones protegidas para las paginas internas.
- Redireccion al login cuando una pagina protegida se visita sin sesion.
- Retorno automatico a la pagina solicitada despues de iniciar sesion.
- Pagina principal con enfoque clinico y nuevo estilo azul hospitalario.
- Paginas propias para cada apartado profesional.
- Centro de analisis con carga de estudios dentales.
- Previsualizacion local de imagenes antes de enviarlas.
- Checklist de calidad del estudio.
- Estimador de urgencia clinica.
- Simulador educativo de criterios visuales.
- Pagina de dataset conectada a Kaggle Hub.
- Pagina especial de YOLOv8 proximamente como lanzamiento principal.

## YOLOv8 proximamente

YOLOv8 es el evento estrella del sistema. La pagina `/yolov8-proximamente` anuncia la futura integracion de inteligencia artificial para deteccion asistida de caries.

En esta version:

- No se ejecuta inferencia automatica desde la interfaz.
- El centro de analisis prepara el estudio y deja claro que YOLOv8 llegara en una siguiente etapa.
- Se conserva el modulo tecnico `servicio/yolo.py` y el script de entrenamiento para desarrollo futuro.
- La experiencia visible evita prometer diagnostico automatico antes de tener el modelo validado.

## Rutas principales

Rutas publicas:

- `/` - Login.

Rutas protegidas por sesion:

- `/inicio` - Pagina principal.
- `/servicio` - Centro de analisis odontologico.
- `/deteccion-caries` - Apartado de deteccion de caries.
- `/radiografias` - Apartado de analisis radiografico.
- `/revision-clinica` - Apartado de revision de imagenes clinicas.
- `/yolov8-proximamente` - Evento estrella YOLOv8.
- `/dataset` - Dataset de caries.
- `/acerca-de` - Descripcion institucional del proyecto.
- `/salir` - Cierre de sesion.

## Estructura del proyecto

```text
Sistema de diagnostico/
|-- app.py
|-- requirements.txt
|-- README.md
|-- render.yaml
|-- descargar_dataset.py
|-- entrenar_yolov8.py
|-- models/
|-- servicio/
|   |-- __init__.py
|   |-- analisis.py
|   |-- dataset.py
|   |-- yolo.py
|-- templates/
|   |-- base.html
|   |-- login.html
|   |-- index.html
|   |-- apartado.html
|   |-- acerca.html
|   |-- servicio.html
|   |-- dataset.html
|-- static/
|   |-- css/
|   |   |-- estilos.css
|   |-- js/
|   |   |-- interacciones.js
|   |-- img/
|   |   |-- deteccion.svg
|   |   |-- radiografia.svg
|   |   |-- analisis.svg
|   |-- resultados/
```

## Archivos clave

### `app.py`

Configura la aplicacion Flask, sesiones, cookies, rutas protegidas y redirecciones. Tambien lee variables de entorno para ejecutar localmente o en Render.

Variables usadas:

- `SECRET_KEY`: clave de sesion.
- `SESSION_COOKIE_SECURE`: permite activar cookies seguras en HTTPS.
- `PORT`: puerto local cuando se ejecuta con `python app.py`.
- `FLASK_DEBUG`: activa o desactiva debug local.

### `servicio/analisis.py`

Concentra la logica de presentacion clinica:

- Validacion de correo.
- Datos de las paginas institucionales.
- Datos de los apartados.
- Estado de YOLOv8 como proximamente.
- Preparacion de estudios cargados sin ejecutar inferencia.

### `static/js/interacciones.js`

Agrega funciones reales en el navegador:

- Vista previa de archivos cargados.
- Checklist de calidad.
- Estimador de prioridad.
- Simulador educativo de criterios visuales.

### `templates/apartado.html`

Plantilla reusable para las paginas profesionales:

- Deteccion de caries.
- Analisis radiografico.
- Revision clinica.
- YOLOv8 proximamente.

## Instalacion local

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecutar la aplicacion:

```bash
python app.py
```

3. Abrir:

```text
http://127.0.0.1:5000
```

Tambien se puede ejecutar con Flask:

```bash
python -m flask --app app run
```

## Despliegue en Render

El archivo `render.yaml` ya esta preparado:

```yaml
services:
  - type: web
    name: sistema-diagnostico
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: SECRET_KEY
        generateValue: true
```

Para reflejar los cambios en Render, solo se necesita redeplegar el servicio conectado al repositorio de GitHub.

## Dependencias

```text
Flask==3.1.0
gunicorn==23.0.0
kagglehub==0.3.12
ultralytics>=8.3,<9.0
```

## Dataset

El sistema mantiene una pagina para el dataset publico:

```text
mariamosamakhalifa/adult-caries-detection-dataset
```

Tambien se puede descargar por consola:

```bash
python descargar_dataset.py
```

## Desarrollo futuro

Siguientes pasos recomendados:

- Revisar y preparar el dataset real.
- Crear `datasets/caries/data.yaml`.
- Entrenar YOLOv8.
- Validar resultados con criterio clinico.
- Integrar inferencia en la interfaz cuando el modelo este listo.
- Convertir el login actual en autenticacion real si el sistema se usara con usuarios finales.

## Verificaciones realizadas

Antes de subir los cambios se verifico:

```bash
python -m compileall app.py servicio
```

Tambien se probaron las rutas protegidas con el cliente de pruebas de Flask.
