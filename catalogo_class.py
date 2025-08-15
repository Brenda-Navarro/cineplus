import os
from pelicula_class import Pelicula

class CatalogoPeliculas:
    def __init__(self, nombre, archivo):
        self.nombre = nombre
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8") as f:
                pass

    def agregar_pelicula(self, pelicula):
        with open(self.archivo, "a", encoding="utf-8") as f:
            f.write(f"{pelicula.nombre}|{pelicula.genero}|{pelicula.descripcion}|{pelicula.imagen}\n")

    def listar_peliculas(self):
        peliculas = []
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    datos = linea.strip().split("|")
                    if len(datos) == 4:
                        peliculas.append(Pelicula(*datos))
        return peliculas

    def eliminar_catalogo(self):
        if os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8") as f:
                pass
