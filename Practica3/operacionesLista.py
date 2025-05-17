class MetodosLista:
    def __init__(self, L = [], tam = 0):
        self.elementos = L
        self.tam = tam

    def ingresar_items(self, tam):
        self.elementos = []
        self.tam = tam
        i = 0
        while i < self.tam:
            try:
                item = int(input(f"Elemento {i + 1}  ->  "))
                self.elementos.append(item)
                i += 1
            except ValueError:
                print("Entrada no válida. Debe ingresar un número")

    def eliminar_item(self, valor):
        if not self.elementos:
            print("La lista está vacía.")
            return
        try:
            self.elementos.remove(valor)
            print(f"Elemento {valor} eliminado.")
        except ValueError:
            print("El valor no está en la lista.")
    
    def mostrar_items(self):
        print(self.elementos)

    def calcular_promedio(self):
        if not self.elementos:
            print("La lista está vacía.")
            return
        return sum(self.elementos) / self.tam

    def calcular_factorial(self):
        try:
            num = int(input("\nIngrese un número para calcular su factorial: "))
            if num < 0:
                print("El factorial no está definido para números negativos.")
                return
            lista = [i for i in range(1, num + 1)]
            fact = 1
            for i in lista:
                fact *= i
            print(f"El factorial de {num} es: {fact}")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            return
        
    def calcular_fibonacci(self):
        try:
            num = int(input("\nIngrese la cantidad de términos de Fibonacci: "))
            if num <= 0:
                print("Debe ingresar un número positivo.")
                return
            fibo = [0] * num
            fibo[0], fibo[1] = 0, 1
            for i in range(2, num):
                fibo[i]= fibo[i-1] + fibo[i-2]
            print(f"Serie Fibonacci hasta {num} términos: {fibo}")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            return

    def buscar_item_mayor(self):
        if not self.elementos:
            print("La lista está vacía.")
            return
        return max(self.elementos)

    def buscar_item_menor(self):
        if not self.elementos:
            print("La lista está vacía.")
            return
        return min(self.elementos)

    def order_items(self):
        if not self.elementos:
            print("La lista está vacía.")
            return
        self.elementos.sort()
        print(f"\nLista ordenada: {self.elementos}")

def menu():
    lista = MetodosLista()
    while True:
        print("\n===== MENÚ =====")
        print("1. Ingresar números de la Lista")
        print("2. Eliminar número de la Lista")
        print("3. Mostrar números de la Lista")
        print("4. Calcular promedio")
        print("5. Calcular factorial")
        print("6. Calcular serie Fibonacci")
        print("7. Encontrar número mayor de la Lista")
        print("8. Encontrar número menor de la Lista")
        print("9. Ordenar números de la lista")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            try:
                tam = int(input("\nIngrese el tamaño de la lista: "))
                lista.ingresar_items(tam)
            except ValueError:
                print("Entrada no válida. Debe ingresar un número.")
        elif opcion == "2":
            try:
                item = int(input("\nIngrese el número a eliminar: "))
                lista.eliminar_item(item)
            except ValueError:
                print("Entrada no válida. Debe ingresar un número.")
        elif opcion == "3":
            print("\nLista actual: ")
            lista.mostrar_items()
        elif opcion == "4":
            print(f"\nEl promedio es: {lista.calcular_promedio():.2f}")
        elif opcion == "5":
            lista.calcular_factorial()
        elif opcion == "6":
            lista.calcular_fibonacci()
        elif opcion == "7":
            mayor = lista.buscar_item_mayor()
            if mayor is not None:
                print(f"\nEl número mayor es: {mayor}")
        elif opcion == "8":
            menor = lista.buscar_item_menor()
            if menor is not None:
                print(f"\nEl número menor es: {menor}")
        elif opcion == "9":
            lista.order_items()
        elif opcion == "0":
            print("\nSaliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
