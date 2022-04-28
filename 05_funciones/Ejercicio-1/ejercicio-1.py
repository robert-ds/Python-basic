#Escribe una función que calcule el área de un triángulo, recibiendo la altura y la base como parámetros y otra función que calcule el área de un círculo recibiendo el radio del mismo.
import math

def areaTriangulo(altura, base):
	return (base * altura) / 2

print("Area del Triangulo",areaTriangulo(2,4))

def areaCirculo(radio):
    return math.pi * radio**2

print("Area del Circulo", areaCirculo(5))
