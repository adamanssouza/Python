valores = list()
for c in range(0,5):
    valores.append(int(input(f'Digite o valor para a posiçao {c}:  ')))

maior = max(valores)
menor = min(valores)

print(valores)
print(f'O maior valor é {maior} e aposição {c}')
print(f'O maior valor é {menor} e aposição {c}')

print('=-='*20)

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um numero para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]

print('-=-' * 20)
print(listanum)
print(f'O maior valor digitado foi {mai} nas posições', end=' ')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}...', end=' ')
print('\n' + '-=-' * 20)
print(f'O menor valor digitado foi {men} nas posições', end=' ')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end=' ')
print('\n' + '-=-' * 20)
