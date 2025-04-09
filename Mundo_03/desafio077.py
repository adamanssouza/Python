vogal = ('a', 'e', 'i', 'o', 'u')  # Definindo as vogais
palavra = input('Digite uma palavra: ')

for letra in palavra:
    if letra.lower in vogal:
        print(letra)  # Imprime a vogal que aparece



