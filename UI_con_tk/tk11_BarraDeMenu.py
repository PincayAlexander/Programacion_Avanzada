import tkinter as tk

# Funciones del menú
def abrir(): 
    print("Comando: Abrir")
    
def guardar(): 
    print("Comando: Guardar")
    
def ayuda(): 
    print("Comando: Ayuda")

# Configuración inicial de la ventana
root = tk.Tk()
root.title("Menu de Barra")         # Título de la ventana 
root.geometry("180x100+150+150")    # Tamaño y posición en pantalla

# Declarar barra de menú
menu = tk.Menu(root)

# Definir un submenu "Archivo"
archivo = tk.Menu(menu, tearoff=0)
archivo.add_command(label="Abrir", command=abrir)       # Abrir
archivo.add_command(label="Guardar", command=guardar)   # Guardar
menu.add_cascade(label="Archivo", menu=archivo)         # Añadir archivo al menú

# Añadir ayuda directamente al menú
menu.add_command(label="Ayuda", command=ayuda)

# Establecer el menu en la ventana
root.config(menu=menu)

root.mainloop()   # Ejecutar el bucle principal