valor = float(input('Qual o valor da casa R$? '))
salario = float(input('Qual a sua base salarial? '))
anos = int(input('Quantas anos quer pagar? '))
meses = anos * 12
casa = valor/meses  
if casa < salario * 0.30:
    print('Seu imprestimo foi aprovado')
    print('O valor a ser pago {:.2f}'.format(casa))
else:
    print('Seu imprestimo foi negado! ')
