msg='Ola, Mundo!'
cores = {'limpa':'\033[m', 'azul':'\033[1;34m', 'amarelo':'\033[0;33m', 'verde':'\033[0;32m'}
print('Esta mensagem foi reformulada pela aula 011, as cores do texto {}{}{}!!!'.format(cores['amarelo'],msg, cores['limpa']))
print('As cores de {}{}{} estão lindas!!!'.format(cores['verde'], msg, cores['limpa']))