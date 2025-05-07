# Pincay Baque John Alexander
# Programación Avanzada - paralelo A

from math import *        #funciones matemáticas

class figura: 
    def __init__(self, base, altura): 
        self.__base = base
        self.__altura = altura 
    
    #Getter & Setter
    def setBase(self, base):
        self.__base = base
    def setAltura(self, altura):
        self.__altura = altura
    def getBase(self):
        return self.__base
    def getAltura(self):
        return self.__altura
    
    #Metodo
    def info(self):
        print(f"Base: {self.getBase()}      Altura: {self.getAltura()}")
    def area(self): 
        return 0
    def perimetro(self): 
        return 0
    
class rectangulo(figura):
    def __init__(self, base, altura): 
        super().__init__(base, altura)
    #Metodos
    def info(self):
        print("RECTANGULO")
        super().info()
        print(f"Perimetro: {self.perimetro()}      Area: {self.area()}")
    def area(self):
        return self.getBase() * self.getAltura()
    def perimetro(self):
        return (2 * self.getBase()) + (2 * self.getAltura())
    
class triangulo_rectangulo(figura):
    def __init__(self, base, altura): 
        super().__init__(base, altura)
    #Metodos
    def info(self):
        print("TRIANGULO RECTANGULO")
        super().info()
        print(f"Hipotenusa: {self.hipotenusa()}      Perimetro: {self.perimetro()}      Area: {self.area()}")
    def hipotenusa(self):
        return sqrt((self.getBase()**2) + (self.getAltura()**2))    
    def area(self):
        return (self.getBase() * self.getAltura()) / 2
    def perimetro(self):
        return self.getBase() + self.getAltura() + self.hipotenusa()
    
class hexagono(figura):
    def __init__(self, base, altura): 
        super().__init__(base, altura)
    #Metodos
    def info(self):
        print("HEXAGONO")
        super().info()
        print(f"Perimetro: {self.perimetro()}      Area: {self.area()}") 
    def area(self):
        return ((self.getBase() * self.getAltura()) / 2 ) * 12
    def perimetro(self):
        return self.getBase() * 12
    
class menu_figura:
    def __init__(self): 
        self.__figuras = [] 
 
    def addRectangulo(self, base, altura): 
        rect = rectangulo(base, altura)
        rect.info()
        self.__figuras.append(rect) 
 
    def addTriangulo(self, base, altura):
        tri = triangulo_rectangulo(base, altura)
        tri.info()
        self.__figuras.append(tri)
        
    def addHexagono(self, b, h):
        hexa = hexagono(b, h)
        hexa.info()
        self.__figuras.append(hexa)
    
    def ingresarDatos(self, tipo_figura):
        try:
            b = float(input(f"Ingrese la base del {tipo_figura}: ")) 
            h = float(input(f"Ingrese la altura del {tipo_figura}: "))
            if b <= 0 or h <= 0:
                print("La base y la altura deben ser mayores que cero.")
                return None
            return [b, h]
        except ValueError:
            print("Error en el ingreso. Intente de nuevo.....")
            return None
    
    def mostrarFiguras(self):
        if not self.__figuras:
            print("No hay figuras añadidas previamente")
            return
        for i, f in enumerate(self.__figuras):
            print(f"\nFigura #{i + 1}")
            f.info() 
            print('%' * 40)
    
    def menu(self):
        while True: 
            print("\nMenu de Figuras:") 
            print("1. Añadir Rectangulo") 
            print("2. Añadir Triangulo Rectangulo") 
            print("3. Añadir Hexagono") 
            print("4. Mostrar todas las Figuras")
            print("5. Salir")
            op = input("Seleccione una opción:  -> ") 
            
            if op == "1": 
                datos = self.ingresarDatos("rectangulo")
                if not datos:
                    continue
                self.addRectangulo(datos[0], datos[1])
            elif op == "2": 
                datos = self.ingresarDatos("triangulo_rectangulo")
                if not datos:
                    continue
                self.addTriangulo(datos[0], datos[1]) 
            elif op == "3": 
                datos = self.ingresarDatos("hexagono")
                if not datos:
                    continue
                self.addHexagono(datos[0], datos[1]) 
            elif op == "4": 
                self.mostrarFiguras() 
            elif op == "5": 
                print("Saliendo del programa.....") 
                break 
            else: 
                print("Opción inválida. Intente de nuevo.....") 

if __name__ == "__main__": 
    menu = menu_figura() 
    menu.menu()
