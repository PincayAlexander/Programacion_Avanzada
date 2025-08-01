import tkinter as tk

# Configuración inicial de la ventana
root = tk.Tk()
root.title("Checkbutton con TK")     # Título de la ventana
root.geometry("280x200+150+150")     # Tamaño y posición inicial
root.resizable(False, False)         # Ventana no redimensionable

# Variables TK para los checkbuttons
var1 = tk.IntVar()       # Variable entera para el primer checkbutton
var2 = tk.StringVar()    # Variable texto para el segundo checkbutton

# Función que actualiza la etiqueta con los valores actuales
def actualizar_valores():
    lblResultado.config(text=f"Estado actual: \nVariable 1 = {var1.get()} \nVariable 2 = {var2.get()}")

# Crear primer checkbutton (asociado a var1)
chck_num = tk.Checkbutton(
    root, 
    text="Opción Numérica", 
    variable=var1, 
    command=actualizar_valores,
    onvalue=1,                   # Valor cuando está marcado
    offvalue=0,                  # Valor cuando está desmarcado
    font="Consolas 12"           # Fuente del texto
)

# Segundo checkbutton (valor texto)
chck_texto = tk.Checkbutton(
    root, 
    text="Opción Textual", 
    variable=var2, 
    command=actualizar_valores,
    onvalue="Si",                # Valor cuando está marcado
    offvalue="No",               # Valor cuando está desmarcado
    font="Consolas 12"           # Fuente del texto
)
    
# Etiqueta para mostrar resultados
lblResultado = tk.Label(root, text="Estado actual: \nVariable 1 = 0 \nVariable 2 = No", font="Consolas 12")

# Empaquetar los widgets checkbuttons y label
for widget in (chck_num, chck_texto, lblResultado):
    widget.config(bg=root["bg"])
    widget.pack(anchor="center")        # Alineación al centro

# Mostrar valores iniciales
actualizar_valores()

root.mainloop()   # Iniciar el bucle principal