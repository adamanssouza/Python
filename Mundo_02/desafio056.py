from datetime import datetime
print('-=='*10)
print('PREENCHA A FICHA DE CADASTRO! ')
print('-=='*10)
maior_idade_homem = 0
mome_velho = ''
mulheres_20 = 0
soma_idade = 0
media_idade = 0
ano_atual = datetime.now().year
for p in range(1,5):
    nome = str(input('Digite o {}° nome: '.format(p))).strip()
    idade= int(input('Digite sua idade: '))
    sexo = str(input('Digite o sexo! [M / F] ! ')).strip()
    soma_idade += idade
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mn' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres_20 +=1
media_idade = soma_idade / 4
print(f'A média de idade é {media_idade:.2f} anos')
print('O homem mais velho e {} e tem  {} anos'.format(nome_velho, maior_idade_homem))
print(f'O número de mulheres com menos de 20 anos sao {mulheres_20}')



