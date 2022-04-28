class Juguete:
    _encendido = True

    def __init__(self):
        print("Estoy en la clase Juguete")

    def enciende(self):
        print("El juguete está encendido")
        self._encendido = True

    def apaga(self):
        print("El juguete está apagado")
        self._encendido = False
    
    def isEncendido(self):
        return self._encendido

# clase Potato
class Potato(Juguete):
    color = ""
    nombre = ""

    def __init__(self, nombre):
        super().__init__()
        self.color = "Verde"
        self.nombre = nombre

    def quitarOreja(self):
        pass

    def ponerOreja(self):
        pass

# Clase Dino
class Dino(Juguete):
    def verEscamas(self):
        pass

p = Potato("Vic")
print(p.nombre,p.color)
