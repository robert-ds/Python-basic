def main():
    usuarios = listarUsuarios()

    for usuario in usuarios:
        print(f'Usuario: {usuario}')

def listarUsuarios():
    f = open('/etc/passwd', 'r')
    datos = f.readlines()
    f.close()

    resultado = []
    for lines in datos:
        if lines[0] == '#':
            continue

        if lines[0] == '_':
            continue

        partes = lines.split(':')
        resultado.append(partes[0])

    return resultado

if(__name__ == "__main__"):
    main()