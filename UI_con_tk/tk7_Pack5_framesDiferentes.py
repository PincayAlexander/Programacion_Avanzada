import tkinter as tk

# Configuración inicial de la ventana
root = tk.Tk()
root.title("Posicionamiento con pack()")  # Título de la ventana
root.geometry("160x100+150+150")          # Tamaño y posición inicial

# Frame contenedor principal
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)  # Expande para ocupar toda la ventana

# frame Interno para etiquetas A, B, C
frameInterno = tk.Frame(frame)
frameInterno.pack(fill='x', expand=False)  # Expande horizontalmente

# Creación de etiquetas (todas en frameInterno excepto D)
a = tk.Label(frameInterno, text="A")
b = tk.Label(frameInterno, text="B")
c = tk.Label(frameInterno, text="C")
d = tk.Label(frame, text="D")  # Etiqueta D fuera del frameInterno

# Lista de colores para fondo (bg)
colores = [
    ["#6f11cc"],    # A
    ["#03a108"],    # B
    ["#23d7ad"],    # C
    ["#d5891d"]     # D
]

# Empaquetado y Estilo para las etiquetas
for i, etiqueta in enumerate([a, b, c, d]):
    etiqueta.pack(side="left", expand=True, fill="both")
    etiqueta.config(
        relief="solid",           # Tipo de Borde
        borderwidth=2,            # Grosor del borde
        bg=colores[i],            # Color de fondo
        fg="black",               # Color de texto
        font="Arial 16 bold"      # Estilo de Fuente del texto
    )

root.mainloop()  # Ejecutar el bucle principal