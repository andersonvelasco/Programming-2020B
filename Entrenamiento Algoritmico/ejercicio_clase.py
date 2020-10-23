'''Validaciones:
1. X
2. X
'''
import os
os.system("clear")

print(":::lista de numeros::: ")
n1=int(input("Ingrese un numero : "))
print("\n ::: LISTA GENERADA ::: ")
i=1
b=0
while i <= n1 :
    print(i)
    i=i%2
    b=b+i
    if i==0:
        print("el numero de pares fueron:", b )
    else:
        print("el numero de impares es ",b)
i+=1 # i = i + 1

print("\n::: REPORTE :::")  
print("La cantidad de números generados es: ", n1)
#print("La cantidad de números generados es: ", i-1)

