'''
PUNTO 2 Y 3 CHALLENGE1
Script que lanza un dado el número de veces digitado por el usuario
y muestra la suma de los lanzamientos
Glossary:
    randint: It generates integer (Z) numbers
    uniform: It  generates float (R) numbers
'''
#Call packages or libraries
import os
os.system("cls") # thsi kine let you clear screen.

from random import randint, uniform

'''
z=randint(1,6) #Rango (star,end)
r=uniform(1,6)
print("Integer number is: ", z)
print("Integer number is: ", r)
'''
num=int(input("No. de lanzamientos : "))
i=1
suma=0
while i<=num:
    dado=randint(1,6) #Rango (star,end)
    suma=suma+dado
    print ("lanzamientos : ",dado)
    i+=1
print("la suma de los lanzamientos es ",suma)