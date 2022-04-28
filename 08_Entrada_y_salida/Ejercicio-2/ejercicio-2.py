# En este segundo ejercicio, tendréis que crear un archivo py y dentro crearéis una clase Vehículo, haréis un objeto de ella, lo guardaréis en un archivo y luego lo cargamos.
import pickle

class Vehiculo:
    modelo = ""
    marca = ""
    precio = 0.0

    def __init__(self, modelo, marca, precio):
        self.modelo = modelo
        self.marca = marca
        self.precio = precio

    def getModelo(self):
        return self.modelo

    def getMarca(self):
        return self.marca

    def getPrecio(self):
        return self.precio


def guardaObjeto(objeto, archivo):
    f = open(f'{archivo}', 'wb')
    pickle.dump(objeto, f)
    f.close()

def abreObjeto(archivo):
    f = open(f'{archivo}.txt', 'rb')
    vehiculo = pickle.load(f)
    f.close()

    print(f'modelo del vehiculo {vehiculo.modelo}, marcar: {vehiculo.marca} y su precio: {vehiculo.precio}')

v = Vehiculo("Deportivo", "Tesla", 10000)

guardaObjeto(v,'miVehiculo.txt')
abreObjeto("miVehiculo")

