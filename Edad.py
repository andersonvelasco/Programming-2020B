#Script:sumas
'''
Teniendo en cuenta el año actual, solicite a un usuario
por consola: el nombre y el año de nacimiento, y le muestre por pantalla un mensaje
indicando el nombre ingresado y la edad actual
'''
#INPUTS
print("Digite el nombre y el año para determinar su edad actual")
print("Ingrese su nombre: ")
nombre=str(input())
print("Digite el año de nacimiento")
year_nacimiento=int(input())
year=2020

#PROCESS
edad_actual=year-year_nacimiento
#OUTPUTS
print (nombre, "tiene ",edad_actual)
