fruits=['Banana','Apple','orange']
print('fruits', fruits)
print('len: tamaño ', len(fruits))

otra_fruta = input('Ingrese Fruta : ')
fruits.append(otra_fruta)
otra_fruta = input('Ingrese otra Fruta : ')
fruits.append(otra_fruta)

print("\n")
print('fruits: ',fruits)
print('len: Tamaño ',len(fruits))
'''
print('\nFruit 1:',fruits[0])
print('Fruit 2:',fruits[1])
print('Fruit 3:',fruits[2])
print('Fruit 4:',fruits[3])
'''
i=0
while i < len(fruits) :
    print(print('Fruit ',i+1," : ", fruits[i]))
    i=i+1