from random import randint

v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ''
    tipo = str(input('Par ou Ímpar? (P/I): ')).strip().upper()
    while tipo not in 'PI':
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.', end=' ')
    print('Deu par' if total % 2 == 0 else 'Deu ímpar')
    
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    
    print('Vamos jogar novamente...')
    
print(f'GAME OVER! Você venceu {v} vezes.')

  
        
