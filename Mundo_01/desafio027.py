import random

numero = random.randint(0,5)
numero1 = int(input('Digite um numero entre 0 e 5? '))
if numero1 == numero:
    print('O usuario acertou!')
else:
    print('O usuario errou!')

