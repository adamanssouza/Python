import random
numero = random.randint(0,10)
p = 0
acertou = False
while not acertou:
    numero1 = int(input('Digite um numero entre 0 e 10? '))
    p +=1
    if numero1 == numero:
        acertou  = True
        break
    else:
        if numero > numero1:
          print('Você errou, o numero e maior, tente novamente! ')
        elif numero < numero1:
          print('Voce errou,  o numero e menor, tente novamente! ')
print(f'O usuario acertou! com {p} tentativas')
        

    

