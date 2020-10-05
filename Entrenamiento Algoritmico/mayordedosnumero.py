'''Script que compara 2 numeros ingresados por el usuario
y define cual numero es mayor'''

import os
os.system("cls") # thsi kine let you clear screen.

num1=0
num2=0
print ("Programa para calcular el mayor de dos números ")
print ("Ingrese primer número: ")
num1=int(input())
print ("Ingrese segundo número: ")
num2=int(input())
if num1 > num2 :
    print("El número mayor entre", num1," y ", num2," es: ", num1)
else:
    print("El número mayor entre", num1," y ", num2," es: ", num2)    