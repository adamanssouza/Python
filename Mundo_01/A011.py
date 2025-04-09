print('\033[1;31;43m Ola, Mundo\033[m')
print('\033[0;30;41m Ola, Mundo\033[m')
print('\033[7;30m Ola, Mundo\033[m')
print('-='*20)
nome = 'Adamans'
print('Ola, {}{}{}, prazer em te conhecer '.format('\033[4;32m', nome, '\033[m'))
print('\033[1;31m-='*20,'\033[m')
a = 3
b = 5
print('Os valores são \033[32m {}\033[m e \033[31m {}\033[m!!!'.format(a, b))

nome = 'Fabyana'
cores = {'limpa':'\033[m', 'azul': '\033[34m', ' vermelho': '\033[31m'}
print(' Este teste da {}{}{} e para ser top !!!'.format(cores['azul'], nome, cores['limpa']))