aluno = dict()
aluno['nome'] = str(input('Digite o  nome: '))
aluno['media'] = float(input('Digite a media: '))
print('-='*30)
print(f'- nome é igual a {aluno["nome"]}')
print(f'- média é igula a {aluno["media"]}')
if aluno['media'] >= 7:
    print('- situação e igual a Aprovado')
elif 5 <= aluno['media'] < 7:
    print('- situação e igual a Recuperaçao')
else:
    print('- situação e igual a Reprovado')

print('-=-='*30)
print('Guanabara')
print('-=-='*30)

aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >=7:
    aluno['situação'] = 'Aprovado'
elif 5<= aluno('media') <7 :
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print('-=-='*30)
for k, v in aluno.items ():
    print(f'{k} é igual a {v}')