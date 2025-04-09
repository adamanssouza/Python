formulario = list()
pessoas = dict()
for c in range(0,2):
    pessoas['nome'] = str(input('Digite um nome? '))
    pessoas['sexo'] = str(input('Digite um sexo? '))
    pessoas['idade'] = int(input('Digite uma idade? '))
    pessoas['peso'] = float(input('Digite seu peso? '))
    formulario.append(pessoas.copy())
print(formulario)
print('-=-'*30)
for p in formulario:
    print(p)