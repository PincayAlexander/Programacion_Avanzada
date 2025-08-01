import tkinter as tk

# Configuración inicial de la ventana
root = tk.Tk()
root.title("Posicionamiento con pack()")  # Título de la ventana
root.geometry("160x100+150+150")          # Tamaño y posición inicial

# Frame contenedor principal (expansible)
frame = tk.Frame(root)
frame.pack(fill='both', expand=True)  # Expande para ocupar toda la ventana

# Creación y posicionamiento de etiquetas con expansión
a = tk.Label(frame, text="A")
a.pack(side="left", expand=True, fill="y")  # Expande verticalmente

b = tk.Label(frame, text="B")
b.pack(side="bottom", expand=True, fill="both")  # Expande en ambas direcciones

c = tk.Label(frame, text="C")
c.pack(side="right")  # Posición derecha

d = tk.Label(frame, text="D")
d.pack(side="top")  # Posición arriba

# Lista de colores para fondo (bg)
colores = [
    ["#7c0000"],  # A
    ["#007c04"],  # B
    ["#0a007c"],  # C
    ["#a5b004"]   # D
]

# Estilo para las etiquetas
for i, etiqueta in enumerate([a, b, c, d]):
    etiqueta.configure(
        relief="groove",           # Tipo de Borde
        borderwidth=10,            # Grosor del borde
        padx=10,                   # Espacio horizontal interno
        pady=5,                    # Espacio vertical interno
        bg=colores[i],             # Color de fondo
        fg="white",                # Color de texto
        font="Arial 16 bold"       # Estilo de Fuente del texto
    )

root.mainloop()  # Ejecutar el bucle principal