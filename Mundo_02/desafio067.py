print(f"{'Tabuada de varios numeros':*^30}")
print('->'*20)
n = 0
soma = 0 
while True:
    n = int(input('Quer ver a taboada de qual valor? '))
    if n <=0:
        print('Tabuada encerrada!')
        break
    for i in range(1,11):
        soma = n*i 
        print(f'{n} x {i} = {soma}')

    