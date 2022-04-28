# En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos: Color, Ruedas, Puertas.

# Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos: Velocidad, Cilindrada.

# por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
    color = ""
    ruedas = 0
    puertas = 0

    def __init__(self):
        print("Esto es un vehiculo")

class Coche(Vehiculo):
    velocidad = 200
    cilindrada = 4

    def __init__(self):
        super().__init__()
        print("De tipo Coche")

c = Coche()
c.color = "Rojo"
c.ruedas = 4
c.puertas = 2
print("De color:",c.color)
print("Ruedas:",c.ruedas)
print("Puertas:",c.puertas)
print("Velocidad:",c.velocidad,"y",c.cilindrada,"Cilindros")


        

