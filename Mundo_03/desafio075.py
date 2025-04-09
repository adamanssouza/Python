num = ( int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')),
        int(input('Digite um numero: ')))

print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 esta na {num.index(3)}° posição ')
else:
    print('O valor 3 não foi digitado em nenhuma posição!')
for n in num:
    if n  %2 ==0:
        print(f'O numero {n} e par ')
