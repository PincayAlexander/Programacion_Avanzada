import tkinter as tk

# Función que se ejecuta al seleccionar una opción del popup
def saludo(opcion):
    print(f"Hola! Saludo desde {opcion}")

# Configuración inicial de la ventana
root = tk.Tk()
root.title("Menú Contextual")      # Título de la ventana
root.geometry("200x150+150+150")   # Tamaño y posición inicial
root.resizable(False, False)       # No se puede redimensionar la ventana

# Menú contextual
menuContextual = tk.Menu(root, tearoff=0)
menuContextual.add_command(label="Hola 1", command=lambda: saludo("'Opcion 1'"))  # Saludo clickeando la opción 1
menuContextual.add_command(label="Hola 2", command=lambda: saludo("'Opcion 2'"))  # Saludo clickeando la opción 2

# Función para muestrar el menú con click derecho
def mostrar(event):
    menuContextual.post(event.x_root, event.y_root)

# Área del click
frame = tk.Frame(root, bg="#dded9d")
frame.pack(fill="both", expand=True)

# Etiqueta
lbl = tk.Label(frame, text="De click derecho", font="Consolas 14", bg=frame["bg"])
lbl.pack(side="top", anchor="center")

# Evento de click al frame
frame.bind("<Button-3>", mostrar)

root.mainloop()   # Ejecutar el bucle principal