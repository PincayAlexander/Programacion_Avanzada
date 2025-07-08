# * FUNCIONES DE PRIMER ORDEN 
print("---- FUNCIONES DE PRIMER ORDEN ----")
# Asignar una función a una variable
def saludar(nombre):
    return f"Hola, {nombre}!"

def despedir(nombre):
    return f"Adiós, {nombre}."

f1 = saludar  # Asignamos la función saludar a la variable f1
f2 = despedir # Asignamos la función despedir a la variable f2

print(f1("Ana"))  # Salida: Hola, Ana!

# Pasar una función como argumento
def aplicar_funcion(func, valor):
    # Llamar a la función que se pasa como argumento con el valor indicado
    return func(valor)

print(aplicar_funcion(f1, "Luis"))  # Salida: Hola, Luis!
print(aplicar_funcion(f2, "Luis"))  # Salida: Hola, Luis!


# * FUNCIONES ANÓNIMAS
print("\n---- FUNCIONES ANÓNIMAS ----")
# Definir función lambda que calcula el cubo de un número, en la variable cubo
cubo = lambda x: x * x * x
print(f"Cubo de 3: {cubo(3)}")  # Salida: 27

# Definir función que recibe otra función como argumento y la aplica a un valor
def ejecutar_funcion(func, valor):
    return func(valor)

# Se pasa la función 'cubo' como argumento y se aplica al valor 7
resultado = ejecutar_funcion(cubo, 7)
print(f"Cubo de 7: {resultado}")  # Salida: 343


# * FUNCIONES DE ORDEN SUPERIOR
print("\n---- FUNCIONES DE ORDEN SUPERIOR ----")
# map(funct, iterable)
def cuadrado(x):
    return x * x

numeros = [1, 2, 3, 4]
#  Aplica la función cuadrado a cada elemento de la lista
resultado = list(map(cuadrado, numeros))
print(f"Cuadrado: {resultado}")  # Salida: [1, 4, 9, 16]

# También se puede hacer con una función lambda
resultado = list(map(lambda x: x ** 2, numeros))
print(f"Cuadrado con lambda: {resultado}")  # Salida: [1, 4, 9, 16]

# filter(funct, iterable)
def es_par(n):
    return n % 2 == 0

numeros = [1, 2, 3, 4, 5]
# Filtra los números de la lista que son pares (devuelven True)
pares = list(filter(es_par, numeros))
print(f"Pares: {pares}")  # Salida: [2, 4]

# Usando función lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Pares con lambda: {pares}")  # Salida: [2, 4]

# reduce(funct, iterable)
from functools import reduce

def sumar(x, y):
    return x + y

numeros = [1, 2, 3, 4]
# Aplica una función acumulativa a los elementos de la lista
resultado = reduce(sumar, numeros)
print(f"Sumatoria: {resultado}")  # Salida: 10

# Usando función lambda
resultado = reduce(lambda x, y: x + y, numeros)
print(f"Sumatoria con lambda: {resultado}")  # Salida: 10

# zip(iterable1, iterable2, ...)
nombres = ["Ana", "Luis", "Carlos", "Isabel"]
edades = [25, 30, 22, 24]
# Combina las listas nombres y edades, agrupando sus elementos en tuplas por posición
combinado = list(zip(nombres, edades))
print(f"Combinando listas: {combinado}")  # Salida: [('Ana', 25), ('Luis', 30), ('Carlos', 22)]
