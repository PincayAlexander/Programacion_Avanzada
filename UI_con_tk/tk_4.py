import tkinter as tk

root = tk.Tk()
root.title("Ejemplo con etiquetas A, B, C, D")
root.geometry("400x300+150+150")

top = tk.Frame(root)
top.pack(fill='both', expand=True)

# A: izquierda y todo el alto
a = tk.Label(top, text="A", relief="groove", borderwidth=10, font="Times 24 bold", background="lightblue")
a.pack(side="left", fill="y", expand=True)

# B: abajo y todo el ancho
b = tk.Label(top, text="B", relief="groove", borderwidth=10, font="Times 24 bold", background="lightcoral")
b.pack(side="bottom", fill="x", expand=True)

# C: derecha
c = tk.Label(top, text="C", relief="groove", borderwidth=8, font="Times 24 bold", background="lightgreen")
c.pack(side="right", fill="y", expand=True)

# D: arriba
d = tk.Label(top, text="D", relief="groove", borderwidth=4, font="Times 24 bold", background="lightyellow")
d.pack(side="top", fill="x", expand=True)

root.mainloop()