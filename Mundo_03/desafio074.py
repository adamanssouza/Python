from random import randint
 
maior = 0
menor = 0

aleatorios = tuple(randint(0, 100) for _ in range(5))

print(f'Os valores selecionado foram:', *aleatorios )

maior = max(aleatorios)
menor = min(aleatorios)

print(f'O maior valor é: {maior} ')
print(f'O menor valor é: {menor}')
