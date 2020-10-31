Algoritmo  prog3
	Definir contador,acumulador, x, z, w, limite Como Entero
	contador<-0
	acumulador<-0
	x<-1
	z<-0
	w<-0
	limite<-10 
	Mientras  x <= limite Hacer
		contador<-contador +1
		si contador mod 3 = 0 Entonces
			z = z + contador
		SiNo
			si contador mod 5 = 0 Entonces
				w <- w + 1
			FinSi
		FinSi
		acumulador=acumulador + x
		x=x+1
	FinMientras
	Escribir "contador al final del proceso :", contador
	Escribir "acumulador al final del proceso ", acumulador
	Escribir " valor de x : ",x
	Escribir " valor de z : ",z
	Escribir " valor de w : ", w
	
FinAlgoritmo