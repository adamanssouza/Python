velocidade  = float(input('Digite a velocidade!: '))
if velocidade > 80:
    print("""Você foi multado! 
          A multa vai custar R$ 7,00 por cada Km
          acima do limite.""")
    multa = (velocidade - 80) * 7
    print('O valor da multa {:.2f} Reais.'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')