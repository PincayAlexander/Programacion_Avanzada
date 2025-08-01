import tkinter as tk

# Configuración inicial de la ventana
root = tk.Tk()
root.title("Contador")             # Título de la ventana
root.geometry("200x150+150+150")  # Tamaño y posición inicial
root.resizable(False, False)       # No se puede redimensionar la ventana

# Función para incrementar del botón
def incrementar():
    lbl.config(text=str(int(lbl.cget("text")) + 1))

# Etiqueta
lbl = tk.Label(root, text="0", font="Consolas 20")
lbl.pack(pady=20)

# Botón
btn = tk.Button(root, text="Incrementar", command=incrementar)
btn.config(width=15, height=1, bg="#9cef89", font="Consolas 14")
btn.pack()

root.mainloop()   # Ejecutar el bucle principal