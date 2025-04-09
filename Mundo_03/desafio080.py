# Inicializa uma lista vazia onde os valores serão armazenados
lista = []

# Laço que repete 5 vezes (o range vai de 0 a 4, ou seja, 5 iterações)
for c in range(0, 5):
    # Solicita ao usuário que digite um valor inteiro
    n = int(input('Digite um valor: '))
    
    # Caso seja o primeiro valor (c == 0) ou o valor digitado seja maior que o último valor da lista
    if c == 0 or n > lista[-1]:
        # Adiciona o valor ao final da lista
        lista.append(n)
        # Exibe uma mensagem informando que o valor foi adicionado ao final
        print('adicionado ao final da lista')
    else:
        # Caso o valor não seja maior que o último valor, será inserido na posição correta para manter a ordem
        pos = 0  # Inicializa a posição onde vamos procurar o local de inserção
        # Laço que percorre a lista para encontrar a posição onde o valor deve ser inserido
        while pos < len(lista):
            # Verifica se o valor digitado é menor ou igual ao valor na posição "pos"
            if n <= lista[pos]:
                # Insere o valor na posição "pos"
                lista.insert(pos, n)
                # Exibe uma mensagem indicando a posição em que o valor foi inserido
                print(f'Adicionado na posição {pos}')
                break  # Sai do laço ao adicionar o valor
            pos += 1  # Avança para a próxima posição da lista
          
# Após o loop terminar, exibe a lista final com os valores digitados e organizados
print(f'Os valores digitados foram {lista}')

