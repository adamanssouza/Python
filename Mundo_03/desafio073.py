camp = ('Botafogo', 'Palmeiras', 'Fluminense', 'Grêmio',
         'Flamengo', 'São Paulo', 'Atlético Mineiro', 
         'Internacional', 'Corinthians', 'Atlético Goianiense',
         'Santos', 'Ceará', 'Bragantino',
         'Vasco', 'Cruzeiro', 'Bahia', 'Fortaleza', 'Coritiba', 
         'Goiás', 'Avaí'
)

# Mostrando os 5 primeiros times
print(f'Os 5 primeiros são: {camp[0:5]}')

# Mostrando os 4 últimos times
print(f'Os 5 últimos são: {camp[-5:]}')

# Convertendo a tupla em uma lista e ordenando
lista_camp = list(camp)
lista_camp.sort()
print(f'Times em ordem alfabética: {", ".join(lista_camp)}')

# Encontrando a posição do Internacional
posicao_internacional = lista_camp.index('Internacional') + 1  # +1 para ajustar a posição (1-20)
print(f'A posição do Internacional é: {posicao_internacional}°')

# Mostrando a quantidade de times
print(f'Total de times: {len(camp)}')

for pos, camp in enumerate(camp):
    print(f'{pos}-{camp}')