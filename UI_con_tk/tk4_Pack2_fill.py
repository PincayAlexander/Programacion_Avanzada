import tkinter as tk

# Configuración inicial de la ventana
root = tk.Tk()
root.title("Posicionamiento con pack()")  # Título de la ventana
root.geometry("160x100+150+150")          # Tamaño y posición inicial

# Frame contenedor principal
frame = tk.Frame(root)
frame.pack()  # Empaquetar en la ventana

# Creación y posicionamiento de etiquetas
a = tk.Label(frame, text="A")
a.pack(side="left", fill="y")  # Posición izquierda, expande verticalmente

b = tk.Label(frame, text="B")
b.pack(side="bottom", fill="x")  # Posición abajo, expande horizontalmente

c = tk.Label(frame, text="C")
c.pack(side="right")  # Posición derecha

d = tk.Label(frame, text="D")
d.pack(side="top")  # Posición arriba

# Lista de colores para fondo
colores = [
    ["lightcoral"],  # A
    ["lightgreen"],  # B
    ["lightblue"],   # C
    ["lightyellow"]  # D
]

# Estilo para las etiquetas
for i, widget in enumerate([a, b, c, d]):
    widget.configure(
        relief="ridge",            # Borde en relieve
        borderwidth=10,             # Grosor del borde
        padx=10,                   # Espacio horizontal interno
        pady=5,                    # Espacio vertical interno
        bg=colores[i],          # Color de fondo
        fg="black",          # Color de texto
        font="Arial 16 bold"       # Fuente del texto
    )

root.mainloop()  # Ejecutar el bucle principal