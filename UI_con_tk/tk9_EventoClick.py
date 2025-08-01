import tkinter as tk

# Función para evento de clic del mouse
def ubicacionClick(event):
    lbl.config(text=f"Click en\nX={event.x}, Y={event.y}")

# Configuración inicial de la ventana
root = tk.Tk()
root.title("Eventos de Mouse")            # Título de la ventana
root.geometry("400x200++150+150")         # Tamaño y posición de la ventana
root.resizable(False, False)              # No se puede redimensionar la ventana

# Etiqueta
lbl = tk.Label(root, text="Haz clic aqui", font="Consolas 14")
lbl.config(bg="#c7f6ed")        # fondo de la etiqueta
lbl.pack(expand=True, fill="both")

# Bind de eventos
lbl.bind("<Button-1>", ubicacionClick)  # Clic izquierdo

root.mainloop()  # Ejecutar el bucle principal