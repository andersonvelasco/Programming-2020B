#Script:Temperatura
'''
programa que permita recibir por consola el valor de la temperatura
en grados centígrados, debe convertir este valor a grados Kelvin, y finalmente,
visualizar el resultado por pantalla. Considere la siguiente fórmula: °K = °C + 273.15.
'''
#INPUTS
print("Programa para convertir grados Centigrados °C a Kelvin °K")
print("Digite el valor en grados °C")
gradosC=float(input())
#PROCESS
conversor=gradosC+273,15
#OUTPUTS
print (gradosC, "°C equivale a",conversor,"°K")
