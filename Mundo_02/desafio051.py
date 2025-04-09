# Solicitar o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
decimo = primeiro_termo + (10-1) * razao  # Fórmula da PA
# Exibir os 10 primeiros termos da PA
print("Os 10 primeiros termos da PA são:")
for c in range(primeiro_termo, decimo + razao, razao):  # Para os 10 primeiros termos
    print('{}'.format(c), end =' = ')
print('ACABOU')
