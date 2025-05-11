
class FuncionesLista:
    def __init__(self, lista):
        self.__lista = lista
    
    def getList(self):
        return self.__lista
    
    def search_mayorMenor(self):
        mayor = menor = self.__lista[0]
        for num in self.__lista:
            if num > mayor:
                mayor = num
            elif num < menor:
                menor = num
        return (mayor, menor)
    
    def count_parImpar(self):
        par = impar = 0
        for e in self.__lista:
            if e % 2 == 0:
                par += 1
            else:
                impar += 1
        return (par, impar)
    
    def delete_duplicates(self):
        list_unico = []
        idx = 0
        for e in self.__lista:
            if e not in list_unico:
                list_unico.append(e)
            else:
                idx += 1
        return (idx, list_unico)
    
    def order_list(self):
        self.__lista.sort()
    
    def invert_list(self):
        self.__lista.reverse()

def menu():
    while True:
        print("\n\n*** MENÚ DE LISTAS " + "*"*30)
        print("0. Salir")
        print("1. Buscar el número mayor y menor en la lista")
        print("2. Contar elementos pares e impares en la lista")
        print("3. Eliminar elementos duplicados en la lista")
        print("4. Ordenar lista")
        print("5. Invertir Lista")

        opcion = input("Elige una opción: ")
        
        if opcion == "0":
            print("Saliendo del programa.....") 
            break
        elif opcion not in {"1", "2", "3", "4", "5"}:
            print("ERROR: Opción inválida. Intente de nuevo.....")
            continue
        
        try:
            print()
            ingreso = input("Ingresa una lista de elementos separados por comas: ").strip().split(",")
            elementos = [e.strip() for e in ingreso] 
            
            if opcion in {"1", "2"}:
                elementos = [int(e) for e in elementos]
            
            lista = FuncionesLista(elementos)
            print(f"\nLista: {lista.getList()}")
            
        except Exception as ex:
            print("Error al ingresar la lista")
            if opcion in {"1", "2"}:
                print(f"Para la opcion {opcion} se debe ingresar una lista unicamente de números")
            continue

        if opcion == "1":
            mayor, menor = lista.search_mayorMenor()
            print(f"El número mayor en la lista es: {mayor}")
            print(f"El número menor en la lista es: {menor}")
        
        elif opcion == "2": 
            pares, impares = lista.count_parImpar()
            print(f"Cantidad de números pares:   {pares}")
            print(f"Cantidad de números impares: {impares}")

        elif opcion == "3":
            idx, sin_duplicado = lista.delete_duplicates()
            print(f"Se borro {idx} elementos duplicados")
            print(f"Lista sin duplicados: {sin_duplicado}")

        elif opcion == "4":
            lista.order_list()
            print(f"Lista ordenada: {elementos}")

        elif opcion == "5":
            lista.invert_list()
            print(f"Lista invertida: {elementos}")


if __name__ == "__main__":
    menu()

#numeros = [10, 24, 56, 7, 34]
#numeros = [1, 2, 2, 3, 4, 4, 5]
#numeros = [34, 12, 5, 76, 23]
