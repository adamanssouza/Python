frase = str(input('digite uma frase')).strip().upper()
palavra =  frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} e {} '. format(junto,inverso))
if inverso == junto:
    print('temos um palindromo!')
else:
    print('A frase digitada nao e um palindromo')


texto = input("Digite um texto: ").lower().replace(" ", "")  # Converte para minúsculas e remove espaços
if texto == texto[::-1]:  # Compara a string com sua versão invertida
    print("O texto é um palíndromo!")
else:
    print("O texto não é um palíndromo.")
print(texto[::-1])
