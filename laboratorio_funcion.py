from logging import exception
from msilib import type_string
from re import X


def enteros(promt,num_min, num_max):
    try:
        num1 = int(input("Introduzca un número entero: "))
       #num2 = int(input("Introduzca un número entero: "))
        #num3 = int(input("Introduzca un número entero: "))
        #return (num_min)
        return (num1)
    except type_string:
        print("Error en el ingreso ")
    print("Ingreso exitoso")


