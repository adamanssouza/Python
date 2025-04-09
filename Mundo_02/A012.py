nome = str(input('Qual é seu nome? '))
if nome == 'Adamans':
    print('Que nome bonito!')
elif nome == 'Pedro' or 'Joao' or 'Maria' or  nome == ' Paulo':
    print( 'Seu nome e bem popular no brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Belo nome Feminino!')
else:
    print('Seu nome e bem normal.')
print('Tenha um bom dia, {}'.format(nome))
