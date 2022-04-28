import operaciones as o
import sys
import pprint

def main():
    res = o.suma(2, 2)
    print("Hola desde main",res)
    print(o.como_me_llamo())

    pprint.pprint(sys.path)


if(__name__ == '__main__'):
    main()
