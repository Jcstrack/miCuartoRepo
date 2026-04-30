# Importa el módulo os (sirve para interactuar con el sistema operativo)
# En este código no se está usando, podría eliminarse
import os

# Importa Union desde typing (permite definir múltiples tipos posibles)
# Tampoco se está usando actualmente
from typing import Union

# Importa la clase principal FastAPI desde la librería fastapi
# Esta clase se usa para crear la aplicación backend
from fastapi import FastAPI

# Importa BaseModel desde pydantic
# Sirve para crear modelos de datos (validación de inputs), aunque aquí no se usa aún
from pydantic import BaseModel


# Crea una instancia de la aplicación FastAPI
# 'app' será el objeto principal que maneja rutas, peticiones y respuestas
app = FastAPI()


# Define una ruta GET en la URL "/familia"
# Cuando alguien accede a http://localhost:8000/familia
# se ejecuta la función get_familia()
@app.get("/familia")
def get_familia():
    
    # Crea una lista de strings con nombres
    rows = ["Amin", "Marce", "Miranda"]
    
    # Retorna la lista como respuesta
    # FastAPI automáticamente la convierte a JSON
    return rows


# Define otra ruta GET en "/superheroesDC"
# Se accede desde http://localhost:8000/superheroesDC
@app.get("/superheroesDC")
def get_superheroes():
    
    # Lista de nombres de superhéroes de DC
    rows = ["Superman", "Batman", "Flash", "Wonder", "Aquaman", "Cyborg"]
    
    # Retorna la lista en formato JSON
    return rows

@app.get("/superheroesMarvel")
def get_superheroes():
    
    # Lista de nombres de superhéroes de Marvel
    rows = ["Spider-Man", "Iron Man", "Captain America", "Thor", "Hulk", "Black Widow"]
    
    # Retorna la lista en formato JSON
    return rows

@app.get("/cursosPlatzi")
def get_cursos():
    
    # Lista de nombres de cursos de Platzi
    rows = ["Docker", "Bash", "Python", "JavaScript", "Data Science", "Machine Learning"]
    
    # Retorna la lista en formato JSON
    return rows