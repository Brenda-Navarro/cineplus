# main_gui.py — CinePlus (Tkinter + PIL + sonidos WAV con winsound)
# Diseño oscuro con fondo, iconos y ayudas sutiles.
# Requisitos: pillow (PIL)
# Coloca estos archivos en la carpeta del proyecto:
#   - catalogo_class.py  (con la clase CatalogoPelicula)
#   - pelicula_class.py  (con la clase Pelicula)
#   - carpeta "imagenes" con:
#         background.jpg   (opcional)
#         placeholder.png  (recomendado)
#         welcome.wav      (opcional)
#         click.wav        (opcional)

import os
import tkinter as tk
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk

# Sonidos WAV (Windows). En otros SO simplemente no sonarán (sin error).
try:
    import winsound
except Exception:  # pragma: no cover
    winsound = None

from pelicula_class import Pelicula
from catalogo_class import CatalogoPeliculas

# ------------------ Rutas y constantes ------------------
RUTA_ARCHIVO      = "catalogo.txt"
IMG_FOLDER        = "imagenes"
RUTA_BG           = os.path.join(IMG_FOLDER, "background.jpg")     # Imagen de fondo
RUTA_PLACEHOLDER  = os.path.join(IMG_FOLDER, "placeholder.png")    # Imagen por defecto
SND_WELCOME       = os.path.join(IMG_FOLDER, "welcome.wav")
SND_CLICK         = os.path.join(IMG_FOLDER, "click.wav")

# Géneros (7) + Otros
GENEROS = ["Acción", "Comedia", "Drama", "Terror", "Ciencia Ficción", "Romance", "Animación"]
GENEROS_FILTRO = ["Todos"] + GENEROS + ["Otros"]
GENEROS_ADD    = GENEROS + ["Otros"]

# Recomendación (no bloquea)
REC_MAX_W, REC_MAX_H = 300, 300

# ------------------ App base ------------------
root = tk.Tk()
root.title("CinePlus 🎬")
root.geometry("900x600")
root.resizable(False, False)
root.configure(bg="#0f0f0f")

catalogo = CatalogoPeliculas("Catálogo de Películas", RUTA_ARCHIVO)

# Background global (si existe)
_BG_PHOTO = None
if os.path.exists(RUTA_BG):
    try:
        _BG_PHOTO = ImageTk.PhotoImage(Image.open(RUTA_BG).resize((900, 600)))
    except Exception:
        _BG_PHOTO = None

# ------------------ Utilidades ------------------
def play_sound(path):
    """Reproduce un WAV de forma asíncrona en Windows. Silencioso si falta o en otros SO."""
    if not (winsound and path and os.path.exists(path)):
        return
    try:
        winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
    except Exception:
        pass

def _scene():
    """Crea una 'escena' con fondo y panel central oscuro para contenido."""
    frame = tk.Frame(root, bg="#0f0f0f")
    frame.place(x=0, y=0, width=900, height=600)

    # Fondo
    if _BG_PHOTO:
        bg = tk.Label(frame, image=_BG_PHOTO)
        bg.image = _BG_PHOTO
        bg.place(x=0, y=0, relwidth=1, relheight=1)

    # Panel central para legibilidad
    panel = tk.Frame(frame, bg="#1c1c1c")
    panel.place(x=20, y=20, width=860, height=560)
    return frame, panel

def _btn(parent, text, command, bg="gold", fg="black", w=28, pady=8):
    return tk.Button(
        parent,
        text=text,
        font=("Arial", 14),
        bg=bg,
        fg=fg,
        width=w,
        activebackground="#f0ce54",
        activeforeground="black",
        pady=pady,
        command=lambda: (play_sound(SND_CLICK), command())
    )

def _title(parent, text):
    return tk.Label(parent, text=text, font=("Arial Black", 26), bg="#1c1c1c", fg="gold")

def _label(parent, text, size=12, fg="white"):
    return tk.Label(parent, text=text, font=("Arial", size), bg="#1c1c1c", fg=fg)

# ------------------ Escenas ------------------
def mostrar_bienvenida():
    frame, panel = _scene()
    play_sound(SND_WELCOME)

    _title(panel, "🎥 Bienvenido a CinePlus 🎥").pack(pady=28)
    _label(
        panel,
        "Tu cine personal para guardar, organizar y disfrutar películas.\n"
        "Agrega un título, elige el género, una imagen y listo.",
        13,
        "lightgray"
    ).pack(pady=6)

    _btn(panel, "▶ Continuar", lambda: [frame.destroy(), mostrar_menu()], w=24).pack(pady=20)

def mostrar_menu():
    frame, panel = _scene()

    _title(panel, "📽 Menú Principal").pack(pady=24)

    _btn(panel, "➕ Agregar Película",
         lambda: [frame.destroy(), agregar_pelicula()]).pack(pady=8)

    _btn(panel, "📂 Gestionar Catálogo",
         lambda: [frame.destroy(), gestionar_catalogo()]).pack(pady=8)

    # Mismo estilo (amarillo)
    _btn(panel, "🗑 Eliminar Catálogo",
         eliminar_catalogo).pack(pady=8)

    _btn(panel, "🚪 Salir",
         salir_programa).pack(pady=8)

    _label(panel, "Consejo: empieza agregando 2 o 3 títulos para ver la magia del catálogo.",
           10, "lightgray").pack(pady=10)

def agregar_pelicula():
    # Estado de imagen
    imagen_path = RUTA_PLACEHOLDER if os.path.exists(RUTA_PLACEHOLDER) else ""
    img_preview = None

    frame, panel = _scene()
    _title(panel, "🎞 Agregar Nueva Película").place(x=30, y=20)

    # Formulario (izquierda)
    _label(panel, "🏷️ Título *", 12).place(x=30, y=80)
    entry_nombre = tk.Entry(panel, font=("Arial", 12), width=38)
    entry_nombre.place(x=30, y=105)

    _label(panel, "🎭 Género *", 12).place(x=30, y=145)
    combo_genero = ttk.Combobox(panel, values=GENEROS_ADD, state="readonly", width=36)
    combo_genero.set(GENEROS_ADD[0])
    combo_genero.place(x=30, y=170)

    _label(panel, "📝 Descripción", 12).place(x=30, y=210)
    text_desc = tk.Text(panel, width=40, height=6, font=("Arial", 10))
    text_desc.place(x=30, y=235)

    _label(panel, f"Recomendado: hasta {REC_MAX_W}x{REC_MAX_H}px (se adapta si es distinto).",
           10, "gray").place(x=30, y=338)

    # Previsualización (derecha)
    _label(panel, "🖼 Previsualización", 12).place(x=580, y=80)
    lbl_preview = tk.Label(panel, bg="#1c1c1c")
    lbl_preview.place(x=560, y=105, width=220, height=300)

    def _cargar_preview(ruta):
        nonlocal img_preview
        img = None
        try:
            if ruta and os.path.exists(ruta):
                img = Image.open(ruta).copy()
            elif os.path.exists(RUTA_PLACEHOLDER):
                img = Image.open(RUTA_PLACEHOLDER).copy()
        except Exception:
            img = None

        if img:
            img.thumbnail((220, 300))
            img_preview = ImageTk.PhotoImage(img)
            lbl_preview.config(image=img_preview)
            lbl_preview.image = img_preview
        else:
            lbl_preview.config(image="")
            lbl_preview.image = None

    _cargar_preview(imagen_path)

    def seleccionar_imagen():
        nonlocal imagen_path
        ruta = filedialog.askopenfilename(
            title="Selecciona una imagen",
            filetypes=[("Imágenes", "*.png;*.jpg;*.jpeg;*.gif")]
        )
        if ruta:
            imagen_path = ruta
            _cargar_preview(imagen_path)

    # Botones (separados)
    _btn(panel, "📷 Seleccionar Imagen", seleccionar_imagen, w=24).place(x=30, y=370)

    def guardar_pelicula():
        nombre = entry_nombre.get().strip()
        genero = combo_genero.get().strip()
        descripcion = text_desc.get("1.0", tk.END).strip()

        if not nombre or not genero:
            messagebox.showwarning("Campos Obligatorios", "El título y el género son obligatorios.")
            return

        # Si no eligió imagen, usamos placeholder si existe
        ruta_final = imagen_path if imagen_path else (RUTA_PLACEHOLDER if os.path.exists(RUTA_PLACEHOLDER) else "")

        pelicula = Pelicula(nombre, genero, descripcion, ruta_final)
        catalogo.agregar_pelicula(pelicula)
        messagebox.showinfo("CinePlus", f"'{nombre}' se agregó al catálogo.")

        frame.destroy()
        mostrar_menu()

    _btn(panel, "💾 Guardar Película", guardar_pelicula, bg="#3cb371", fg="white", w=24).place(x=30, y=420)
    _btn(panel, "🏠 Volver al Menú", lambda: [frame.destroy(), mostrar_menu()], bg="gray", fg="white", w=24).place(x=30, y=470)

def gestionar_catalogo():
    frame, panel = _scene()
    _title(panel, "📚 Catálogo de Películas").place(x=30, y=20)

    # ----- Barra superior (filtro a la izquierda, botones a la derecha) -----
    toolbar = tk.Frame(panel, bg="#1c1c1c")
    toolbar.place(x=30, y=60, width=800, height=42)

    _label(toolbar, "Filtro:", 11, "white").pack(side="left", padx=(0, 6))
    combo_filtro = ttk.Combobox(toolbar, values=GENEROS_FILTRO, state="readonly", width=22)
    combo_filtro.set("Todos")
    combo_filtro.pack(side="left")

    # Botones a la derecha, más compactos
    btn_volver = _btn(toolbar, "🏠 Volver al Menú",
                      lambda: [frame.destroy(), mostrar_menu()],
                      bg="gray", fg="white", w=16, pady=4)
    btn_eliminar_todas = _btn(toolbar, "🧹 Eliminar Todas",
                              lambda: eliminar_todas(),
                              bg="#d9534f", fg="white", w=16, pady=4)
    btn_eliminar_todas.pack(side="right", padx=(6, 0))
    btn_volver.pack(side="right", padx=(0, 6))

    # ----- Contenedor con scroll para las tarjetas -----
    cont = tk.Frame(panel, bg="#1c1c1c")
    cont.place(x=30, y=110, width=800, height=420)

    canvas = tk.Canvas(cont, bg="#1c1c1c", highlightthickness=0)
    vsb = ttk.Scrollbar(cont, orient="vertical", command=canvas.yview)
    lista = tk.Frame(canvas, bg="#1c1c1c")

    lista.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    win = canvas.create_window((0, 0), window=lista, anchor="nw", width=780)
    canvas.configure(yscrollcommand=vsb.set)

    canvas.pack(side="left", fill="both", expand=True)
    vsb.pack(side="right", fill="y")

    # Ajuste de ancho del frame interno al redimensionar cont (aunque está fijo, mantiene coherencia)
    def _resize_inner(event):
        try:
            canvas.itemconfigure(win, width=event.width - 20)  # margen para el scroll
        except Exception:
            pass
    cont.bind("<Configure>", _resize_inner)

    # Scroll con rueda del ratón (Windows/Mac/Linux)
    def _on_mousewheel(event):
        # Windows / Mac
        if event.delta:
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        else:
            # Linux
            if event.num == 4:
                canvas.yview_scroll(-3, "units")
            elif event.num == 5:
                canvas.yview_scroll(3, "units")

    canvas.bind_all("<MouseWheel>", _on_mousewheel)   # Win/Mac
    canvas.bind_all("<Button-4>", _on_mousewheel)     # Linux
    canvas.bind_all("<Button-5>", _on_mousewheel)     # Linux

    tip = _label(panel, "Recomendación: usa el filtro para navegar por géneros. • Usa la rueda del mouse para desplazarte, cuando esté muy lleno el catálogo.",
                 10, "lightgray")
    tip.place(x=30, y=535)

    def cargar_lista():
        # limpiar
        for w in lista.winfo_children():
            w.destroy()

        peliculas = catalogo.listar_peliculas()
        f = combo_filtro.get()
        if f and f != "Todos":
            peliculas = [p for p in peliculas if (p.genero or "").lower() == f.lower()]

        if not peliculas:
            _label(lista, "No hay películas en esta vista. Agrega nuevas desde el menú principal.",
                   12, "lightgray").pack(pady=16)
            return

        for p in peliculas:
            card = tk.Frame(lista, bg="#2a2a2a")
            card.pack(pady=6, padx=6, fill="x")

            # Imagen/miniatura
            ruta_img = p.imagen if (p.imagen and os.path.exists(p.imagen)) else (RUTA_PLACEHOLDER if os.path.exists(RUTA_PLACEHOLDER) else "")
            thumb = None
            if ruta_img:
                try:
                    im = Image.open(ruta_img).copy()
                    im.thumbnail((92, 92))
                    thumb = ImageTk.PhotoImage(im)
                except Exception:
                    thumb = None

            if thumb:
                lbl_img = tk.Label(card, image=thumb, bg="#2a2a2a")
                lbl_img.image = thumb
                lbl_img.pack(side="left", padx=10, pady=8)
            else:
                _label(card, "Sin imagen", 10, "gray").pack(side="left", padx=10)

            # Texto
            txt = tk.Frame(card, bg="#2a2a2a")
            txt.pack(side="left", fill="x", expand=True, padx=5, pady=8)

            tk.Label(txt, text=f"🎬 {p.nombre}", font=("Arial", 13, "bold"),
                     bg="#2a2a2a", fg="white", anchor="w").pack(fill="x")
            tk.Label(txt, text=f"🎭 {p.genero}", font=("Arial", 11),
                     bg="#2a2a2a", fg="gold", anchor="w").pack(fill="x")

            desc = (p.descripcion or "").strip()
            if len(desc) > 150:
                desc = desc[:150] + "…"
            tk.Label(txt, text=desc, font=("Arial", 10),
                     bg="#2a2a2a", fg="lightgray", anchor="w", justify="left", wraplength=520).pack(fill="x", pady=2)

            # Acciones (botón más compacto)
            acciones = tk.Frame(card, bg="#2a2a2a")
            acciones.pack(side="right", padx=8)

            _btn(acciones, "🗑 Selección", lambda pel=p: confirmar_eliminar(pel),
                 bg="#d9534f", fg="white", w=12, pady=4).pack(pady=8)

    def confirmar_eliminar(pelicula):
        top = tk.Toplevel(root)
        top.title("Confirmar eliminación")
        top.geometry("360x300")
        top.resizable(False, False)
        top.configure(bg="#1c1c1c")

        _label(top, f"¿Eliminar '{pelicula.nombre}'?", 12, "white").pack(pady=12)

        ruta_img = pelicula.imagen if (pelicula.imagen and os.path.exists(pelicula.imagen)) else (RUTA_PLACEHOLDER if os.path.exists(RUTA_PLACEHOLDER) else "")
        tkimg = None
        if ruta_img:
            try:
                im = Image.open(ruta_img).copy()
                im.thumbnail((180, 180))
                tkimg = ImageTk.PhotoImage(im)
            except Exception:
                tkimg = None
        if tkimg:
            lbl = tk.Label(top, image=tkimg, bg="#1c1c1c")
            lbl.image = tkimg
            lbl.pack(pady=6)

        box = tk.Frame(top, bg="#1c1c1c")
        box.pack(pady=6)
        _btn(box, "Eliminar", lambda: (_eliminar_pelicula(pelicula), top.destroy()), bg="#d9534f", fg="white", w=12, pady=4).pack(side="left", padx=8)
        _btn(box, "Cancelar", top.destroy, bg="gray", fg="white", w=12, pady=4).pack(side="left", padx=8)

    def _eliminar_pelicula(pelicula):
        peliculas = catalogo.listar_peliculas()
        restantes = [p for p in peliculas if p.nombre != pelicula.nombre]
        with open(RUTA_ARCHIVO, "w", encoding="utf-8") as f:
            for p in restantes:
                f.write(f"{p.nombre}|{p.genero}|{p.descripcion}|{p.imagen}\n")
        messagebox.showinfo("CinePlus", f"'{pelicula.nombre}' fue eliminada.")
        cargar_lista()

    def eliminar_todas():
        if not catalogo.listar_peliculas():
            messagebox.showinfo("CinePlus", "Tu catálogo ya está vacío.")
            return
        if messagebox.askyesno("Confirmar", "¿Eliminar TODAS las películas del catálogo?"):
            catalogo.eliminar_catalogo()
            messagebox.showinfo("CinePlus", "Se eliminó todo el catálogo.")
            cargar_lista()

    combo_filtro.bind("<<ComboboxSelected>>", lambda e: cargar_lista())
    cargar_lista()

def eliminar_catalogo():
    if not catalogo.listar_peliculas():
        messagebox.showinfo("CinePlus", "Tu catálogo ya está vacío.")
        return
    if messagebox.askyesno("Confirmar", "¿Eliminar TODAS las películas del catálogo?"):
        catalogo.eliminar_catalogo()
        messagebox.showinfo("CinePlus", "Se eliminó todo el catálogo.")

def salir_programa():
    messagebox.showinfo("CinePlus", "Gracias por usar CinePlus. ¡Nos vemos en la próxima función!")
    root.destroy()

# ------------------ Inicio ------------------
mostrar_bienvenida()
root.mainloop()
