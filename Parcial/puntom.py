Script description
Se requiere de un programa que solicite por pantalla los datos de un empleado, al finalizar la solicitud de un empleado, debe preguntar si desea ingresar otro, al presionar SI/si continuará solicitando la información de un nuevo empleado, y si presiona NO/no, finalizará la solicitud.  El sistema debe solicitar de cada empleado la siguiente información:
Entradas:
•	Nombres y apellidos
•	Genero [M, F, O]
•	Año de nacimiento [AAAA]
•	Salario
•	Categoría fondo de empleados [A, B, C]
Identifique los procesos a realizar que permitan obtener el siguiente reporte al área contable:
•	Total de empleados registrados ok
•	Total de empleados con género M ok
•	Total de empleados con género F ok
•	Total de empleados con genero O ok
•	Promedio de edad de todos los empleados con género M
•	Promedio de salario de empleados con género F
•	Valor total por concepto de salario a pagar
•	Total incrementos por cada categoría
Tenga en cuenta las siguientes validaciones:
•	El año de nacimiento no puede ser superior a 2002 ni inferior a 1950
•	El género únicamente podrá ser M, F u O
•	La categoría únicamente podrá ser A, B o C
•	Si la categoría es A, tendrá un incremento al salario del 10%
•	Si la categoría es B, tendrá un incremento al salario del 7%
•	Si la categoría es A, tendrá un incremento al salario del 4%
'''
import os
os.system ("clear")
a=1
b=0
totalemple=0
genm=0
genf=0
geno=0
contm=0
edad=0
acumedad=0
promedad=0
while a==1:
  print ("Ingrese Datos personales:")
  nombre=input("Nombre y Apellido  ")
  val= True
  while val:
    print ("Ingrese su genero:")
    genero= str (input("M, F, O  "))
    if genero == "M":
      contm=contm+1
      val=False
    elif genero =="F":
      contf=contf+1
      val=False
    elif genero =="O":
      conto=conto+1
      val=False
    else:
      print ("Error, digite la opcion en el formato solicitado")
    valnac=True
  while valnac:  
    print ("Ingrese su año de nacimiento:")
    anonacimiento=int(input("Año de Nacimiento:  "))
    if anonacimiento >= 1950 and anonacimiento <= 2002:
      edad = 2020 - anonacimiento
      acumedad = acumedad+edad
      statusn=False
    else:
      print("Digite el año de nacimiento entre 1050 y 2002")
    print ("Salario:")
    salario=int(input("Ingrese su salario:  "))
    print ("Ingrese categoria de fondo de empleados:")
    catfondoemple=input("A, B, C  ")
    print("Desea ingresar otro usuario:")
    a=int(input("1. SI, 2. NO  "))
    totalemple=totalemple+a
print("El numero total de empleados es:", totalemple-1)
promedad=acumedad/contf
if genero=="m":
  genm=genm+1
else:
  if genero=="f":
    genf=genf+1
  else:
    geno=geno+1
print("Total genero M", genm)
print("Total genero F", genf)
print("Total genero O", geno)
print("Promedio de edad Genero F", promedad)

