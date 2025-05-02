if __name__ == "__main__":
    class Misuperclase1():
        def metodo_1(self):
            print("metodo_1 metodo llamado")
    class Misuperclase2():
        def metodo_2(self):
            print("metodo_2 metodo llamado")
    class Miclase(Misuperclase1, Misuperclase2):
        def metodo_3(self):
            print("metodo_3 metodo llamado")
c = Miclase()
c.metodo_3()
c.metodo_2()
c.metodo_1()