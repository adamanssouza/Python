print('---'*20)
print('Lista de compras')
print('---'*20)

produtos = []  # Lista para armazenar os produtos
preços = []  # Lista para armazenar os preços

# Recebendo produtos e preços
while True:
    produto = input('Digite o produto (ou "sair" para terminar): ')
    if produto.lower() == 'sair':
        break
    preço = float(input(f'Digite o valor do produto "{produto}": '))
    produtos.append(produto)
    preços.append(preço)

# Exibindo a lista de compras
for pos in range(len(produtos)):
    print(f'{produtos[pos]:.<30} R$ {preços[pos]:>7.2f}')
    
print('--'*20)
