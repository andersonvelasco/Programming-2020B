'''Script que lanza un dado y muestra el resultado y adicionalmente debe mostrar 
si el resultado es par o impar
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
dado=randint(1,6) #Rango (star,end)
if dado % 2 == 0:
    print("El dado ha caido en: ", dado, " y es par")
else:
    print("El dado ha caido en: ", dado, " y es impar")