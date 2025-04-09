import datetime
dados = dict()
for n in range(4):
    dados['Nome'] = str(input('Qual o nome: '))
    Ano = int(input('Digite o ano de nascimento: '))
    dados['idade'] = datetime.datetime.now().year - Ano
    dados['ctps'] = int(input('Digite o numero ou [0] para [NÃO]: '))

    if dados['ctps'] != 0:
        dados['contratacao'] = int(input('Digite o ano de contratação: '))
        dados['salario'] = float(input('Digite o salario R$: '))
        dados['aposentadoria'] = dados['contratacao'] + 35 - dados['idade'] + datetime.datetime.now().year

for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
