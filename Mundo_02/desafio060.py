try:
    from math import factorial
    while True:
        n = int(input('Digite um numero: '))
        if n < 0:
            print('Fatorial nao e defiinidos para numeros negativos')
        else:
            print(f'O fatorial de {n} e {factorial(n)}')

except ValueError:
    print('Por favor, digite um número inteiro válido.')