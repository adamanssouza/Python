from random import randint

jogo = int(input('Quantos jogos deseja fazer: '))

for i in range (jogo):
    palpite = list()

    for jogo in range(1,6):
        numero =  randint(1,60)
        palpite.append(numero)
    print(f'Jogo {i+1}: {sorted(palpite)}') 
print('--->> Boa sorte <<-- ')

        
#guanabara 
from random import randint

lista = list()
jogos = list()

print('=' * 10)
print('_____Joga na Mega Sena_____')
quant = int(input('Quantos jogos deseja fazer: '))
tot = 1

while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1  # Corrected the increment operator
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()  # Clear the list to prepare for the next game
    tot += 1

print('---' * 3, f'SORTEANDO {quant} JOGOS', '---' * 3)
for i, l in enumerate(jogos):  # Use 'jogos' instead of 'jogo'
    print(f'Jogo {i + 1}: {l}')


    