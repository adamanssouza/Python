soma = 0
cont = 0
for i in range(6):  # Loop para ler 6 números
    n = int(input('Digite um número: '))
    if n % 2 == 0:  # Verifica se o número é par
        soma += n  # Adiciona o número à soma se for par
        cont += 1

print(f'A soma de {cont} números pares é a soma é: {soma}')
    