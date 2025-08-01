import tkinter as tk

# Configuración de la ventana principal
root = tk.Tk()
root.title("Etiquetas con TK")     # Título de la ventana
root.geometry("370x100+200+200")   # Tamaño y posición inicial de la ventana

# Frame contenedor
frame = tk.Frame(root, bg="white", padx=10, pady=10)
frame.pack(fill="both", expand=True)  # Empaquetar y ocupar toda la ventana

# Etiqueta
label = tk.Label(frame, text="Texto de Ejemplo")
# Estilo de la etiqueta
label.config(
    fg="#0d3f51",           # Color de texto
    bg="#abdbe3",           # fondo del label
    font="Consolas 22 bold",  # Estilo de Fuente del texto
    relief="groove",          # Borde
    bd=5                      # Grosor del borde
)
label.pack(padx=5, pady=5, fill="x", expand=True)  # Empaquetar y expandir al ancho

root.mainloop() # Ejecutar el bucle principal
