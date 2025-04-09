from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print(''' SUAS OPÇÕES :
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input("Digite sua jogada ! "))
print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PO!!!')
print('---==='*11)
print('Computador jogou {}'.format(itens[computador]))
print('Você jogou {}'.format(itens[jogador]))
print('---==='*11)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Você venceu!')
    elif jogador == 2:
        print('O computador venceu ')
    else:
        print('JOGADA INVALIDA')
elif  computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Você venceu!')
    elif jogador == 0:
        print('O computador venceu ')
    else:
        print('JOGADA INVALIDA') 
elif computador == 2:
    if jogador == 2:
        print('EMPATE')
    elif jogador == 0:
        print('Você venceu!')
    elif jogador == 1:
        print('O computador venceu ')
    else:
        print('JOGADA INVALIDA')
   

