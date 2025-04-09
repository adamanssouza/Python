# Solicita ao usuário que digite uma expressão
exp = input('Digite uma expressão: ')
print('=-='*10)  # Exibe uma linha separadora

try:
    # Avalia a expressão fornecida e guarda o resultado
    n = eval(exp)
    # Caso não ocorra erro, informa que a expressão é válida
    print('Sua expressão é válida!')
    print('=-='*10)  # Exibe outra linha separadora
    # Exibe o resultado da avaliação da expressão
    print(f'O resultado da expressão é: {n}')
except:
    # Caso ocorra algum erro ao avaliar a expressão, entra no except
    print('Sua expressão não é válida!')

print('=-=-'*10)  # Exibe uma linha separadora

# Solicita uma nova expressão para verificar a validade dos parênteses
expr = str(input('Digite a expressão'))  
pilha = []  # Inicializa uma lista que vai simular uma pilha para verificar os parênteses

# Loop que percorre todos os caracteres da expressão
for simb in expr:
    if simb == '(':  # Quando encontra um parêntese de abertura
        pilha.append('(')  # Adiciona na pilha
    elif simb == ')':  # Quando encontra um parêntese de fechamento
        if len(pilha) > 0:  # Verifica se a pilha não está vazia (se há um parêntese de abertura correspondente)
            pilha.pop()  # Remove o parêntese de abertura correspondente
        else:
            # Se a pilha estiver vazia, significa que o parêntese de fechamento não tem par correspondente
            pilha.append(')')
            break

# Verifica se a pilha está vazia no final, o que significa que todos os parênteses estão balanceados
if len(pilha) == 0:
    print('Sua expressão está válida')  # Expressão com parênteses balanceados
else:
    print('Sua expressão está errada')  # Expressão com parênteses desbalanceados
