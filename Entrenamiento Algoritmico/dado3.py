'''
PUNTO 4 CHALLENGE1

Script que permita lanzar dos
dados N veces, y finalice ÚNICAMENTE cuando
genere un PAR de SEIS.

    randint: It generates integer (Z) numbers
    uniform: It  generates float (R) numbers
'''
#Call packages or libraries
import os
os.system("cls") # thsi kine let you clear screen.
from random import randint, uniform

num=int(input("No. de lanzamientos : "))
i=1
status=True
while i == num :
    while True:
        dice1=randint(1,6)
        dice2=randint(1,6)
        if dice1 == 6 and dice2 == 6:
            print(dice1," y ", dice2)

        else:
            print(dice1," y ", dice2)
    status=True
    i=i+1