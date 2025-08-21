# Proyecto de Pruebas de Creación de Kits - Urban Grocers

## Descripción

Este proyecto automatiza las pruebas de la funcionalidad de **creación de kits de productos** en la aplicación **Urban Grocers**. Se utilizan pruebas con **Pytest** para validar distintos escenarios, asegurando que la API funcione correctamente y cumpla con los requisitos definidos.

### Características:

- Validación de datos enviados a la API
- Manejo de respuestas esperadas y errores
- Pruebas parametrizadas para diferentes configuraciones de kits

## Requisitos

Antes de ejecutar las pruebas, asegúrate de tener instaladas las siguientes herramientas:

- **Python 3.x**
- **Pytest** (`pip install pytest`)
- **Requests** (`pip install requests`)

## Instalación y Ejecución

Sigue estos pasos para configurar y ejecutar las pruebas:

1. **Clonar el repositorio**

   git clone https://github.com/DavidHunter94/qa-project-Urban-Grocers-app-es

2. **Instalar dependencias**

   pip install -r requirements.txt

3. **Ejecutar pruebas**

   pytest
   
## Estructura del Proyecto

📂 **config/**            → Archivos de configuración, como `configuration.py`  
📂 **data/**              → Archivos relacionados con los datos de prueba, como `data.py`  
📂 **requests/**          → Archivos relacionados con las solicitudes a la API, como `sender_stand_request.py`  
📄 **create_kit_name_kit_test.py**  → Pruebas automatizadas para la creación de kits de productos  
📄 **.gitignore**         → Archivos para excluir del control de versiones  
📄 **README.md**          → Documentación del proyecto


## Autor y Sprint

*Autor:* Víctor David Martínez Matías
*Sprint:* 7 - Introducción a la automatización de pruebas
