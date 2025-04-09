total = totmil = menor = cont = 0
barato = ''

while True:
    # Informações do consumidor
    produto = input('Nome do produto: ').strip().upper()
    preço = float(input('Preço: '))
    cont += 1
    total += preço

    if preço > 1000:
        totmil += 1

    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar not in 'SN':
        print('Erro! Responda com [S] ou [N].')
        continue
    if continuar == 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O menor preço foi {menor} do produto {barato}')
print(f'O total de produtos foi {cont}')
print(f'Total de produtos acima de 1000: {totmil}')
print(f'A soma dos preços dos produtos é {total}')
