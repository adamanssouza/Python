nun = cont = soma = 0
nun = int(input('Digite o numero:[999] pra parar  '))
while nun != 999:
    soma += nun
    cont += 1
    nun = int(input('Digite o numero: '))

print('Você digitou {} numros e a soma entre eles foi {}'.formati(cont, soma))

