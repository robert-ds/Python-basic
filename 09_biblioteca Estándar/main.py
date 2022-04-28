"""
Haciendo uso de la funcion filter

numero = [1,2,3,4,5,6,7,8,]

def miFuncion(x):
    if x % 2 == 0:
        return True

    return False


resultado = filter(miFuncion, numero)
print(list(resultado))
"""

"""
Implemantacion de la funcion map
def cuadrado(x):
    return x * x

resultado = map(cuadrado, [1,2,3,4,5,6,7,8,9,10])
# resultado = map(lambda x: x * x, [1,2,3,4,5,6,7,8,9,10])
print(list(resultado))
"""

"""
Uso de la funcion reduce
from functools import reduce

def suma(a, b):
    print(f'a:{a} b:{b}')
    return a + b

res = reduce(suma,[1,2,3,4,5,6,7,8,9,10])
print(res)
"""

"""
Ejemplo de zip, unir o asociar elementos de una lista
cursos = ["Java","Python","Git"]
asistentes = [14,20,12]

demo = zip(cursos,asistentes)
print(list(demo))
"""

from getpass import getpass

user = input("Username: ")
passwd = getpass("Passwd: ")

print(f'Su nombre de usuario es: {user} y contraseña: {passwd}')


