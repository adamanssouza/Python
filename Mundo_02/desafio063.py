from sympy import fibonacci

# Gerar os primeiros 10 números de Fibonacci
n = int(input('Digite o numero: '))
print("Sequência de Fibonacci:")
for i in range(n):
    print(fibonacci(i), end=" → ")
print("FIM")
