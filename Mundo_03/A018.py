# Lista para armazenar as informações de todas as pessoas
galera = list()

# Variáveis para contar o número de maiores e menores de idade
totmai = totmen = 0

# Laço que irá pedir dados de 3 pessoas (nome e idade)
for c in range(0, 3):
    # Criando uma lista vazia para armazenar os dados de cada pessoa
    dado = []  
    
    # Solicita o nome da pessoa e armazena na lista 'dado'
    dado.append(str(input('Nome: ')))
    
    # Solicita a idade da pessoa e armazena na lista 'dado'
    dado.append(int(input('Idade: ')))
    
    # Adiciona a lista 'dado' (contendo o nome e idade) na lista 'galera'
    galera.append(dado)

# Laço para percorrer a lista 'galera' e classificar cada pessoa
for p in galera:
    # Verifica se a pessoa é maior de idade (idade >= 21)
    if p[1] >= 18:
        # Imprime o nome e que a pessoa é maior de idade
        print(f'{p[0]} é maior de idade.')
        
        # Incrementa o contador de maiores de idade
        totmai += 1
    else:
        # Imprime o nome e que a pessoa é menor de idade
        print(f'{p[0]} é menor de idade.')
        
        # Incrementa o contador de menores de idade
        totmen += 1

# Imprime o número total de maiores e menores de idade
print(f'Temos \033[32m {totmai} maiores e {totmen} menores\033[m de idade.')
