import tkinter as tk

# Configuración inicial de la ventana principal
root = tk.Tk()
root.title("Ejemplo de Canvas")     # Título de la ventana
root.geometry("400x400+150+150")    # Tamaño y posición inicial

# Crear el área de dibujo (Canvas) con fondo blanco
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)  # Expandir para ocupar toda la ventana

# Dibujar un óvalo rojo con borde azul
ovalo = canvas.create_oval(25, 20, 220, 150, outline="blue", width=4, fill="lightcoral")

# Crear y colocar un botón dentro del canvas
btn_canvas = tk.Button(root, text="Botón Canvas", width=15)
canvas.create_window(30, 220, window=btn_canvas, anchor="w")

# Dibujar una línea negra con múltiples segmentos
linea = canvas.create_line(100, 30, 120, 60, 50, 90, 100, 150, fill="black", width=2)

# Dibujar un rectángulo blanco
rectangulo = canvas.create_rectangle(40, 160, 100, 200, fill="white")

# Cargar y colocar una imagen en el canvas
img = tk.PhotoImage(file="UI_con_tk/imagen.png").subsample(5,5)
canvas.create_image(300, 250, image=img, anchor="center")
canvas.imagen = img   # Mantener la referencia a la imagen

# Dibujar un arco naranja con borde verde en el canvas
arco = canvas.create_arc(150, 90, 240, 190, start=30, extent=90, outline="#0fb335", fill="#eb721d", width=2)

# Agregar texto en varias líneas en el canvas
texto = canvas.create_text(200, 50, text="Texto 1\nTexto 2", font="Consolas 14 bold")

root.mainloop()   # Iniciar el bucle principal