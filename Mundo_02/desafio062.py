# Solicitar o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
termos_exibidos = primeiro_termo # Inicialmente exibimos os 10 primeiros termos
mais = 10
total = 0
const = 1
print("\nOs próximos termos da PA são:")
while mais != 0 :
    total = total + mais
    while const <= total:
        print('{} - '.format(termos_exibidos), end='')
        termos_exibidos +=razao
        const +=1
    print('Pausa')
    mais = int(input('Quantos termos a mais quer mostrar ?'))
print('Progressao finalizada com {} termos mostrados '.format(total))