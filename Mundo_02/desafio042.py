print('-='*20)
print('Analisador de triângulos')
print('-='*20)

# Entrada dos segmentos
r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))

# Verificação de possibilidade de formar um triângulo
if r1 <= r2 + r3 and r2 <= r1 + r3 and r3 <= r1 + r2:
    # Classificação do triângulo
    if r1 == r2 == r3:
        print(f'O seu triângulo tem todos os lados iguais: {r1}, {r2}, {r3} formando um EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print(f'O seu triângulo tem dois lados iguais: {r1}, {r2}, {r3} formando um ISÓCELES')
    else: #elif r1 != r2 != r3 != r1: isoceles 
        print(f'O seu triângulo tem todos os lados diferentes: {r1}, {r2}, {r3} formando um ESCALENO')
else:
    print(f'Esses segmentos {r1}, {r2}, {r3} não podem formar um triângulo!')


