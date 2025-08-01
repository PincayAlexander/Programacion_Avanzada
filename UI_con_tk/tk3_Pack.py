import tkinter as tk

# Configuración inicial de la ventana
root = tk.Tk()
root.title("Posicionamiento con pack()")  # Título de la ventana
root.geometry("160x100+150+150")          # Tamaño y posición inicial de la ventana

# Frame contenedor
frame = tk.Frame(root)
frame.pack()  # Empaquetar a la ventana

# Creación de etiquetas con posiciones en la ventana
a = tk.Label(frame, text="A")
a.pack(side="left")  # Posición izquierda

b = tk.Label(frame, text="B")
b.pack(side="bottom")  # Posición abajo

c = tk.Label(frame, text="C")
c.pack(side="right")  # Posición derecha

d = tk.Label(frame, text="D")
d.pack(side="top")  # Posición arriba

# Lista de colores para fondo y texto (bg, fg)
colores = [
    ["#FF5733", "white"],  # A
    ["#33FF57", "black"],  # B
    ["#3357FF", "white"],  # C
    ["#D0CD0E", "black"]   # D
]

# Estilo para las etiquetas
for i, etiqueta in enumerate([a, b, c, d]):
    etiqueta.configure(
        relief="ridge",            # Borde de relieve
        borderwidth=6,             # Grosor del borde
        padx=10,                   # Espacio horizontal interno
        pady=5,                    # Espacio vertical interno
        bg=colores[i][0],          # Color de fondo
        fg=colores[i][1],          # Color de texto
        font="Arial 16 bold"       # Estilo de Fuente del texto
    )

root.mainloop() # Ejecutar el bucle principal