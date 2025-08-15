# CinePlus 🎬

Aplicación de escritorio en Python (Tkinter) para gestionar un catálogo de películas con imágenes, géneros y descripciones.

## Características
- Bienvenida con sonido e imagen de fondo.
- Catálogo filtrable por géneros.
- Miniaturas de imágenes y descripciones.
- Eliminación individual o total de películas.
- Mensaje de salida amistoso.

## Requisitos
```bash
pip install pillow
```
(Solo en Windows) para sonidos WAV:
```bash
import winsound
```

## Estructura
cineplus/
│-- main_gui.py
│-- pelicula_class.py
│-- catalogo_class.py
│-- catalogo.txt
│-- imagenes/
    │-- background.jpg
    │-- placeholder.png
    │-- welcome.wav
    │-- click.wav
