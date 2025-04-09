print('{:=^40}'.format("Escolha um produto"))
preco= float(input("Digite o preço das compras: "))
print('''FORMAS DE PAGAMENTO
[1] À vista em dinheiro/cheque (10% de desconto)
[2] À vista no cartão (5% de desconto)
[3] Em até 2x no cartão (sem juros)
[4] 3x ou mais no cartão (20% de juros)''')
opcao  = int(input('Qual e a opção? '))
if opcao == 1:
   total = preco - (preco * 10/100)
elif opcao == 2:
   total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra sera parcelada em 2x de R${}:.2f '.format(parcela))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final' .format(preço,total))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = 0 
    print('OPÇÃO INVALIDA de pagamento. Tente novament!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final;' .format(preco, total))

