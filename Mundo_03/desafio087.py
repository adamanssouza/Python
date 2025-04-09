matriz = [[0,0,0],[0,0,0],[0,0,0]]
maior = menor = scol = spar = 0

# Input values into the matrix
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor: [{l}, {c}]:'))

print('-=-=' * 10)

# Print the matrix and calculate the sum of even numbers
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')

        # Check if the value is even
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]  # Sum of even numbers

    print()

print('-=-=' * 10)
print(f'A soma dos Pares é {spar}')  # Display sum of even numbers

# Sum the values in the third column
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma da terceira coluna é {scol}')

# Find the largest value in the matrix
maior = matriz[0][0]  # Start with the first value
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] > maior:
            maior = matriz[l][c]
print(f'O maior valor é {maior}')
