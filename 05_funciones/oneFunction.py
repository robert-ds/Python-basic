def saluda():
    print("Hola como a todo")

saluda()

def suma(*args):
    resultado = 0

    for arg in args:
        resultado += arg

    print(resultado)

suma(3, 2, 2,3)

def operaciones(a, b):
    return a + b, a - b, a * b, a /  b

suma, resta, multiplicacion, divicion = operaciones(2, 4)

print(suma)
print(resta)
print(multiplicacion)

anonime = lambda: print("Hola Lambda")
anonime()

sumatoria = lambda x: x + x
print(sumatoria(4))
