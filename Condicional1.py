'''Script que identifica si un
número ingresado por el usuario
es par'''

import os
os.system("cls") # thsi kine let you clear screen.

num=0

print ("Ingrese un número entero: ")
num=int(input())
if num >= 0 :
    if num % 2 == 0 :
        print("El número es PAR")
    else:
        print ("El número es impar")
else :
    print(":::NO SE ACEPTAN VALORES NEGATIVOS")