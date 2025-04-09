tot18 = toth = totm20 = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    
    while sexo not in 'MF':
        sexo = input('Digite o sexo [F/M]: ').upper().strip()[0]
    
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        toth += 1
    if sexo == 'F' and idade < 20:
        totm20 += 1
    
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Deseja continuar [S/N]: ').upper().strip()[0]
    
    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {tot18}')
print(f'Ao todo temos {toth} homens cadastrados.')
print(f'E temos {totm20} mulheres com menos de 20 anos.')
