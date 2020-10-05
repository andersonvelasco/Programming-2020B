'''Script que compara 2 numeros ingresados por el usuario
y define cual numero es mayor o si son iguales'''

import os
os.system("cls") # thsi kine let you clear screen.

num1=0 #
num2=0 #
print ("Programa para calcular el mayor de dos números o igual ")
num1=int(input("Ingrese primer número:"))
num2=int(input("Ingrese segundo número:"))
'''
EN lenguajes de programacion como java, c++, c#, javascript, php y otros
mas se utiliza las {}
Ejp:
if num1 > num2 { 
    print("El número mayor entre", num1," y ", num2," es: ", num1)
}esle{
    print("El número mayor entre", num1," y ", num2," es: ", num2)
}
'''

if num1 > 0 and num2 > 0 :
    if num1==num2:
        print("Los números son iguales")
    else:
        if num1 > num2 :#":" reemplazan el entonces de pseudocódigo
            print("El número mayor entre", num1," y ", num2," es: ", num1)
        else:
            print("El número mayor entre", num1," y ", num2," es: ", num2)
else:
    print("Los valores deben ser positivos")    