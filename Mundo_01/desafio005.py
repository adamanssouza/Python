n1 = int(input('\33[0;32mUm valor:\33[m '))
n2 = int(input('\33[33mOutro valor: \33[m'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {},\n o produto é {} e a divisão é {:.3f}'.format(s, m, d), end='')
print('Divisão interira {} e potência {}'.format( di, e))
#print('A soma vale {}'.format(n1 + n2))


