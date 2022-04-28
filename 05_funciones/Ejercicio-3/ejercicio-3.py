# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def anoBisiesto():
    response = int(input("Digite el Año: "))

    if response % 4 == 0:
        print("El año que ingreso es bisiesto")
    else:
        print("El Año que ingreso no es bisiesto")

anoBisiesto()
