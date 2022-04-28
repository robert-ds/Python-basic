# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.

from functools import reduce

# implementando filter
numeros = [1,2,3,4,5,6,7,8,9,10]
print("lista de números: ", numeros)

# Funcion que se pasa como parametro al metodo filter
def miFuncion(x):
    if x % 2 == 1:
        return True

    return False

# función que se pasa como parametro al metodo reduce
suma(a,b):
    return a + b

# Filtrando lista
resFilter = list(filter(miFuncion, numeros))
print("Lista de número impares filtrados:", resFilter)

# Sumando elementos impares de la lista
resSuma = reduce(suma,resFilter)
print("La suma de los elementos impares es: ", resSuma)



