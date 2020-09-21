# StarWars_Django

## Descripción
Este proyetco esta desarrollado en Django [**Django**](https://www.djangoproject.com/download/) y Python 3.8  [**Python**](https://www.python.org/downloads/)

## Instalacion de este repositorio
Clonar este repositorio que se encuenta eb github

git clone https://github.com/georgus/StarWars_Django.git


## Activar virtualenv en entornos Gnu/Linux

```sh
$ virtualenv env
$ source env/bin/activate
```

## Activar virtualenv en entornos Windows

```sh
python3 -m virtualenv venv
vanv\Scripts\activate
```

Una vez dentro del entorno, Instalar las dependencias:

```sh
$ pip install -r requeriments.txt
```

## Hacer la migraciones de los modelos 
```sh
python manage.py makemigrations api
python manage.py migrate api  
```
Si no llega a reconocer los modelos apuntar a la APP (api)

```sh
python manage.py makemigrations api
python manage.py migrate api 
```

### Opcional, ejecutar pruebas en eel shell
```sh
python3 manager.py shell
```

### Iniciar el servidor web

```sh
python3 manager.py runserver
```

## **Bases de Datos Soportadas**
Este sistema por defecto, utiliza los siguientes motores de Bases de Datos:
- **SQLite**
