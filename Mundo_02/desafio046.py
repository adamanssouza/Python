from time import sleep
for cont in range(10, -1, -1):
    print(cont)
    sleep(0.5)
print('FELIZ')
sleep(1)
print('ANO')
sleep(1)
print('NOVO')
sleep(2)
print('\033[1;31mFELIZ ANO NOVO\033[m')
