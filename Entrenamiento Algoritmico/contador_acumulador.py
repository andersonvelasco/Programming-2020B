'''
Crear un script en Python que a través de un bucle While permita 
generar lista de una determinada lista de números de acuerdo un valor ingresado por el usuario
. (La lista debe generarse a partir de uno).

Procesos:
1. Listar los números
2. Cuántos números generó en total
3. Cuántos números fueron pares
4. Cuántos números fueron impares
5. Suma total de los pares
6. Suma total de los impares
7. Suma total de todos los números
8. Cual es promedio

'''
import os
os.system("cls")
num=int(input("Ingrese No. : "))
print("\n:::::LISTA GENERADA:::::")
i=1
contp=0
conti=0
acump=0 #Acumulador inicializado en 0 para guardar y sumar los no. pares
acumi=0 #Acumulador inicializado en 0 para guardar y sumar los no. impares
acumt=0 #Acumulador inicializado en 0 para guardas la suma de todos los numeros OPCIONAL
while i<=num :# si i es menos o igual a num (No. digitado por el usuario, entonces ingresa al ciclo)
    acumt=acumt+i #inicia el acumulador total a registrar los valores de i -- OPCIONAL
    if i % 2 ==0: #compara si el modulo de i es igual a dos, si cumple, ingresa por verdadero e imprime
        print("El No. listado es : ",i," y es par")
        contp=contp+1 #contador para los numeros pares, incrementa en 1 cada vez que pasa por el ciclo
        acump=acump+i #inicia el acumulador total a registrar los valores de i pares
    else:
        print("El No. listado es : ",i," y es impar")
        conti=conti+1 #contador para los numeros impares, incrementa en 1 cada vez que pasa por el ciclo
        acumi=acumi+i #inicia el acumulador total a registrar los valores de i impares
    i=i+1 #contador encargado de romper el ciclo cuando
print("\n::::::REPORTE::::::")
print("La cantidad de números generados op 1 es: ", num)
#print("La cantidad de números generados op 2 es: ", i - 1)
print("La cantidad de números pares es : ", contp)
print("La cantidad de números impares es : ", conti)
print("La suma de los no. pares es: ",acump)
print("La suma de los no. impares es: ",acumi)
print("La suma de todos los números op 1 es : ",acump+acumi)#== acumt
#print("La suma de todos los números op 2 es : ",acumt)# == acumi+acump -- OPCIONAL
print("El promedio de los numeros generados es : ",acumt/i)

