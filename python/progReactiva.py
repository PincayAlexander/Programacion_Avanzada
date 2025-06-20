# EJEMPLO 1: Flujo Síncrono con transformación y filtrado
from rx import from_iterable
from rx.operators import map, filter

print(" ---- EJEMPLO CON FLUJO SÍNCRONO ----")
# Crear un observable a partir de una lista
numeros = from_iterable([1, 2, 3, 4, 5, 6])
# Aplicar operadores: duplicar cada número y filtrar los mayores a 5
flujo = numeros.pipe(
    map(lambda x: x * 2),      # Transforma: 2, 4, 6, 8, 10, 12
    filter(lambda x: x > 5)    # Filtra: 6, 8, 10, 12
)
# Suscribirse al flujo y observar los resultados
flujo.subscribe(
    on_next=lambda x: print(f"Recibido: {x}"),
    on_completed=lambda: print("Flujo completo.")
)


#  EJEMPLO 2: Flujo Asíncrono con temporizador
import rx
from rx.operators import take
from time import sleep

print("\n ---- EJEMPLO CON FLUJO ASÍNCRONO EN INTERVALO DE 1 SEG ----")
# Crear un observable que emite un valor que aumenta cada segundo
flujo = rx.interval(1).pipe(
    take(5)  # Solo tomar los primeros 5 valores (0 - 4)
)
# Función para recibir los datos
flujo.subscribe(
    on_next=lambda x: print(f"Valor emitido: {x}"),
    on_completed=lambda: print("Flujo finalizado.")
)
# Esperar el tiempo suficiente para ver todos los valores
sleep(6)
