from datetime import date
ano = int(input('Digite o ano? Coloque 0 para analisar o ano atual ! '))
if ano ==0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Este ano {} e bissexto! '.format(ano))
else:
    print('O ano {} Não é bissexto!'.format(ano))