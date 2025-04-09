valores = []
while True:
    valor = int(input('Digite um valor: '))
    if valor in valores:
        print('Você já digitou este valor!')
    else:
        valores.append(valor)
        valores.sort()

    continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()
    if continuar != 'S':
        break

print(f'Lista final de valores: {valores}')
