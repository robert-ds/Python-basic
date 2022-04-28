#En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

def main():
    f = open('archivo.txt', 'a')

    frutas = [
        "naranja",
        "patilla",
        "melón",
        "fresa"
    ]

    f.write("Lista de Frutas\n")

    for linea in frutas:
        if not linea.endswith("\n"):
            linea += "\n"
        f.write(linea)

    f.close()

if __name__ == "__main__":
    main()
