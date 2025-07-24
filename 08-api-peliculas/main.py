from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI()

# Modelo de datos
class Pelicula(BaseModel):
    titulo: str
    año: int
    descripcion: str
    director: str

class PeliculaConID(Pelicula):
    id: str

# Base de datos simulada (en memoria)
peliculas_db: List[PeliculaConID] = [
    PeliculaConID(id=str(uuid4()), titulo="El Padrino", año=1972, descripcion="Mafia y familia.", director="Francis Ford Coppola"),
    PeliculaConID(id=str(uuid4()), titulo="Pulp Fiction", año=1994, descripcion="Historias entrelazadas del crimen.", director="Quentin Tarantino"),
    PeliculaConID(id=str(uuid4()), titulo="Cadena perpetua", año=1994, descripcion="Esperanza en prisión.", director="Frank Darabont"),
    PeliculaConID(id=str(uuid4()), titulo="El caballero oscuro", año=2008, descripcion="Batman enfrenta al Joker.", director="Christopher Nolan"),
    PeliculaConID(id=str(uuid4()), titulo="Forrest Gump", año=1994, descripcion="Un hombre con gran corazón.", director="Robert Zemeckis"),
    PeliculaConID(id=str(uuid4()), titulo="Origen", año=2010, descripcion="Sueños dentro de sueños.", director="Christopher Nolan"),
    PeliculaConID(id=str(uuid4()), titulo="Gladiator", año=2000, descripcion="Venganza en la arena.", director="Ridley Scott"),
    PeliculaConID(id=str(uuid4()), titulo="La lista de Schindler", año=1993, descripcion="Salvando vidas en el Holocausto.", director="Steven Spielberg"),
    PeliculaConID(id=str(uuid4()), titulo="Interstellar", año=2014, descripcion="Viaje interestelar para salvar la humanidad.", director="Christopher Nolan"),
    PeliculaConID(id=str(uuid4()), titulo="La vida es bella", año=1997, descripcion="Optimismo en tiempos oscuros.", director="Roberto Benigni"),
]

# Endpoints
@app.get("/peliculas", response_model=List[PeliculaConID])
async def listar_peliculas():
    return peliculas_db

@app.get("/peliculas/{pelicula_id}", response_model=PeliculaConID)
async def obtener_pelicula(pelicula_id: str):
    for pelicula in peliculas_db:
        if pelicula.id == pelicula_id:
            return pelicula
    raise HTTPException(status_code=404, detail="Película no encontrada")

@app.post("/peliculas", response_model=PeliculaConID, status_code=201)
async def crear_pelicula(pelicula: Pelicula):
    nueva_pelicula = PeliculaConID(id=str(uuid4()), **pelicula.dict())
    peliculas_db.append(nueva_pelicula)
    return nueva_pelicula

@app.put("/peliculas/{pelicula_id}", response_model=PeliculaConID)
async def actualizar_pelicula(pelicula_id: str, datos: Pelicula):
    for idx, pelicula in enumerate(peliculas_db):
        if pelicula.id == pelicula_id:
            actualizada = PeliculaConID(id=pelicula_id, **datos.dict())
            peliculas_db[idx] = actualizada
            return actualizada
    raise HTTPException(status_code=404, detail="Película no encontrada")

@app.delete("/peliculas/{pelicula_id}", status_code=204)
async def eliminar_pelicula(pelicula_id: str):
    for idx, pelicula in enumerate(peliculas_db):
        if pelicula.id == pelicula_id:
            peliculas_db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Película no encontrada")
