#Packages
import os 
os.system("cls")
lista=[]
#Functions
def llenar_lista(x):
    lista.append(x)

#def validacion_lista():
#    print("Validación :")

#def mostrar_lista():
#    print("Mostrar")

#Main
num=int(input("Ingrese No: "))
op=int(input("::::Desea Agregar un nuevo Número a la Lista : \n1. Si\n2. No : "))
if op =="s" or  op =="S" or op == "1":
    llenar_lista(num)
else:
    print("opción incorrecta")
#   validacion_lista()
