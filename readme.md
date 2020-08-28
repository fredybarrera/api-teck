# Api Rest Teck

Proyecto desarrollado en Python 3.8, Django 2.1.15 y Django Rest Framework 3.11.1

## Propósito

Api Rest para la consulta de registros GPS de equipos y transformación de coordenadas desde base de datos SQL Server 2012.

## Instalación

Descargar el proyecto y descomprimir en una ubicación dentro del disco C:

Se recomienda la instalación dentro de un entorno virtual de [miniconda](https://docs.conda.io/en/latest/miniconda.html).

Instalar miniconda en el sistema operativo y crear un entorno virtual con Python 3.8:
```bash
conda create -n nombre_entorno python==3.8
```
Activar al entorno virtual:
```bash
activate nombre_entorno 
```
Navegar hasta la ubicación del proyecto e instalar las dependencias:

```bash
pip install -r requirements.txt
```

Crear un archivo **.env** en la raiz del proyecto, tomando como referencia el archivo **.env_example** y completar los valores correspondientes para las variables:
```bash
CORS_WHITE_LIST_LOCALHOST = ""
APP_DATABASE_NAME = ""
APP_DATABASE_USER = ""
APP_DATABASE_PASSWORD = ""
APP_DATABASE_HOST = ""
APP_DATABASE_DRIVER = ""
```

## Uso

Levantar el proyecto con el comando:
```bash
python manage.py runserver
```

Para usar un puerto distinto:
```bash
python manage.py runserver 7000
```

### Acceso

Acceder a la siguiente url:
```
http://127.0.0.1:8000/api/equip/