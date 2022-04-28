from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def sonido(self):
        pass

    def diHola(self):
        print("Hola")

class Perro(Animal):
    def sonido(self):
        print("Gua gua")

class Gato(Animal):
    def sonido(self):
        print("Miau Miau")

p = Perro()
p.sonido()
p.diHola()

g = Gato()
g.sonido()
p.diHola()


