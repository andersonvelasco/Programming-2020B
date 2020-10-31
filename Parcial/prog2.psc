Algoritmo abc
	Definir a,b,c Como Entero
	a<-5
	b<-7
	c<-10
	si a>b Entonces
		a<-b-3
		b<-a+2
		c<-103
		Escribir "valor de c en if 1: ",c
	SiNo
		si a< b Entonces
			a<-b-1
			b<-a+1
			c<-a
			Escribir "valor de c en if 2: ",c
		SiNo
			b<-b-1
			b<-a*3.1416
			c<-b
			Escribir "valor de c en if 3",c
		FinSi
	FinSi
	Escribir "valor de c al finalizar",c
FinAlgoritmo
