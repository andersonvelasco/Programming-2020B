#Developer: AndersonVelasco
'''
Script description:
Se requiere de un programa que solicite por pantalla el número [N] de empleados de la compañía.  El sistema debe solicitar de cada empleado la siguiente información:
Entradas:
•	Nombres y apellidos
•	Genero [M, F, O]
•	Año de nacimiento [AAAA]
•	Salario
•	Categoría fondo de empleados [A, B, C]
Identifique los procesos a realizar que permitan obtener el siguiente reporte al área contable:
•	Total de empleados registrados
•	Total de empleados con género M
•	Total de empleados con género F
•	Total de empleados con genero O
•	Promedio de edad de todos los empleados
•	Promedio de salario de empleados con género F
•	Valor total por concepto de salario a pagar
•	Total incrementos
Tenga en cuenta las siguientes validaciones:
•	El año de nacimiento no puede ser superior a 2002 ni inferior a 1950
•	El género únicamente podrá ser M, F u O
•	La categoría únicamente podrá ser A, B o C
•	Si la categoría es A, tendrá un incremento al salario del 10%
•	Si la categoría es B, tendrá un incremento al salario del 7%
•	Si la categoría es A, tendrá un incremento al salario del 4%
'''
import os
os.system("cls") # thsi kine let you clear screen.
print(":::::Bienvenido al Sistema::::::")
nume=int(input("Ingrese el No. de Empleados : "))#Solicita el No. de empleados para solicitar información
i=1#contador fin ciclo while
acumedad=0
#---Contadores Genero
conm=0
conf=0
condif=0
#--- Contadores Categoria
concat=0
concatb=0
concatc=0
#---acumulador Edad
acumedad=0
#--- acumulador salario f
acumsalf=0
acumsalm=0
#--- Inicio Proceso
while i<=nume:
    print(":::::Datos Empleado:::::::No. ", i)
    #--------- validación Genero --------------- 
    status= True
    nombre=str(input("Digite su nombre : "))
    while status:
        genero=str(input("Genero [M/m, F/f, O/o] : "))
        if genero == "M" or genero == "m":
            conm=conm+1
            status=False
        elif genero == "F" or genero == "f":
            conf=conf+1
            status= False
        elif genero == "O" or genero == "o":
            condif=condif+1
            status = False
    statusn=True
    #-------------- validación Nacimiento ----------------
    while statusn:
        nacimiento=int(input("Año de nacimiento : "))
        if nacimiento >=1950 and nacimiento <= 2002:
            edad=2020 - nacimiento
            acumedad=acumedad+edad
            statusn=False
    #-------- Suma de Salarios
    salario=int(input("Salario : "))
    if genero == "F" or genero =="f":
        acumsalf=acumsalf+salario
    else:
        acumsalm=acumsalm+salario
    #--------------- validacion Categoria----------------
    statuscat=True
    while statuscat:
        categoria=str(input("Categoría fondo de empleados [A, B, C] : "))
        if categoria == "A" or categoria == "a":
            incsala=salario*0.1
            totalsala=salario+incsala
            concat=concat+1
            statuscat=False
        elif categoria == "B" or categoria == "b":
            incsalb=salario*0.07
            totalsalb=salario+incsalb
            concatb=concatb+1
            statuscat= False
        elif categoria == "C" or categoria == "c":
            incsalc=salario*0.04
            totalsalc=salario+incsalc
            concatc=concatc+1
            statuscat = False
    i+=1
print(":::::::::::Reporte:::::::::")
print("Total de empleados registrados : ", nume)
print("Total de empleados Genero : M : ",conm)
print("Total de empleados Genero : F : ",conf)
print("Total de empleados Genero : O : ",condif)
print("Promedio de Edad entre los empleados es: ", acumedad/nume)
if acumf == 0:
    acumf=acumf+1
print("Promedio de salario de empleados con género F", acumsalf/acumf)
print("Valor total por concepto de salario a pagar",acumsalf+acumsalm)
print("Total Incrementos")
