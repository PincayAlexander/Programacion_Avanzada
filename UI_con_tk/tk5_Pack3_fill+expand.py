import tkinter as tk

# Configuración inicial de la ventana
root = tk.Tk()
root.title("Posicionamiento con pack()")  # Título de la ventana
root.geometry("160x100+150+150")          # Tamaño y posición inicial

# Frame contenedor principal (expansible)
frame = tk.Frame(root)
frame.pack(fill='both', expand=True)  # Expande para ocupar toda la ventana

# Creación y posicionamiento de etiquetas
a = tk.Label(frame, text="A")
a.pack(side="left", fill="y")  # Posición izquierda, expande verticalmente

b = tk.Label(frame, text="B")
b.pack(side="bottom", fill="x")  # Posición abajo, expande horizontalmente

c = tk.Label(frame, text="C")
c.pack(side="right")  # Posición derecha

d = tk.Label(frame, text="D")
d.pack(side="top")  # Posición arriba

# Lista de colores para fondo y texto (bg, fg)
colores = [
    ["lightcoral", "#7c0000"],  # A
    ["lightgreen", "#007c04"],  # B
    ["lightblue", "#0a007c"],   # C
    ["lightyellow", "#a5b004"]  # D
]

# Estilo para las etiquetas
for i, etiqueta in enumerate([a, b, c, d]):
    etiqueta.configure(
        relief="groove",           # Tipo de Borde
        borderwidth=8,             # Grosor del borde
        padx=10,                   # Espacio horizontal interno
        pady=5,                    # Espacio vertical interno
        bg=colores[i][0],          # Color de fondo
        fg=colores[i][1],          # Color de texto
        font="Arial 16 bold"       # Estilo de Fuente del texto
    )

root.mainloop() # Ejecutar el bucle principal