ficha =list ()
while True:
    nome = str(input('Nome: '))
    n1 =float(input('N1: '))
    n2= float(input('N2: '))

    media = (n1+n2) / 2

    dados = [nome,n1,n2,media]

    ficha.append([nome,[n1 , n2],media])



    resp = str(input('Quer continuar [N\S]')).upper().strip()
    if resp in 'Nn':
        break

print('-=-='*10)
print(f'{'No.':<4}{'NOME':<10}{'MEDIA':>8}')
print('--'*20)
for i, a in enumerate(ficha):
      print(f'{i:<4}{a[0]:>10} {a[2]:>8.1f}')

while True:
    print('-'*35)
    opc = int(input('Mostrar nota de qual aluno?  999 encerrar! '))
    if opc == 999:
        print('finalisado')
        break
    if opc <=  len(ficha):
        print(f'Notas de {ficha[opc][0]} são: N1 = {ficha[opc][1]}, N2 = {ficha[opc][2]}')
