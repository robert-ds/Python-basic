import mipaquete.operaciones

"""
Haciendo uso de los paquetes en python
implementando clases y methodos

"""

def main():
    print(mipaquete.operaciones.suma(2,4))
    mp = mipaquete.operaciones.Multiplicador()

    print(mp.multiplicar(5, 2))

if __name__ == '__main__':
    main()
