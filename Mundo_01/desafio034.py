print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1 = float(input('Digite a primeira segmento: '))
r2 = float(input('Digite a segunda segmento: '))
r3 = float(input('Digite a terceira segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('O segmento acima pode formar um triangulo! ')
else:
    print('Essa formula nao pode formar um triangulo! ')



