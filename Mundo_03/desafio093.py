time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador? '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(tot):
        while True:
            partidas.append = input(f'Quantos gols fez na {c}ª partida? ').strip()  # Remover espaços
            jogador['gols'] = partidas
            jogador['total'] = sum(partidas)
            time.append(jogador.copy())
            
    while True:
        resp = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resp in 'SN':
            break
        print('Coloque um valor válido [S/N]!')

    if resp == 'N':
        break
print('-='*30)
print('cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print()