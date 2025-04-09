try:
    # Solicitar peso e altura
    peso = float(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))

    # Validar se peso e altura são positivos
    if peso <= 0 or altura <= 0:
        print("Peso e altura devem ser números positivos e maiores que zero!")
    else:
        # Calcular o IMC
        imc = peso / (altura**2)
        print(f'Seu peso é {imc:.1f}')
        # Avaliar o IMC e imprimir a mensagem correspondente
        if imc < 18.5:
            print(f'Você está abaixo do peso! ')
        elif 18.5 <= imc < 25:
            print(f'Você está no peso ideal! IMC')
        elif 25 <= imc < 30:
            print(f'Você está com sobrepeso! ')
        elif 30 <= imc < 40:
            print(f'Você está com obesidade!')
        else:
            print(f'Obesidade mórbida! Procure um especialista.')

except ValueError:
    print("Por favor, insira valores numéricos válidos para peso e altura.")
