'''Script que determina si un numero ingresado por el usuario es primo o compuesto
Teoria:
    Que es un número primo:
    SOn aquellos no. enteros divisibles unicamente entre 1 y por si mismo. Solo 2 divisores

'''
#Call packages or libraries
import os
os.system("cls") # thsi kine let you clear screen.
counter = 0
i = 1
print(":::VERIFICADOR DE NÚMEROS PRIMOS::::")
num=int(input("Ingrese un número: "))
while i <= num :
    if num % i ==0:
        counter = counter +1
    i = i + 1
if counter <= 2:#counter < 3
    print("El No. ",i-1," es PRIMO")
else:
    print("El No. ",i-1," es COMPUESTO") 