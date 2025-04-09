import random 
from time import sleep
jogador = {}
maior = menor = 0
for pos in range(4):
    jogo = random.randint(1,6)
    jogador[f'Jogador{pos+1}'] = jogo
    if jogo  > maior:
        maior = jogo 
        maior_jogador = pos + 1
    if jogo < menor or menor ==0:
        menor = jogo 
        menor_jogador = pos + 1

    print('-='*30)
    sleep(1)
    print(f' Jogador {pos+1} saiu  com numero: {jogo}')
print('-=-='*15)

print(f' O jogador {maior_jogador} tirou o maior jogo que foi {maior}')