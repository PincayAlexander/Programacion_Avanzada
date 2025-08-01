import tkinter as tk

# Configuración inicial de la ventana principal
root = tk.Tk()
root.title("Editor de Texto")         # Título de la ventana
root.geometry("400x150+150+150")      # Tamaño y posición inicial

# Función para insertar asterisco '*' en la posición actual del cursor
def insertarAsterisco():
    entryTxt.insert(tk.INSERT, "*")

# Función para limpiar todo el contenido del campo de texto
def limpiarTexto():
    entryTxt.delete(0, tk.END)

# Campo de entrada de texto
entryTxt = tk.Entry(root, font="Consolas 16")
entryTxt.config(
    bg="white",          # Fondo blanco
    fg="black",          # Texto negro
    selectbackground="lightblue"  # Color de selección
)
entryTxt.pack(pady=15, padx=5, fill="x")

# Frame para contener los botones
frm_btns = tk.Frame(root)
frm_btns.pack()

# Botón para insertar asterisco
btn_insertar = tk.Button(frm_btns, text="Insertar '*'", command=insertarAsterisco)
btn_insertar.config(
    width=12,
    height=1,
    font="Consolas 12",
    bg="#adf4e6",        # Color de fondo
    activebackground="#ba83fd"  # Color al presionar
)

# Botón para limpiar texto
btn_limpiar = tk.Button(frm_btns, text="Limpiar", command=limpiarTexto)
btn_limpiar.config(
    width=12,
    height=1,
    font="Consolas 12",
    bg="#adf4e6",        # Color de fondo
    activebackground="#fd8383"  # Color al presionar
)

# Posicionar botones uno al lado del otro
btn_insertar.pack(side="left", padx=10)
btn_limpiar.pack(side="left", padx=10)

root.mainloop()   # Iniciar el bucle principal de la aplicación