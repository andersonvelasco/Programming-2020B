'''Script operaciones aritméticas básicas'''

import os
os.system("cls") # thsi kine let you clear screen.

print ("Programa para operaciones aritmeticas básicas")
print ("[1] Sumar")
print ("[2] Restar")
print ("[3] Multiplicar")
print ("[4] Dividir")
op=int(input("Seleccione la operación : "))
num1=int(input("Ingrese primer número: "))
num2=int(input("Ingrese segundo número: "))

if op == 1 or op <= 5 and op >=0: 
    print(num1," + ", num2," = ",num1+num2)
    if op == 2:
        print(num1," - ", num2," = ",num1-num2)
        if op == 3:
            print(num1," X ", num2," = ",num1*num2)
            if op == 4:
                print(num1," / ", num2," = ",num1/num2)              
else :
    print("No selecciono la operación valida para operar los numeros")