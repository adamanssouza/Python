salario = float(input('Digite o salario: '))
if salario > 1250:
    soma = salario + 10/100
    print('O seu salario com o aumento de 10% é {:.2f} Reais'.format(soma))
else:
    s=salario + 15/100
    print('O seu salario com aumento de 15% é {:.2f} Reais'.format(s))