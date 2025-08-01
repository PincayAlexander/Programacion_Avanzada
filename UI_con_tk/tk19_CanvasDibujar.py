import tkinter as tk

# Función que inicia el trazo al hacer clic
def iniciar_trazo(event):
    x, y = lienzo.canvasx(event.x), lienzo.canvasy(event.y)
    lienzo.create_line(x, y, x, y, tags="trazo_actual", fill="blue", width=2)

# Función que continúa el trazo al arrastrar
def continuar_trazo(event):
    x, y = lienzo.canvasx(event.x), lienzo.canvasy(event.y)
    coords = lienzo.coords("trazo_actual") + [x, y]
    lienzo.coords("trazo_actual", *coords)

# Función que finaliza el trazo al soltar
def finalizar_trazo(event):
    lienzo.itemconfig("trazo_actual", tags=())

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lienzo de dibujo usando el mouse")    # Título de la ventana
root.geometry("500x400+150+150")                  # Tamaño y posición inicial

# Área de dibujo (Canvas)
lienzo = tk.Canvas(root, bg="white")
lienzo.pack(fill="both", expand=True)

# Asociar eventos de dibujo
lienzo.bind("<Button-1>", iniciar_trazo)          # Clic para iniciar
lienzo.bind("<B1-Motion>", continuar_trazo)       # Arrastrar para continuar
lienzo.bind("<ButtonRelease-1>", finalizar_trazo) # Soltar para terminar

root.mainloop()   # Iniciar el bucle principal