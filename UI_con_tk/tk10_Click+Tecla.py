import tkinter as tk

# Función para evento de clic del mouse
def click(event):
    lbl.config(text=f"Mouse clicado en\nX={event.x}, Y={event.y}")

# Función para evento de teclado
def tecla(event):
    lbl.config(text=f"Tecla presionada:\n{event.keysym}\nCódigo: {event.keycode}\nChar: '{event.char}'")

# Configuración de ventana principal
root = tk.Tk()
root.title("Eventos de Mouse y Teclado")  # Título de la ventana
root.geometry("400x200+150+150")          # Tamaño y posición de la ventana
root.resizable(False, False)              # No se puede redimensionar la ventana

# Etiqueta
lbl = tk.Label(root, text="Haz clic o \npresiona una tecla", font="Consolas 14")
lbl.config(bg="#c7f6ed")        # fondo de la etiqueta
lbl.pack(expand=True, fill="both")
lbl.focus_set()

# Bind de eventos
lbl.bind("<Button-1>", click)  # Clic izquierdo
lbl.bind("<Key>", tecla)       # Teclado

root.mainloop()  # Ejecutar el bucle principal