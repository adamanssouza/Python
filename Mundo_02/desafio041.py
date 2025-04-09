from datetime import datetime
# Solicita o ano de nascimento
ano = int(input('Digite o ano de nascimento: '))
# Obtém o ano atual
ano_atual = datetime.now().year
# Calcula a idade
idade = ano_atual - ano
# Determina a categoria com base na idade
if idade <= 9:
    print(f'Você tem {idade} anos, sua categoria é Mirim.')
elif idade <= 14:
    print(f'Você tem {idade} anos, sua categoria é Infantil.')
elif idade <= 19:
    print(f'Você tem {idade} anos, sua categoria é Junior.')
elif idade <= 25:
    print(f'Você tem {idade} anos, sua categoria é Senior.')
else:
    print(f'Você tem {idade} anos, sua categoria é Master.' )
