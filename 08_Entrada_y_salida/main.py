class Juguete:

    nombre = ""
    precio = 0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f'El nombre del juguete es {self.nombre} y el precio es {self.precio}'

j1 = Juguete("Potato", 10.5)
j2 = Juguete("Dino", 4.2)

print(j1)
print(j2)

cadena = "En algun lugar de la manchA"
num = "10"
print(num.isdigit())
print(cadena.count('A'))
print(cadena.split())