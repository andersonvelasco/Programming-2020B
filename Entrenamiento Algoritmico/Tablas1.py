'''Script que determina la tabla de multiplica a partir de ingresar un numero por el usuario
'''
#Call packages or libraries
import os
os.system("cls") # thsi kine let you clear screen.
posli=True
posls=True
poslsma=True
posta=True

print(":::::Tabla de Multiplicar:::::")
while posta:
    tabla = int(input("Ingrese No. : "))
    if tabla > 0:
        posta=False
    else:
        print("Solo admite números positivos")
        print("Digite nuevamente el No. ")

while posli:# posli==true
    li=int(input("Limite inferior: "))
    if li > 0:
        posli=False
    else:
        print("El número debe ser positivo")
        print("Ingrese nuevamente el limite inferior")

while posls:# posli==true
    ls=int(input("Limite superior: "))
    if ls > li:#and ls >= li or ls<=li:
        posls=False
    else:
        print("El número debe ser mayor que el limite inferior")
        print("Ingrese nuevamente el limite superior")

i=li
while i<=ls :#i<11
    #multiplicacion=tabla*i
    print(tabla," X ",i," = ",tabla*i)
    i=i+1

'''
limite superior y limite inferior
'''