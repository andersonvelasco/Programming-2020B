#inicio del programa
import os
os.system("cls") # thsi kine let you clear screen.
print(":::::Bienvenido al Sistema::::::")
contador=0
acumulador=0
x=1
m3=0
m5=0
limite=1000
while x<= limite:
    contador = contador +1
    if contador % 3 == 0:
        m3=m3+contador
    else:
        if contador % 5 == 0:
            m5=m5 +1
    acumulador = acumulador + x
    x=x+1
print("El valor de m5 es :",m5)
print("El valor del acumulador es : ", acumulador)