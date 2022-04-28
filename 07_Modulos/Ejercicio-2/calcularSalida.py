"""
En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, haréis una operación para calcular el tiempo que queda de trabajo.
"""
import time

def main():
    hora_actual = int(time.strftime('%H'))

    if(hora_actual >= 19):
        print("La jornada laboral a concluido")
    else:
        tiempo_restante = 19 - hora_actual
        print("Faltan",tiempo_restante,"horas para concluir la jornada Laboral")

if __name__ == "__main__":
    main() 
