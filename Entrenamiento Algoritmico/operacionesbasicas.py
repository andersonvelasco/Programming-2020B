'''Script operaciones aritméticas básicas'''

import os
os.system("cls") # this line let you clear screen.

print ("Calculadora Básica")

num1=int(input("Ingrese primer número: "))
num2=int(input("Ingrese segundo número: "))
    
print(":::: Menú ::::")
print ("[1] Sumar")
print ("[2] Restar")
print ("[3] Multiplicar")
print ("[4] Dividir")

while status:
    op = int(input("Digite Operación: "))
    if op >= 1 and op <=4 :
        status = False
    else:
        tried = tried + 1
        print("tried No. ", tried)
        if tried == 3:
            print("")
            key = input("Presione cualquier tecla")
            break
        status = True         
    if op==1:
        print ("[1] SUMA")
        calcular = num1+num2
        print(num1," + ", num2," = ",calcular) 
    elif op==2:
        print ("[2] RESTA")
        calcular=num1-num2
        print(num1," - ", num2," = ",calcular)
    elif op==3:
        print ("[3] Multiplicación")
        calcular=num1*num2
        print(num1," - ", num2," = ",calcular)
    elif op==4:
        print ("[4] División")
        calcular=num1-num2
        print(num1," / ", num2," = ",calcular)
    else :
        print("Operación no encontrada")
print("Fin ejecución")
#-----------------------------------------

'''
print ("Programa para operaciones aritmeticas básicas")
num1=int(input("Ingrese primer número: "))
num2=int(input("Ingrese segundo número: "))
print (":::: Menú ::::")
print ("[1] Sumar")
print ("[2] Restar")
print ("[3] Multiplicar")
print ("[4] Dividir")
op=int(input("Digite operación"))
if op==1:
    print ("[1] SUMA")
    calcular=num1+num2
    print(num1," + ", num2," = ",calcular)
elif op==2:
    print ("[2] RESTA")
    calcular=num1-num2
    print(num1," - ", num2," = ",calcular)
elif op==3:
    print ("[3] Multiplicación")
    calcular=num1*num2
    print(num1," - ", num2," = ",calcular)
elif op==4:
    print ("[4] División")
    calcular=num1-num2
    print(num1," / ", num2," = ",calcular)
else :
    print("Operación no encontrada")
'''