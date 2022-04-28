import pickle

class Juguete:
    nombre = ""
    precio = 0.0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def getNombre(self):
        return self.nombre

"""
Serializa  el objeto potato en un archibo .bin

j1 = Juguete("Potato", 10.2)
f = open('datos.bin', 'wb')
pickle.dump(j1, f)
f.close()
"""
f = open('datos.bin', 'rb')
potato = pickle.load(f)
f.close()

print(type(potato))
print(potato.getNombre(), "Precio: ", potato.precio)


