# Estructuras de datos en Python

# Listas
print("\n=== Listas ===")
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print("Lista original:", fruits)

# Contar ocurrencias
print("\nContar ocurrencias:")
print("Número de 'apple':", fruits.count('apple'))  # 2
print("Número de 'tangerine':", fruits.count('tangerine'))  # 0

# Buscar índice de un elemento
print("\nBuscar índices:")
print("Primer 'banana' en índice:", fruits.index('banana'))  # 3
print("'banana' después de índice 4:", fruits.index('banana', 4))  # 6

# Invertir lista
fruits.reverse()
print("\nLista invertida:", fruits)  # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

# Agregar al final
fruits.append('grape')
print("\nDespués de append('grape'):", fruits)  # ['...', 'grape']

# Ordenar elementos
fruits.sort()
print("\nLista ordenada:", fruits)  # ['apple', 'apple', ..., 'pear']

# Eliminar y retornar último elemento
popped = fruits.pop()
print("\nElemento eliminado con pop():", popped)  # 'pear'
print("Lista después de pop():", fruits)

#  Usar listas de tipo pilas (LIFO)
print("\n\n=== Pilas (LIFO) ===")
stack = [3, 4, 5]
print("Pila inicial:", stack)
stack.append(6)
stack.append(7)
print("Después de append(6) y append(7):", stack)
print("Elemento sacado con pop():", stack.pop())  # 7
print("Elemento sacado con pop():", stack.pop())  # 6
print("Pila final:", stack)  # [3, 4, 5]

# Usar listas de tipo cola (FIFO)
print("\n\n=== Colas (FIFO) ===")
from collections import deque
queue = deque(["Eric", "John", "Michael"])
print("Cola inicial:", queue)
queue.append("Terry")
queue.append("Graham")
print("Después de append('Terry') y append('Graham'):", queue)
print("Elemento sacado con popleft():", queue.popleft())  # 'Eric'
print("Elemento sacado con popleft():", queue.popleft())  # 'John'
print("Cola final:", queue)

# Comprensión de listas
print("\n\n=== Comprensión de listas ===")
# Crear lista de cuadrados
squares = [x**2 for x in range(10)]
print("\nCuadrados (0-9):", squares)

# Lista de combinaciones distintas
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print("\nCombinaciones (x != y):", combs)

# Varios ejemplos:
vec = [-4, -2, 0, 2, 4]
print("\nLista original:", vec)
print("Duplicar valores:", [x*2 for x in vec])
print("Filtrar no negativos:", [x for x in vec if x >= 0])
print("Valores absolutos:", [abs(x) for x in vec])

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print("\nFrutas con espacios:", freshfruit)
print("Frutas limpias:", [weapon.strip() for weapon in freshfruit])

print("\nTuplas (número, cuadrado):", [(x, x**2) for x in range(6)])

vec2d = [[1,2,3], [4,5,6], [7,8,9]]
print("\nMatriz 2D:", vec2d)
print("Aplanada:", [num for row in vec2d for num in row])

# Expresiones más complejas
from math import pi
print("\nRedondeos de pi:", [str(round(pi, i)) for i in range(1, 6)])

# Comprensiones anidadas
print("\n\n=== Comprensiones anidadas ===")
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print("\nMatriz original:")
for row in matrix:
    print(row)

# Transponer matriz
transposed = [[row[i] for row in matrix] for i in range(4)]
print("\nTranspuesta con comprensión:")
for row in transposed:
    print(row)

# Alternativa explícita
transposed_manual = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed_manual.append(transposed_row)
print("\nTranspuesta manual:")
for row in transposed_manual:
    print(row)

# Usar zip para transponer
print("\nTranspuesta con zip():")
print(list(zip(*matrix)))

# Instrucción del
print("\n\n=== Instrucción del ===")
a = [-1, 1, 66.25, 333, 333, 1234.5]
print("\nLista original:", a)
del a[0]
print("Eliminar a[0]:", a)
del a[2:4]
print("Eliminar rebanada a[2:4]:", a)
del a[:]
print("Vaciar lista (del a[:]):", a)
del a
# print(a)  # Error: 'a' ya no existe

# Tuplas y secuencias
print("\n\n=== Tuplas y secuencias ===")
t = 12345, 54321, 'hello!'
print("\nTupla creada:", t)
print("Elemento t[0]:", t[0])
u = t, (1, 2, 3, 4, 5)
print("Tuplas anidadas:", u)

v = ([1, 2, 3], [3, 2, 1])
print("\nTupla con listas mutables:", v)
v[0][0] = 999
print("Modificar lista dentro de tupla:", v)

# Tupla vacía y de un solo ítem
empty = ()
singleton = 'hello',
print("\nTupla vacía:", empty)
print("Tupla con un elemento:", singleton)

# Desempaquetado
x, y, z = t
print("\nDesempaquetado de tupla:")
print("x =", x, ", y =", y, ", z =", z)

# Conjuntos
print("\n\n=== Conjuntos ===")
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print("\nConjunto (duplicados eliminados):", basket)

print("\nVerificar existencia:")
print("'orange' en basket:", 'orange' in basket)
print("'crabgrass' en basket:", 'crabgrass' in basket)

# Operaciones entre conjuntos
a = set('abracadabra')
b = set('alacazam')
print("\nConjunto a:", a)
print("Conjunto b:", b)
print("\nOperaciones:")
print("a - b (diferencia):", a - b)
print("a | b (unión):", a | b)
print("a & b (intersección):", a & b)
print("a ^ b (diferencia simétrica):", a ^ b)

# Comprensión de conjuntos
print("\nComprensión de conjuntos:")
print({x for x in 'abracadabra' if x not in 'abc'})

# Diccionarios
print("\n\n=== Diccionarios ===")
tel = {'jack': 4098, 'sape': 4139}
print("\nDiccionario inicial:", tel)
tel['guido'] = 4127
print("Agregar 'guido':", tel)
tel['jack'] = 1111
print("Actualizar 'jack':", tel)
del tel['sape']
print("Eliminar 'sape':", tel)

print("\nClaves del diccionario:", list(tel))
print("Claves ordenadas:", sorted(tel))
print("'guido' en tel:", 'guido' in tel)

# Crear diccionario desde lista de tuplas
print("\nDiccionario desde tuplas:")
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))

# Comprensión de diccionarios
print("\nComprensión de diccionarios:")
print({x: x**2 for x in (2, 4, 6)})

# Métodos útiles
print("\nRecorrer diccionario:")
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(f"Clave: {k}, Valor: {v}")