# ------------------------------------------------------------------------
# LISTAS
# ------------------------------------------------------------------------
print("\n--------------------------- LISTAS ---------------------------")
lenguajes = ['Python', 'JavaScript', 'Java', 'C++', 'Python', 'Ruby']
print(f" * Lista de Lenguajes de Programación: {lenguajes}")

# Contar ocurrencias
print(f" * Número de ocurrencias 'Python' en la lista:  {lenguajes.count('Python')}")
print(f" * Número de ocurrencias 'Go' en la lista:      {lenguajes.count('Go')}")

# Buscar índice de un elemento
print(f" * Primer 'Java' en índice:      {lenguajes.index('Java')}")
print(f" * 'Python' después de índice 2: {lenguajes.index('Python', 2)}")

# Invertir lista
lenguajes.reverse()
print(f" * Lista invertida:         {lenguajes}")

# Agregar al final
lenguajes.append('TypeScript')
print(f" * Insertar 'TypeScript':   {lenguajes}")

# Insertar en posición específica
lenguajes.insert(2, 'Kotlin')
print(f" * Insertar 'Kotlin' en posición 2: {lenguajes}")

# Remover un elemento por valor
lenguajes.remove('Ruby')
print(f" * Eliminar 'Ruby':        {lenguajes}")

# Eliminar y retornar el último elemento
eliminado = lenguajes.pop()
print(f" * Elemento eliminado con pop():    {eliminado}")
print(f" * Lista tras eliminación:          {lenguajes}")

# Ordenar alfabéticamente
lenguajes.sort()
print(f" * Lista ordenada:       {lenguajes}")

# Copiar lista
copia_lenguajes = lenguajes.copy()
print(f" * Copia de la lista:    {copia_lenguajes}")

# Vaciar lista
lenguajes.clear()
print(f" * Lista tras clear():   {lenguajes}")

# PROGRAMACIÓN FUNCIONAL CON LISTAS
print("\nEjemplos de programación funcional con LISTAS")
# Convertir a mayúsculas (con map)
resultado = list(map(str.upper, copia_lenguajes))
print(f" * Lenguajes en mayúsculas (map):   {resultado}")

# Obtener longitud de cada elemento (con map)
resultado = list(map(len, copia_lenguajes))
print(f" * Longitud de cada palabra (map):  {resultado}")

# Crear nueva lista sin 'Python' (con filter)
resultado = list(filter(lambda x: x != 'Python', copia_lenguajes))
print(f" * Lista sin 'Python' (filter):     {resultado}")


# ------------------------------------------------------------------------
# LISTAS DE TIPO PILA (LIFO)
# ------------------------------------------------------------------------
print("\n\n------------------------ PILAS (LIFO) ------------------------")
pila_tareas = ['Leer email', 'Escribir informe', 'Enviar reporte']
print(f" * Pila inicial: {pila_tareas}")

# Agregar elementos al final (push)
pila_tareas.append('Preparar presentación')
pila_tareas.append('Revisar código')
print(f" * Después de ingresar 2 tareas: {pila_tareas}")

# Eliminar elementos del final (pop)
print(f" * Elemento sacado con pop():    {pila_tareas.pop()}")
print(f" * Elemento sacado con pop():    {pila_tareas.pop()}")
print(f" * Pila final: {pila_tareas}")

# Programación funcional con PILAS
print("\nEjemplos de programación funcional con PILAS ")
# Filtrar solo tareas que contienen la palabra 'reporte'
resultado = list(filter(lambda t: 'reporte' in t.lower(), pila_tareas))
print(f" * Tareas relacionadas a 'reporte' (filter): {resultado}")


# ------------------------------------------------------------------------
# LISTAS DE TIPO COLA (FIFO)
# ------------------------------------------------------------------------
print("\n\n------------------------ COLAS (FIFO) ------------------------")
from collections import deque

cola_personas = deque(['ANA', 'LUIS', 'SOFIA'])
print(f" * Cola inicial:      {cola_personas}")

# Agregar elementos al final (enqueue)
cola_personas.append('CARLOS')
cola_personas.append('MARIA')
print(f" * Después de ingresar 2 personas: {cola_personas}")

# Eliminar elementos desde el inicio (dequeue)
print(f" * Persona eliminada: {cola_personas.popleft()}")
print(f" * Persona eliminada: {cola_personas.popleft()}")
print(f" * Cola final:        {cola_personas}")

# Programación funcional con COLAS
print("\nEjemplos de programación funcional con COLAS ")
# Transformar nombres a minuscula
resultado = list(map(str.lower, cola_personas))
print(f" * Nombres en mayúsculas (map):    {resultado}")


# ------------------------------------------------------------------------
# CONPRESIÓN DE LISTAS
# ------------------------------------------------------------------------
print("\n\n------------------- CONPRESIÓN DE LISTAS --------------------")
# Crear lista de cuadrados
cuadrados = [x**2 for x in range(10)]
cuadrados_map = list(map(lambda x: x**2, range(10))) # con programación funcional
print(f" * Cuadrados 0 - 9:  {cuadrados}")
print(f" * Cuadrados 0 - 9 con lambda y map:  {cuadrados_map}")

# Lista de combinaciones distintas donde x != y
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(f" * Combinaciones (x != y): {combs}")

# Operaciones con una lista
vec = [-4, -2, 0, 2, 4]
print(" Lista:", vec)

# Valores x 2
duplicados = list(map(lambda x: x * 2, vec))  # equivalente a [x * 2 for x in vec] 
print(f" * Valores duplicados: {duplicados}")

# Filtrar no negativos
no_negativos = list(filter(lambda x: x >= 0, vec))  # equivalente a [x for x in vec if x >= 0]
print(f" * Solo no negativos: {no_negativos}")
 
# Aplicar valores absolutos
absolutos = [abs(x) for x in vec]
print(f" * Valores absolutos: {absolutos}")

# Lista con espacios
txt = ['  hola', ' adios ', 'hasta luego  ']
print(f" * Lista con espacios: {txt}")
# Limpiar espacios con strip()
limpias = list(map(str.strip, txt))  # equivalente a [i.strip() for i in txt]
print(f" * Lista sin espacios: {limpias}")

# Tuplas de x y su cubo (x, x**3)
tuplas_cuadrados = list(map(lambda x: (x, x**3), range(6)))  # equivalente a [(x, x**3) for x in range(6)]
print(f" * Tuplas (número, cubo): {tuplas_cuadrados}")


# ------------------------------------------------------------------------
# CONPRESIÓN DE LISTAS ANIDADAS
# ------------------------------------------------------------------------
print("\n\n--------------- CONPRESIÓN DE LISTAS ANIDADAS ---------------")
# Matriz de ejemplo 3x4
matrix = [
    [10, 20, 30, 40],
    [5, 6, 7, 8],
    [99, 10, 11, 12],
]
print("Matriz inicial:")
for row in matrix:
    print(f"{row}")

# Transponer matriz con compesion de listas
transpuesta = [[row[i] for row in matrix] for i in range(4)]
print(" * Transpuesta (con comprensión de listas):")
for row in transpuesta:
    print(f"   {row}")

# Transponer matriz con zip y desempaquetado
transpuesta_zip = list(zip(*matrix))
print(" * Transpuesta (con zip):")
for row in transpuesta_zip:
    print(f"   {row}")


# ------------------------------------------------------------------------
# INSTRUCCIÓN del
# ------------------------------------------------------------------------
print("\n\n---------------------- INSTRUCCIÓN del -----------------------")

# Lista de calificaciones
calificaciones = [8.5, 9.0, 7.2, 10.0, 9.5]
print(f"\n * Lista inicial:              {calificaciones}")

# Eliminar primer elemento
del calificaciones[0]
print(f" * Eliminar calificaciones[0]:   {calificaciones}")

# Eliminar una rebanada
del calificaciones[1:3]
print(f" * Eliminar calificaciones[1:3]: {calificaciones}")

# Vaciar toda la lista usando del [:]
del calificaciones[:]
print(f" * Vaciar lista con del [:]:     {calificaciones}")

# Eliminar la variable completamente
del calificaciones 
# print(calificaciones)  -->  Error: 'calificaciones' ya no existe


# ------------------------------------------------------------------------
# TUPLAS Y SECUENCIAS
# ------------------------------------------------------------------------
print("\n\n-------------------- TUPLAS Y SECUENCIAS ---------------------")

# Tupla con títulos de libros
libros = "Harry Potter", "Shadow Hunters", "Sombra y Hueso"
print(f" * Tupla de libros: {libros}")
print(f" * Primer libro (libros[0]): {libros[0]}")

# Tupla anidada (tupla dentro de tupla)
tupla_anidada = libros, ("Dune", "Fundación")
print(f" * Tuplas anidadas: {tupla_anidada}")

# Tupla con listas 
capitulos = (["Intro", "Capítulo 1"], ["Resumen", "Epílogo"])
print(f" * Tupla con listas: {capitulos}")
capitulos[0][0] = "Prólogo"
print(f" * Modificar elemento [0][0]: {capitulos}")

# Tuplas vacías y con un solo elemento
vacia = ()
uno = "Crónica de una muerte anunciada",  # La coma la vuelve tupla
print(f" * Tupla vacía: {vacia}")
print(f" * Tupla con un solo elemento: {uno}")

# Desempaquetado de tupla
titulo1, titulo2, titulo3 = libros
print(f" * Desempaquetado de libros:")
print(f"   1. titulo1= {titulo1}")
print(f"   2. titulo2= {titulo2}")
print(f"   3. titulo3= {titulo3}")


# ------------------------------------------------------------------------
# CONJUNTOS
# ------------------------------------------------------------------------
print("\n\n------------------------- CONJUNTOS --------------------------")
# Crear un conjunto con elementos duplicados
lenguajes = {'Python', 'JavaScript', 'Python', 'C++', 'Java', 'C++'}
print(f" * Conjunto de lenguajes (no conserva duplicados): {lenguajes}")

# Verificar existencia de elementos
print(f" * ¿'Python' está en el conjunto?:  {'Python' in lenguajes}")
print(f" * ¿'Go' está en el conjunto?:      {'Go' in lenguajes}")

# Operaciones entre conjuntos
a = set('abracadabra')
b = set('alacazam')

print(f" * Conjunto a (abracadabra): {a}")
print(f" * Conjunto b (alacazam):    {b}")

print(" * Operaciones entre conjuntos:")
print(f"   - Diferencia (a - b):           {a - b}")
print(f"   - Unión (a | b):                {a | b}")
print(f"   - Intersección (a & b):         {a & b}")
print(f"   - Diferencia simétrica (a ^ b): {a ^ b}")

# Comprensión de conjuntos
comprension = set(filter(lambda x: x not in 'abc', 'abracadabra'))  # equivalente a {x for x in 'abracadabra' if x not in 'abc'}
print(f"\n * Comprensión de conjunto (letras no en 'abc'): {comprension}")


# ------------------------------------------------------------------------
# DICCIONARIOS
# ------------------------------------------------------------------------
print("\n\n------------------------ DICCIONARIOS ------------------------")
paises = {'Ecuador': 'Quito', 'Francia': 'París'}
print(f"\n * Diccionario inicial:       {paises}")

# Agregar un nuevo país
paises['Japón'] = 'Tokio'
print(f" * Añadiendo 'Japón':           {paises}")

# Editado la capital de un país
paises['Ecuador'] = 'Guayaquil'
print(f" * Editar capital de 'Ecuador': {paises}")

# Eliminar un país
del paises['Francia']
print(f" * Eliminar 'Francia':          {paises}")

# Obtener claves como lista
print(f" * Lista de países del diccionario:  {list(paises)}")

# Crear diccionario desde tuplas
paises2 = dict([('Brasil', 'Brasilia'), ('Italia', 'Roma'), ('India', 'Nueva Delhi')])
print(f" * Diccionario desde tuplas:    {paises2}")

# Comprensión de diccionarios: país → longitud del nombre de su capital
capitales_largo = dict(map(lambda x: (x[0], len(x[1])), paises2.items())) # equivalente a {pais: len(capital) for pais, capital in paises2.items()}
print(f" * Longitud de cada capital:    {capitales_largo}")

# Recorrer diccionario
print(" * Recorrido del diccionario:")
for pais, capital in paises2.items():
    print(f"   - País: {pais}, Capital: {capital}")


# ------------------------------------------------------------------------
# TÉCNICAS DE ITERACIÓN
# ------------------------------------------------------------------------
print("\n\n--------------------- TÉCNICAS DE ITERACIÓN ---------------------")

# range() - Itera n veces (0 a n-1)
print("\n * Iteración con range(3):", end=" ")
for i in range(3):
    print(i, end=" ")  # Output: 0 1 2

# dict.items() - Recorre claves y valores de un diccionario
print("\n\n * Iteración con dict.items():")
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(f"   - {k}: {v}")

# enumerate() - Obtiene índice y valor de una secuencia
print("\n * Iteración con enumerate():")
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(f"   - Posición {i}: {v}")

# zip() - Combina múltiples secuencias en paralelo
print("\n * Iteración con zip():")
questions = ['nombre', 'objetivo', 'color favorito']
answers = ['Lancelot', 'el santo grial', 'azul']
for q, a in zip(questions, answers):
    print(f"   - ¿Cuál es tu {q}? Es {a}.")

# reversed() - Itera en orden inverso
print("\n * Iteración con reversed(range(1, 10, 2)):", end=" ")
for i in reversed(range(1, 10, 2)):
    print(i, end=" ")  # Output: 9 7 5 3 1

# sorted() - Itera en orden ascendente
print("\n\n * Iteración con sorted(lista):", end=" ")
for fruta in sorted(['manzana', 'pera', 'banana']):
    print(fruta, end=" ")  # Output: banana manzana pera

# set() - Itera valores únicos (sin duplicados)
print("\n\n * Iteración con set():", end=" ")
for item in set(['a', 'b', 'a', 'c']):
    print(item, end=" ")  # Output: a b c (orden no garantizado)
