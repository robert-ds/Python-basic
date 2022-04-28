def escribe(fichero,datos):
    f = open(fichero, 'a')

    for linea in datos:
        if not linea.endswith("\n"):
            linea += '\n' \

        f.write(linea)

    f.close()

lista = [
    "una linea",
    "dos lineas",
    "tres lineas"
]

escribe('mifichero2.txt', lista)





