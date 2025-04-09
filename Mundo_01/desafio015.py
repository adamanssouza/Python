dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km foram percorridos? '))
s = km * 0.15
s1 = dias * 60
r =  s + s1
print('O total a pagar por\33[0;32m {:.0f} km \33[mrodados em\33[0;34m {} \33[mdias utilizados é {:.2f}'.format(km, dias,r))
print('--=='*20)

import math
ca_oposto = float(input('Digite o comprimento do cateto oposto: '))
ca_adjacente = float(input('Digite o comprimento do cateto adjacente: '))
Hipotenusa = math.hypot(ca_adjacente, ca_oposto)
print('O comprimento da hipotenusa e: \33[1;32m{:.2f}\33[m'.format(Hipotenusa))

print('-==='*20)
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co **2 + ca **2)**(1/2)
print('O comprimento da hipotenusa e {:.2f}'.format(hi))
print('-==='*20)

from math import hypot
CO = float(input('Digite o comprimento do cateto oposto: '))
CA = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(CO, CA)
print('O comprimento da hipotenusa e: {:.2f}'.format(hi))