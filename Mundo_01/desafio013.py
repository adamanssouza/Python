cores = {'limpa':'\033[m', 'azul':'\033[0;34m'}
n1 =float(input('Digite o salario: '))
s = n1 + (n1 * 0.15)
print('O salario com adicional de 15% a mais ficou {}{}{}'.format( cores['azul'], s, cores['limpa']))
