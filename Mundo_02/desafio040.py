n = float(input('Digite a 1° nota: '))
n2 = float(input('Digite a 2° nota: '))

m = (n + n2) / 2  # Média das notas

if m >= 7:
    print('Parabéns, sua média foi {:.2f}. Você foi APROVADO.'.format(m))
elif 5 <= m <= 6.9:
    print('Sua média foi {:.2f}. Está entre 5 e 6.9, Recuperação.'.format(m))
else:
    print('Sua média foi {:.2f}. Abaixo do esperado que e 5, REPROVADO.'.format(m))
 