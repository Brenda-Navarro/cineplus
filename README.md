# 🎬 CinePlus — Tu Catálogo de Películas Personal

**CinePlus** es una aplicación de escritorio desarrollada en **Python** con interfaz gráfica en **Tkinter**, diseñada para gestionar un catálogo de películas con una experiencia visual atractiva y fácil de usar.

## 🚀 Características principales
- **🎥 Catálogo interactivo**: agrega, visualiza, filtra y elimina películas.
- **🖼 Previsualización de imágenes** con dimensiones recomendadas para mantener la calidad.
- **🎭 Filtros por género** (Acción, Comedia, Drama, Terror, Ciencia Ficción, Romance, Animación y Otros).
- **💾 Almacenamiento persistente** en un archivo `.txt` para conservar el catálogo.
- **🔊 Sonidos personalizados** en formato `.wav` para la bienvenida y los clics.
- **🌆 Fondo y diseño oscuro** con paneles de alto contraste para mejor legibilidad.
- **⚡ Interfaz fluida** con desplazamiento por rueda del ratón y botones accesibles.
- **💡 Consejos de uso** integrados para guiar al usuario.

## 🛠 Tecnologías utilizadas
- **Python 3.10+**
- **Tkinter** (interfaz gráfica)
- **Pillow (PIL)** para manejo y redimensionamiento de imágenes
- **Winsound** para reproducción de sonidos WAV (Windows)
- **OS / pathlib** para gestión de rutas de archivos
- **ttk** para comboboxes y scrollbars estilizados

## 📂 Estructura del proyecto
cineplus/
│
├── main_gui.py # Interfaz principal
├── pelicula_class.py # Clase Pelicula (modelo)
├── catalogo_class.py # Clase CatalogoPeliculas (gestión del catálogo)
├── catalogo.txt # Base de datos en texto plano
├── imagenes/ # Recursos multimedia
│ ├── background.jpg # Fondo opcional
│ ├── placeholder.png # Imagen por defecto
│ ├── welcome.wav # Sonido de bienvenida
│ └── click.wav # Sonido de clic
└── README.md


## 📥 Instalación y uso
1. **Clonar el repositorio**  
   ```bash
   git clone https://github.com/tuusuario/cineplus.git
   cd cineplus

Instalar dependencias
pip install pillow
Ejecutar la aplicación
python main_gui.py

Puedes usar main_gui.exe para ejecutarlo sin python.

💡 Notas importantes
Si no se encuentran las imágenes o sonidos, la app funcionará igualmente, usando valores por defecto.

Los sonidos .wav funcionan únicamente en Windows (con winsound). En otros sistemas se omitirán sin error.

📜 Licencia
Este proyecto es de uso libre para fines educativos y personales.

✨ CinePlus — Organiza tu cine como un profesional.

---
💻 Desarrollado por **Brenda Navarro**  Especialista en Marketing Tecnológico








