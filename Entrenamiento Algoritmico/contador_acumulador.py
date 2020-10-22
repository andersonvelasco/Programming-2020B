'''
Crear un script en Python que a través de un bucle While permita 
generar lista de una determinada lista de números de acuerdo un valor ingresado por el usuario
. (La lista debe generarse a partir de uno).

Procesos:
1. Listar los números
2. Cuántos números generó en total
3. Cuántos números fueron pares
4. Cuántos números fueron impares
5. Suma total de los pares
6. Suma total de los impares
7. Suma total de todos los números

'''
import os
os.system("cls")
num=int(input("Ingrese No. : "))
i=1
contp=1
conti=1
acump=0
acumi=0
acumt=0
while i<=num :#i<11
    #multiplicacion=tabla*i
    acumt=acumt+i
    if i % 2 ==0:
        print("El No. listado es : ",i," y es par")
        contp=contp+1
        acump=acump+i
    else:
        print("El No. listado es : ",i," y es impar")
        conti=conti+1
        acumi=acumi+i
    i=i+1
print("La cantidad de números generados es: ", num)
print("La cantidad de números generados es: ", i - 1)
print("La cantidad de números pares es : ", contp - 1)
print("La cantidad de números impares es : ", conti - 1)
print("La suma de los no. pares es: ",acump)
print("La suma de los no. pares es: ",acumi)
print("La suma de todos los números es : ",acumt)

