# Solicita ao usuário para digitar um número
num = int(input('Digite um número: '))

# Pergunta qual conversão o usuário deseja
print('Qual a fórmula que deseja converter?')
print(' (1) BINÁRIO  (2) OCTAL  (3) HEXADECIMAL')

# Solicita a opção de conversão
opcao = int(input('Escolha uma opção (1, 2 ou 3): '))

# Realiza a conversão de acordo com a opção escolhida
if opcao == 1:
    print('O número {} em binário é: {}'.format(num, bin(num)[2:]))  # Remove o prefixo '0b'
elif opcao == 2:
    print('O número {} em octal é: {}'.format(num, oct(num)[2:]))  # Remove o prefixo '0o'
elif opcao == 3:
    print('O número {} em hexadecimal é: {}'.format(num, hex(num)[2:]))  # Remove o prefixo '0x'
else:
    print('Opção inválida! Escolha 1, 2 ou 3.')
