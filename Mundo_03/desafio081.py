varios = list()
cont = pos = 0
while True:
    varios.append(int(input('Digite um número: ')))

    cont += 1

    varios.sort(reverse=True)
   

    # Pergunta se o usuário deseja continuar
    continuar = input('Deseja continuar? [S/N]: ').upper().strip()

    # Se o usuário não digitar 's' (minúsculo ou maiúsculo), o loop vai parar
    if continuar.lower() != 's':
        break
print('=-='*20)
if 5 in varios:
    pos=varios.index(5) 
        
else:
    print('O valor 5 não está na lista.')

print(f'O valor 5 está na lista na posiçao {(pos)}.')
print(f'Foram digitados {cont} números.')
print(varios)