numero = list()
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    numero.append(num)

    continuar = input('Quer continuar? [S/N]: ').upper().strip()

    if continuar != 'S':
        break  # Sai do loop se o usuário não digitar 'S'

# Agora percorre a lista 'numero', que contém todos os números digitados
for v in numero:
    if v % 2 == 0:
        pares.append(v)  # Adiciona os números pares na lista 'pares'
    else:
        impares.append(v)  # Adiciona os números ímpares na lista 'impares'

# Exibe as listas e as contagens de números
print(f'Todos os números digitados: {numero}')
print(f'Os números pares são: {pares} (Quantidade: {len(pares)})')
print(f'Os números ímpares são: {impares} (Quantidade: {len(impares)})')
