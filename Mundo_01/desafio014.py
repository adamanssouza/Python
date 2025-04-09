c  =float(input('Informe a temperatura em \33[1;31m°C\33[m: '))
f =(( 9 * c ) / 5 ) + 32
print('A temperatura de {}°C corresponde á {}°f!'.format(c,f))


print('--='*20)

from math import trunc
n = float(input('Digite um numero : '))
print('A porção do numero {} e igula {}'.format(n, trunc(n)))

nun = float(input('Digite um valor'))
print('A parte \33[0;32minteira\33[m de {} e {}'.format(nun, int(nun)))
