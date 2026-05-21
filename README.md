# Sistema de Diagnostico Asistido por Computadora para la Deteccion de Caries Dental

## Descripcion general

Este proyecto corresponde a la base inicial de un sistema web orientado al apoyo odontologico para la deteccion de caries dental en imagenes clinicas y radiografias dentales. El desarrollo esta organizado con Python para la capa del servicio y con HTML y CSS para la interfaz visual.

El sistema se encuentra en una etapa de construccion funcional. Ya existe una experiencia completa de acceso, navegacion institucional, presentacion del proyecto y una vista de servicio preparada para la futura integracion del procesamiento con YOLOv8. Aunque el analisis automatico todavia no ha sido implementado, ya se ha dejado lista la estructura que se utilizara cuando llegue esa fase.

## Objetivo del proyecto

La finalidad del sistema es apoyar al profesional odontologico en la deteccion temprana de caries dental mediante herramientas de analisis asistido por computadora. La proyeccion del proyecto es permitir la carga de estudios dentales, procesarlos con un modelo de vision artificial y presentar resultados de apoyo para la interpretacion clinica.

En el estado actual, el sistema ya cumple con una funcion real de presentacion institucional y organizacion del servicio. La aplicacion permite ingresar mediante correo electronico, navegar por una vista principal, revisar el proposito del proyecto y acceder a una pantalla de servicio donde ya se pueden seleccionar y enviar imagenes, aunque el procesamiento aun no se encuentre disponible.

## Estado actual del sistema

Hasta este momento, el proyecto cuenta con los siguientes componentes ya operativos:

- Aplicacion web construida con Flask.
- Ruta inicial de login en la direccion principal del sistema.
- Validacion basica de correo electronico antes de entrar a la interfaz principal.
- Manejo de sesion para controlar el acceso a las vistas internas.
- Pagina principal con contenido institucional y enfoque clinico.
- Tarjetas informativas sobre caries dental con imagenes referenciales locales.
- Navegacion superior con opcion de `Servicios` y panel desplegable.
- Pagina `Acerca del proyecto` con descripcion formal del sistema.
- Pagina `Servicio` preparada para la carga de imagenes dentales.
- Formulario para subir una o varias imagenes de radiografias o estudios dentales.
- Ventana modal que informa que el proceso de analisis aun no ha sido desarrollado.
- Estilo visual moderno, elegante, sobrio y alineado con una referencia institucional tipo hospital.

## Tecnologias utilizadas

En la fase actual se estan utilizando las siguientes tecnologias:

- Python para la capa del servicio.
- Flask para la aplicacion web.
- HTML para la estructura de las vistas.
- CSS para el diseño visual.

En una siguiente etapa se integrara YOLOv8 como motor de deteccion para el procesamiento de imagenes y radiografias dentales.

## Estructura actual del proyecto

La estructura de trabajo del proyecto se encuentra organizada de la siguiente manera:

```text
Sistema de diagnostico/
|-- app.py
|-- requirements.txt
|-- README.md
|-- servicio/
|   |-- __init__.py
|   |-- analisis.py
|-- templates/
|   |-- base.html
|   |-- login.html
|   |-- index.html
|   |-- acerca.html
|   |-- servicio.html
|-- static/
|   |-- css/
|   |   |-- estilos.css
|   |-- img/
|       |-- deteccion.svg
|       |-- radiografia.svg
|       |-- analisis.svg
```

## Explicacion de cada archivo principal

### app.py

Este archivo es el punto de entrada principal del sistema. Aqui se crea la aplicacion Flask, se configura la carpeta de plantillas, se define la carpeta de recursos estaticos y se inicializa la capa del servicio.

Las rutas actualmente implementadas son:

- `/` para el login inicial.
- `/inicio` para la vista principal del sistema.
- `/acerca-de` para la descripcion del proyecto.
- `/servicio` para la vista de carga de imagenes y estado del modulo.
- `/salir` para cerrar la sesion actual.

Ademas, en esta fase el archivo ya controla el flujo de acceso y la respuesta del formulario de carga de imagenes.

### servicio/analisis.py

Este archivo contiene la clase `AnalisisDental`, que concentra la logica basica de la capa de servicio mientras el sistema aun no procesa imagenes realmente.

Actualmente esta clase se encarga de:

- Validar el correo electronico ingresado por el usuario.
- Devolver el resumen informativo del proyecto.
- Devolver el estado actual del servicio de analisis.
- Preparar la respuesta del formulario de carga de imagenes.

Todavia no realiza inferencia ni procesamiento con modelos de inteligencia artificial, pero ya actua como punto de integracion para la siguiente etapa del desarrollo.

### templates/base.html

Esta plantilla sirve como base para las demas vistas del sistema. Contiene la estructura general del documento HTML y enlaza el archivo principal de estilos CSS.

### templates/login.html

Esta vista es la primera pantalla que aparece al abrir el sistema. Su funcion actual es:

- Presentar una introduccion visual al proyecto.
- Solicitar el correo electronico del usuario.
- Validar el acceso de manera basica.
- Redirigir a la vista principal cuando el correo tiene un formato valido.

### templates/index.html

Esta es la vista principal a la que se accede despues del login. En esta pantalla se presenta:

- El nombre del sistema.
- El correo de la sesion actual.
- Informacion resumida sobre el estado del proyecto.
- Tarjetas informativas sobre deteccion oportuna, apoyo radiografico y analisis asistido.
- Imagenes referenciales dentro de esas tarjetas.
- Un acceso visible hacia la seccion del servicio.

### templates/acerca.html

Esta vista presenta la parte institucional y descriptiva del proyecto. En ella se explica:

- El objetivo general del sistema.
- El alcance actual del desarrollo.
- El estado del modelo.
- El proposito general de la plataforma.

### templates/servicio.html

Esta vista ya representa una base funcional del modulo que mas adelante procesara las imagenes dentales. En este momento incluye:

- Informacion sobre el estado actual del servicio.
- Formulario para subir una o varias imagenes.
- Restriccion visual de formatos admitidos para imagenes.
- Boton de envio.
- Mensaje modal que informa que el analisis aun no esta implementado.

### static/css/estilos.css

Este archivo contiene todo el diseño visual del proyecto. Actualmente resuelve:

- Estilo institucional de la aplicacion.
- Distribucion del login, inicio, pagina informativa y pagina de servicio.
- Navegacion superior con panel desplegable.
- Tarjetas con imagenes y bloques de contenido.
- Formulario de carga de imagenes.
- Modal de aviso para el servicio aun no implementado.
- Ajustes para evitar que el panel desplegable provoque desbordamiento horizontal.

### static/img/

Esta carpeta contiene las ilustraciones SVG utilizadas en la vista principal dentro de las tarjetas informativas sobre caries dental.

## Flujo actual del sistema

El flujo actual de uso es el siguiente:

1. El usuario entra al sistema y visualiza la pantalla de login.
2. Ingresa un correo electronico.
3. Si el correo tiene formato valido, el sistema crea la sesion y redirige a la vista principal.
4. Desde la vista principal puede navegar por `Inicio`, `Acerca de` y `Servicios`.
5. Al pasar el cursor sobre `Servicios`, se despliega un panel con accesos relacionados al modulo futuro.
6. Al entrar a `Servicio`, el usuario puede seleccionar una o varias imagenes.
7. Al enviar esas imagenes, aparece una ventana modal informando que el procesamiento aun no ha sido desarrollado.

## Funcionalidad implementada en la carga de imagenes

La vista del servicio ya permite una simulacion funcional del paso de carga de estudios dentales. Esto significa que:

- El usuario puede abrir el selector de archivos.
- Puede escoger una o varias imagenes.
- El formulario acepta formatos graficos comunes.
- El envio responde con una ventana informativa.

Por el momento, las imagenes no se procesan ni se almacenan como parte de un analisis real. El mensaje mostrado existe para dejar claro que esa parte sigue pendiente de implementacion.

## Criterios de desarrollo aplicados

Durante el desarrollo actual se han seguido los siguientes criterios:

- Separacion entre capa de servicio y capa visual.
- Uso de nombres en español dentro del codigo.
- Preferencia por estilo camelCase para nombres de variables y funciones donde corresponde.
- Estructura ordenada para facilitar la integracion futura con YOLOv8.
- Diseño serio, limpio y profesional.
- Navegacion clara y preparada para crecer con mas modulos.

## Lo que aun falta desarrollar

La siguiente etapa del proyecto debe concentrarse en las funciones que todavia no existen en el sistema:

- Integracion del modelo YOLOv8.
- Procesamiento real de imagenes clinicas y radiografias dentales.
- Generacion de resultados y detecciones visuales.
- Posible almacenamiento de estudios y resultados.
- Mejoras adicionales en autenticacion si se desea convertir el acceso en un modulo real.

## Ejecucion del proyecto

Para ejecutar el sistema en su estado actual se puede seguir este procedimiento:

1. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecutar la aplicacion:

```bash
python app.py
```

3. Abrir en el navegador la direccion local que Flask muestre en consola.

## Dependencias actuales

La dependencia utilizada hasta este momento es la siguiente:

```text
Flask==3.1.0
```

## Verificaciones realizadas

Se ha realizado una verificacion de sintaxis del codigo Python para confirmar que la estructura actual del proyecto no presenta errores basicos de compilacion en la capa de servicio y en el punto de entrada de la aplicacion.

## Resumen de la etapa actual

En el estado presente, el sistema ya dispone de una experiencia web funcional y coherente. El usuario puede ingresar, navegar por las vistas principales, abrir el panel de servicios, revisar informacion clinica relacionada con la caries dental y utilizar una pantalla de carga de imagenes que sirve como base visible del modulo que luego sera conectado con YOLOv8.

Aunque el procesamiento automatico aun no existe, ya se cuenta con una estructura seria, ordenada y lista para evolucionar sin rehacer el proyecto desde cero.
