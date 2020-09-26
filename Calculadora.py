#Script:sumas
'''
Programa que, dadas dos variables N1 = 5 y N2 = 6, permita realizar
las operaciones aritméticas básicas (suma, resta, multiplicación, división) y visualice
por pantalla el resultado de estas 4 operaciones.
'''
#INPUTS
print("Calculadora que permitira obtener los resultados")
print("de las operaciones aritmeticas básicas ")
print("(suma, resta, multiplicación, división)")
print("Ingrese n1: ")
n1=float(input())
print("Ingrese n1: ")
n2=float(input())

#PROCESS
suma=n1+n2
resta=n1+n2
multiplicacion=n1*n2
division=n1/n2
#OUTPUTS
print ("la suma de ",n1,"+",n2,"es: ",suma)
print ("la resta de ",n1,"-",n2,"es: ",resta)
print ("la Multiplicación de ",n1,"x",n2,"es: ",multiplicacion)
print ("la división de ",n1,"/",n2,"es: ",division)
