'''programa que pregunte el nombre del usuario en la consola 
y un número entero e imprima por pantalla en líneas distintas
el nombre del usuario tantas veces como el número introducido.'''

import os
os.system("cls") # thsi kine let you clear screen.

nombre=input("Cual es tu nombre: ")
print(nombre.upper()+" tiene " + str(len(nombre))+" letras")
