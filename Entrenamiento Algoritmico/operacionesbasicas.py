'''Script operaciones aritméticas básicas'''

import os
os.system("cls") # thsi kine let you clear screen.

print ("Programa para operaciones aritmeticas básicas")
print ("[1] Sumar")
print ("[2] Restar")
print ("[3] Multiplicar")
print ("[4] Dividir")
op=int(input("Seleccione la operación : "))
if op==1:
    print ("[1] SUMA")
    num1=int(input("Ingrese primer número: "))
    num2=int(input("Ingrese segundo número: "))
    print(num1," + ", num2," = ",num1+num2)
elif op==2:
    print ("[2] RESTA")
    num1=int(input("Ingrese primer número: "))
    num2=int(input("Ingrese segundo número: "))
    print(num1," - ", num2," = ",num1-num2)
elif op==3:
    print ("[3] Multiplicación")
    num1=int(input("Ingrese primer número: "))
    num2=int(input("Ingrese segundo número: "))
    print(num1," X ", num2," = ",num1*num2)
elif op==4:
    print ("[4] División")
    num1=int(input("Ingrese primer número: "))
    num2=int(input("Ingrese segundo número: "))
    print(num1," / ", num2," = ",num1/num2)
       
else :
    print("Operación no encontrada")
    