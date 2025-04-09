numeros = ('zero', 'um','dois','três', 'quatro', 'cinco',
           'seis', 'sete','oito','nove', 'dez',  'onze',
           'doze','treze','quatorze','quinze','dezesseis',
           'dezessete', 'dezoito','dezenove','vinte'
)

while True:
    n = int(input('Digite um numero [0 a 20]: '))
    
    if 0 <= n <= 20:
        print(f'O numero digitado foi {numeros[n]}')
    else:
        print('Número inválido. Por favor, digite um número entre 0 e 20.')

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar != 'S':
        break
