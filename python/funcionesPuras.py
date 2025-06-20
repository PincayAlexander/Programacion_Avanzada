
# Ejemplos de Funciones Puras
print("----- FUNCIÓN PURA -----")
# EJEMPLO 1: Suma dos números sin modificar ningún estado externo
def suma(num1, num2):
    return num1 + num2
# Llamado a la función sum con 10 y 35 como parámetros
print(f"Sumar 10 + 35: {suma(10, 35)}")  # Salida: 45

# EJEMPLO 2: Calcula el cubo de un número y retorna
def cubo(num):
    return num**3
# Primer llamado a la función cubo con el valor 3
print(f"Cubo de 3: {cubo(3)}")  # Salida: 27
# Segundo llamado a la función cubo con el valor 5
print(f"Cubo de 3 segundo llamado: {cubo(3)}")  # Salida: 27


# Ejemplo de Función Impura
print("\n----- FUNCIÓN IMPURA -----")
# EJEMPLO 1: Modifica directamente la lista original, elevando al cuadrado cada elemento
def square_lista(lista):
    for i, x in enumerate(lista):
        lista[i] = x**2  # Modifica el contenido de la lista original
# Lista original
enteros = [3, 5, 2, 4, 9]
# Antes de modificarla
print("Antes de llamar a la función:", enteros)
square_lista(enteros) # Llamar a la función
# Lista después de ser modificada
print("Después de llamar a la función:", enteros)

import time
from datetime import datetime
# EJEMPLO 2: Imprime la hora del sistema directamente y cada llamado es una hora diferente
def mostrar_hora():
    print("Hora actual:", datetime.now().strftime("%H:%M:%S"))
    time.sleep(3)
# Llamamos la función tres veces
mostrar_hora()
mostrar_hora()
mostrar_hora()
