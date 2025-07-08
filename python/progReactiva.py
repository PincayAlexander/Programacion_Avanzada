# EJEMPLO 1: Flujo Síncrono con transformación y filtrado
import rx
from rx import from_iterable
from rx import operators as ops

print("---- EJEMPLO 1: FLUJO SÍNCRONO ----")

# Observable: fuente de datos (una lista estática)
numeros = from_iterable([1, 2, 3, 4, 5, 6])

# Aplicar operadores con pipe:
# map() transforma los datos (duplica los valores en la lista)
# filter() los filtra (mantiene los valores mayores a 5)
flujo = numeros.pipe(
    ops.map(lambda x: x * 2),      # Transforma:  [2, 4, 6, 8, 10, 12]
    ops.filter(lambda x: x > 5)    # Filtra:      [6, 8, 10, 12]
)

# Observer: Define cómo reaccionar ante los datos (ejecuta tramsformación y filtro)
flujo.subscribe(
    on_next=lambda x: print(f"Recibido: {x}"),      # Cada valor emitido
    on_error=lambda e: print(f"Error: {e}"),        # Si ocurre un error
    on_completed=lambda: print("Flujo completo.")   # Cuando el flujo termina
)


#  EJEMPLO 2: Flujo Asíncrono con temporizador
import rx
from rx import operators as ops
from time import sleep

print("\n---- EJEMPLO 2: FLUJO ASÍNCRONO CADA 1 SEGUNDO ----")

# Observable: fuente de datos que emite valores cada segundo
flujo = rx.interval(1).pipe(
    ops.take(5)  # Operador para limitar las emisiones a solo los primeros 5
)

# Observer: reacciona a cada emisión del observable
flujo.subscribe(
    on_next=lambda x: print(f"Valor emitido: {x}"),
    on_error=lambda e: print(f"Ocurrió un error: {e}"),
    on_completed=lambda: print("Flujo finalizado.")
)

# Espera lo suficiente para que el observable emita todos los valores
sleep(6)


#  EJEMPLO 3: Subject (observable + observer)
import rx
from rx import from_iterable
from rx.subject import Subject

print("\n---- EJEMPLO 3: USO DE SUBJECT PARA COMPARTIR ----")

# Subject actúa como Observable (emite) y como Observer (recibe)
canal = Subject()

# MULTICASTING: varios observers se suscriben al mismo Subject
print("MULTICASTING")
# Observer 1
canal.subscribe(on_next=lambda x: print(f"Observer 1 recibió: {x}"))
# Observer 2
canal.subscribe(on_next=lambda x: print(f"Observer 2 recibió: {x}"))

# Emitir mensaje manualmente
canal.on_next("Mensaje")

print("INTERMEDIACIÓN")
# INTERMEDIACIÓN: Subject(canal) se suscribe a otro Observable (lista
datos = from_iterable(["Dato A", "Dato B", "Dato C"])
# El subject(canal) "recibe" y reenvía a todos sus observers ya declarados
datos.subscribe(canal) 

