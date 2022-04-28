# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    nombre = ""
    nota = ""

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

        if nota < 5:
            print("El estudiante", nombre,"obtuvo una nota de:", nota, ",por tanto no a pasado")
        else:
            print("El estudiante", nombre,"obtuvo una nota de:", nota, ",por tanto ha pasado")

e = Alumno("Juan", 4)

e1 = Alumno("Carlos", 9)

