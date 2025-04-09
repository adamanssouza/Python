from time import sleep
Somar = 1
Multiplicar = 2
maior = 3
novos = 4
sair = 5
s = 0

n1 = int(input('Digite o 1° numero: '))
n = int(input('digite o 2° numero: '))
while s != 5:
    print('-='*10)
    print('''
[1]Somar
[2]Multiplicar
[3]maior
[4]novos numeros
[5]sair do programa''')
    print('-='*10)
    s = int(input('Digite sua escolha: '))
    if s == 1:
        soma = n1+n
        print(f'A soma e {soma}')
        
    elif s == 2:
        mul= n1*n
        print(f'A soma e {mul}')
        
    elif s == 3:
        if n<n1:
            print(f'O mairo e {n1}')
            
        else:
            print(f'O maior e {n}')
            
    elif s == 4:
        print('informe os numeros novamente')    
        n1 = int(input('Digite o 1° numero: '))
        n = int(input('digite o 2° numero: '))
    print('-=='*10)
    sleep(2)
print('Fim do programa! Volte sempre')



