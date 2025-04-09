galera = list()
soma = media = 0

while True:
    pessoa = dict()  # Mova a criação de pessoa aqui para dentro do loop
    pessoa['nome'] = str(input('Digite o nome: '))
    pessoa['sexo'] = str(input('Digite o sexo: ')).upper()
    
    while pessoa['sexo'] not in 'MF':
        print('Caracter não aceito, digite [M ou F]!')
        pessoa['sexo'] = str(input('Digite o sexo: ')).upper()

    pessoa['idade'] = int(input('Digite a idade: '))
    soma += pessoa['idade']  # Soma as idades
    galera.append(pessoa.copy())

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('Erro, Responda apenas [S ou N]!')

    if resp == 'N':
        break

print('-='*30)
print(f'A) Ao todo temos {len(galera)} pessoas cadastradas.')

media = soma / len(galera)  # Cálculo da média
print(f'B) A média de idade é de {media:.2f} anos.')

print('C) As Mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f"{p['nome']}", end=' ')
print()
print('<<ENCERRADO>>')
