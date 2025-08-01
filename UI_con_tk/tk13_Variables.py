import tkinter as tk

# Configuración inicial de la ventana
root = tk.Tk()
root.title("Variables con TK")         # Título de la ventana
root.geometry("250x160+150+150")       # Tamaño y posición de la ventana
root.resizable(False, False)           # No se puede redimensionar la ventana

# Variables acumular y entrada de usuario
acumulador = tk.DoubleVar(root)
valor = tk.DoubleVar(root)

# Función que se ejecuta al presionar Enter
def acumular(event):
    acumulador.set(acumulador.get() + valor.get())  # Suma el valor del campo de entrada
    valor.set(0.0)  # Reinicia el campo de entrada

# Etiqueta con el resultado del acumulador
lblResultado = tk.Label(root, textvariable=acumulador, font="Consolas 20")
lblResultado.pack(pady=20)

# Campo de entrada numérica
entryValor = tk.Entry(root, textvariable=valor)
entryValor.pack()

# Etiqueta de nstrucción
etiqueta_info = tk.Label(root, text="Ingrese un número \ny presione Enter", font="Consolas 10")
etiqueta_info.pack(fill="y", anchor="center")

# Evento de tecla Enter
entryValor.bind("<Return>", acumular)

root.mainloop()    # Ejecutar el bucle principal
