n = int(input("Digite um número: "))
tot = 0
for c in range(1, n + 1):  
    if n % c == 0:   
        print('\033[33m', end='')
        tot +=1
    else:
        print(" \033[31m", end='')
    print('{} '.format( c ), end='')
print('\033[m O {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('E por isso ele e PRIMO')
else:
    print('Epor isso ele Não e primo ')
    