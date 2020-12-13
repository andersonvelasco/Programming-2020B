#Developer: maicolopeza
'''
Script description
Se requiere de un programa que solicite por pantalla los datos de un empleado, al finalizar la solicitud 
de un empleado, debe preguntar si desea ingresar otro, al presionar SI/si continuará solicitando 
la información de un nuevo empleado, y si presiona NO/no, finalizará la solicitud.  
El sistema debe solicitar de cada empleado la siguiente información:
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
os.system ("cls")
a=1
b=0
continuar=0
totalemple=0
genm=0
genf=0
geno=0
conm=0
conf=0
condif=0
edad=0
acumedad=0
promedad=0
acumedadm=0
acumsalariof=0
incrementoa=0
incrementob=0
incrementoc=0
totalcata=0
totalcatb=0
totalcatc=0
#statusg=True
op=0
while op == "1" or a <= 1 or op == "si" or op == "Si" or op== "SI" or op == "sI" or op == "yes" or op == "y" :
  print(".:::::Bienvenido al Sistema:::::.")
  nombre=str(input("Ingrese Nombre del Empleado : "))
#-------------------
  statusg=True
  while statusg:
    genero=str(input("Ingrese Género [M, F, O] : "))
    if genero == "M" or genero == "m":
      conm = conm+1
      statusg = False
    elif genero == "F" or genero == "f":
      conf = conf+1
      statusg = False
    elif genero == "O" or genero == "o":
      condif = condif+1
      statusg = False
    else:
      print("Error,\n Digite Género en formato : \n * Masculino 'M' ó 'm' \n * Femenino 'F' ó 'f' \n * Otro 'O' ó 'o' ")
#------------------------
  statusn=True
  while statusn:
    nacimiento=int(input("Ingrese año de nacimiento : "))
    if nacimiento <=2002 and nacimiento >=1950:
      edad=2020-nacimiento
      if genero == "M" or genero == "m":
        acumedadm=acumedad+edad
    else:
      print("Error, digite nuevamente la edad")
      statusn=True
    statusn=False
#------------------
  salario=float(input("Ingrese Salario : "))
  if genero == "F" or genero == "f":
    acumsalariof=acumsalariof+salario
#--------------------
  statusc=True
  while statusc:
    categoria=str(input("A que categoria pertenece? [A, B, C] : "))
    if categoria == "A" or categoria == "a":
      incrementoa=salario*0.1
      totalcata=totalcata+incrementoa
      statusc=True
    elif categoria == "B" or categoria == "b":
      incrementob=salario*0.1
      totalcatb=totalcatb+incrementob
      statusc=True
    elif categoria == "C" or categoria == "c":
      incrementoc=salario*0.1
      totalcatc=totalcatc+incrementoc
      statusc=True
    else:
      print("Error, Digite de nuevo la Categoria ")
    statusc=False
    op=str(input("Desea Agregar un usuario : \n   1. Si\n   2. No: \n Digite valor : "))
    a=a+1
print("\n.::::::REPORTE::::::.")
if conm==0:
    conm=conm+1
print("Promedio de edad de todos los empleados con género M : ",acumedadm/conm)
if conf==0:
    conf=conf+1
print("Promedio de salario de empleados con género F : ", acumsalariof/conf)







