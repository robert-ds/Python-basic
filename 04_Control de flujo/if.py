a = 2
b = 6

if a < b:
    print("A si es menor que B")
elif b == a:
    print("B es mayor que A")

while a <= b:
    print("Valor de a", a)
    a += 1

valor = 5

match valor:
    case 1:
        print("Valor: ", valor)
        break
    case 2:
        print("Valor: ", valor)
        break
    case 5:
        print("Valor: ", valor)
        break


