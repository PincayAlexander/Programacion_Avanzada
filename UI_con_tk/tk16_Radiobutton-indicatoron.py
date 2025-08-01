import tkinter as tk

# Configuración inicial de la ventana
root = tk.Tk()
root.title("Radiobutton con TK")     # Título de la ventana
root.geometry("250x200+150+150")     # Tamaño y posición inicial

# Variable TK para almacenar el color seleccionado
color = tk.StringVar()  
color.set("black")    # Valor inicial: negro

# Función para actualizar el color de fondo
def cambiarColor():
    lbl.config(bg=color.get())

# Etiqueta para cambiar el color
lbl = tk.Label(root, relief="ridge", background=color.get())
lbl.pack(fill='both', expand=True)

# Opciones de colores disponibles
opciones_colores = [
    ("Negro", "black"),
    ("Rojo", "red"),
    ("Azul", "blue"),
    ("Verde", "green")
]

# Crear RadioButtons para cada opción de color
for txt, valor in opciones_colores:
    rbtn = tk.Radiobutton(
        root,
        text=txt,
        value=valor,
        variable=color,
        command=cambiarColor,
        indicatoron=False,     # Muetra las opciones como botones sin ciculo de selección
        font="Consolas 12"
    )
    rbtn.pack(fill="x")     # Expandirse al ancho
    
root.mainloop()   # Iniciar el bucle principal