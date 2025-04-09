# tupla  = ()
# ista =  []
# dicionario = {}

lanche =('Hamburguer','suco', 'Pizza', 'Pudim')
print(lanche[1])

lanche =('Hamburguer','suco', 'Pizza', 'Pudim')
print(lanche[3])

lanche =('Hamburguer','suco', 'Pizza', 'Pudim')
print(lanche[-2])

lanche =('Hamburguer','suco', 'Pizza', 'Pudim')
print(lanche[1:3])

lanche =('Hamburguer','suco', 'Pizza', 'Pudim')
print(lanche[:2])

lanche =('Hamburguer','suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba')
   

for cont in range(0,len(lanche)):
    print(lanche[cont])

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} e na posiçao {pos}')

print(sorted(lanche))
print(lanche)

a = ( 2,5,4)
b = ( 5,8,1,2)
c = a + b 
print(c)
print(len(c))
print(c.cout(5))#quantos numeros 5 tem no trupla 
print(c.index(8)) # qual a posiçao do numeo 8

pessoa = ('Gustavo',39,'M',1.75)
del(pessoa)
print(pessoa)
