import tkinter as tk

# Clase principal de la aplicación, hereda de Frame
class App(tk.Frame):
    
    #Inicializar el Frame principal
    def __init__(self, master=None):
        super().__init__(master)   # Iniciar la clase padre
        self.master = master       # ventana principal
        self.pack()                # Empaquetar
        self.crear_widgets()       # Inicializa los widgets       
    
    # Crear a los widgets
    def crear_widgets(self):
        # Etiqueta de texto con el mensaje
        self.txt = tk.Label(self, text="Hello World")     
        self.txt.pack(pady=10)
        # Botón para cerrar la app
        self.btn = tk.Button(self, text="Bye", command=self.master.destroy)
        self.btn.config(width=10, height=1)
        self.btn.pack()

# Configuración de la ventana principal
root = tk.Tk()
root.geometry("225x100+700+200")    # Tamaño y posición inicial de la ventana

# Crear la aplicación
ventana = App(master=root)          # Instancia de la app
ventana.master.title("Ventana con TK")    # Título de la ventana
ventana.mainloop()                  # Ejecutar el bucle principal