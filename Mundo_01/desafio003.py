cores = {'limpa':'\33[m','branco':'\033[4;30;41m','vermelho':'\033[1;31m','verde':'\033[0;32m','roxo':'\033[0;35m','azul':'\033[0;36m'}
valor = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
soma = valor + valor2
print(f'A soma entre {valor} e {valor2} é igual a {soma}!')
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}'
      . format(cores['vermelho'],valor , cores['limpa'],
               cores['verde'],valor2,cores['limpa'], cores['roxo'],soma, cores ['limpa'],))
n = bool(input('Digite um valor'))
print(n)
