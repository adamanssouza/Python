from datetime import datetime

ano_atual = datetime.now().year

maiores = 0
menores = 0

for i in range(1,8):
    ano = int(input('Digite  o ano a {}° pessoa nasceu: '.format(i)))
    idade = ano_atual - ano
    if idade < 18:
        menores +=1
    else:
        maiores +=1

print('{} Participantes não atingiram a maior idade'.format(menores))

print('{} Os participantes sao maiores de 18 anos'.format(maiores))
    



