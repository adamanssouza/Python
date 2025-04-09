H = 'Homem'
M = 'Mulher'
sexo = str(input('Digite o sexo [ H \ M ]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    idade = int(input('Digite sua idade: ')).strip().upper()[0]
    print(f'{sexo} Sexo registrado com sucesso')
    if sexo == 'H':
        print(f'seu sexo e {H} ')
        break
    elif sexo == 'M':
        print(f'seu sexo e {M} ')
        break
    else:
        print('Digite corretamente com [H] - Homem e [M] - MUlher!')
        


sexo = str(input('Digite o sexo [ H \ M ]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite corretamente com [H] - Homem e [M] - MUlher!')).strip().upper()[0]
print(f'{sexo} Sexo registrado com sucesso')


        