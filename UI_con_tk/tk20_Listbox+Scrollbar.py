import tkinter as tk

# Configuración inicial de la ventana
root = tk.Tk()
root.title("Listbox con Scrollbar")  # Título de la ventana
root.geometry("200x300+150+150")     # Tamaño y posición inicial

# Listbox (lista de elementos)
lst_items = tk.Listbox(root, font="Consolas 11")
lst_items.pack(side="left", expand=True, fill="both")

# Scrollbar vertical
scr_bar = tk.Scrollbar(root)
scr_bar.pack(side="right", fill="y")

# Asociar Scrollbar al Listbox
scr_bar.config(command=lst_items.yview)       # Scroll controla la vista vertical
lst_items.config(yscrollcommand=scr_bar.set)  # Listbox actualiza la scrollbar

# Insertar 50 elementos numerados en la lista
for num in range(1, 51):
    lst_items.insert(tk.END, f"Elemento {num}") # Insetar al final de la lista

root.mainloop()  # Iniciar el bucle principal