
#guanabara
num = [[],[]]
valor=0
for c in range(1,8):
    valor = int(input(f'Digite {c}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-=-'*10)
num[0].sort()
num[1].sort()
print(f'Os numeros pares são: {num[0]}')
print(f'Os numeros impares são: {num[1]}')

#gpt
numeros = list()
par =list()
impar= list()
contador = 1
pares= impares=0
for n in range(7):
    valor = int(input(f'Digite o {contador}° valor: '))
    numeros.append(valor)
    contador +=1


    if valor % 2 == 0:
        par.append(valor)
        pares +=1
    else:
        impar.append(valor)
        impares +=1



print(f'Os numeros digitados foram {numeros}')      
print(f'Os numero par são:  {par} um total de {pares} numeros pares  ')
print(f'Os numeros impares são {impar} um total de {impares} numeros impares')

