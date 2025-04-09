tinta = 18 
rendimento = 250
n1 = int(input('Digite a altura: '))
n2 = int(input('Digite a largura: '))
s= (n1*n2)
t= s / (250 / 18)
r=t / 18
print('Para pintar a parede toda sera \33[0;31mutilizado\33[m um total de {:.2f} litros de tinta. \33[1;32m Um total de {:.0f} latas\33[m de tinta'.format(t,r))
