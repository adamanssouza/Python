distancia = float(input('Qual a distancia da sua viagem? '))
if distancia <= 200:
    soma = distancia * 0.50
else:
    soma = distancia * 0.45
print('O valor da sua passagem e {:.2f} reais'.format(soma))