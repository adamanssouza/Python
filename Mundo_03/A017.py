num = (2, 4 ,8 ,9 )#Uma tupla nao pode ser alterada ou adicionada.
print(num)
print(num[2])#Ira selecionar  e mostrar o terceiro elemento (8).
nu = [2, 4 , 8 ,9 ]
nu[2] = 3#Substui um elemento a lista.
print(nu)

n = [ 2, 4 , 8, 9 ]
n.append(1)#Adiciona um elemento a lista.
n.sort()#Faz o alinhamento dos numeros.
n.sort(reverse=True)#Faz a contagem ao contrario.
n.insert(2, 0)#Insere um elento ( 0 ) na posição ( 2 )
print(n)
print(f'Essa lista tem {len(n)} elementos.')# Len- Faz a contagem dos elementos.

# n.pop()#Faz a remoção de um elemento.
# n.remove()#Faz a remoçao de um elemento.

if 4 in n:
    n.remove(4)
else:
    print('Nao achei o numero 4')


valores = []
valores.append(5)
valores.append(9)
valores.append(4)
valores.append(3)

for v in enumerate(valores):
    print(f'Na posição {v} encontrei o valor {v}! ')
print('Cheguei ao final da lista. ')

valores = list()
for cont in range(0,5):#contador dos valores armazendados
    valores.append(int(input('Digite um valor: ')))#adiciona os valores a lista 

for v in enumerate(valores):
    print(f'Na posição {v} encontrei o valor {v}! ')
print('Cheguei ao final da lista. ')


#peculiaridade do phyton

a = [2, 3, 4, 7]
b = a
b[2]=8#Vai fazer alteração na segunda posiçao de ambos ja que a e b sao iguais.
print(f'List A :{a}')
print(f'List B :{b}')
#B e um espelhamento de A.

a = [2, 3, 4, 7]
b = a[:]#cria uma copia de A e joga em B
b[2]=8#Vai fazer alteração na segunda  de B ja que B e uma copia e nao igual.
print(f'List A :{a}')
print(f'List B :{b}')
#B não tem uma ligação com A pois [:] faz uma copia.

('''
[Início]
     |
[Inicializar lista vazia]
     |
[Iniciar laço (for) 5 vezes]
     |
[Solicitar valor (input)]
     |
[Condição: c == 0 ou n > lista[-1]?]
     |-----------------------------|
  Sim |                             Não
     |                                  |
[Adicionar n ao final]           [Iniciar laço (while)]
     |                                  |
[Imprimir "adicionado ao final"]   [Verificar se n <= lista[pos]]
     |                                  |
[Próxima iteração]                   | Sim
                                     |
                            [Inserir n na posição]
                                     |
                           [Imprimir "adicionado na posição X"]
                                     |
                              [Sair do laço while]
                                     |
                               [Próxima iteração]
                                     |
[Laço (for) termina?] --------------------|
     |
[Imprimir lista final]
     |
[Fim]
''')