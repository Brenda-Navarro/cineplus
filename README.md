# CinePlus 🎬

CinePlus es una aplicación de escritorio hecha con **Python** y **Tkinter** que permite gestionar un catálogo personal de películas.  
Incluye soporte para imágenes, previsualización, sonidos y categorías de género.

## ✨ Características
- **Interfaz gráfica** moderna en tema oscuro con fondo personalizable.
- **Agregar películas** con título, género, descripción e imagen.
- **Vista de catálogo** con miniaturas, descripción y filtro por género.
- **Previsualización de imágenes** y dimensiones recomendadas.
- **Reproducción de sonidos** (`welcome.wav` y `click.wav`).
- **Gestión completa del catálogo** (eliminar una o todas las películas).
- **Mensajes de bienvenida y despedida**.

## 📂 Estructura del proyecto
```
cineplus/
│
├── main_gui.py           # Interfaz principal de CinePlus
├── pelicula_class.py     # Clase Pelicula
├── catalogo_class.py     # Clase CatalogoPeliculas
├── catalogo.txt          # Archivo donde se guarda el catálogo
└── imagenes/             # Carpeta con recursos
    ├── background.jpg    # Imagen de fondo (opcional)
    ├── placeholder.png   # Imagen por defecto
    ├── welcome.wav       # Sonido de bienvenida
    └── click.wav         # Sonido de clic
```

## 🚀 Requisitos
- Python **3.9+**
- Librerías:
  ```bash
  pip install pillow
  ```

## ▶ Uso
1. Clonar el repositorio o descargarlo como ZIP.
2. Colocar las imágenes y sonidos en la carpeta `imagenes`.
3. Ejecutar:
   ```bash
   python main_gui.py
   ```

## 📌 Notas
- Si los sonidos no se reproducen, verifica que estés en **Windows** (usa `winsound`).
- El catálogo se guarda automáticamente en `catalogo.txt`.

---
💻 Desarrollado por **Brenda Navarro**  
