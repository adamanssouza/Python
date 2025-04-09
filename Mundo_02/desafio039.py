from datetime import date

# Entrada do usuário
ano_nascimento = int(input("Digite o ano de nascimento: "))
sexo = int(input("Digite seu sexo (1 - Homem, 2 - Mulher): "))

# Ano atual e cálculo da idade
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

# Cálculo do tempo de alistamento
tempo = 18 - idade

# Verifica o sexo
if sexo == 1:  # Homem
    print("Na constituição brasileira, você é obrigado a se alistar com 18 anos.")
    if idade == 18:
        print(f"Você está com {idade} anos. Está em tempo de se alistar!")
    elif idade < 18:
        print(f"Você está com {idade} anos. Ainda não é hora de se alistar, faltam {tempo} anos.")
    else:
        print(f"Você está com {idade} anos. O seu tempo de alistamento passou há {abs(tempo)} anos!")
elif sexo == 2:  # Mulher
    print("Na constituição brasileira, o alistamento militar para mulheres não é obrigatório.")
    if idade == 18:
        print(f"Você está com {idade} anos. Está em tempo de se alistar!")
    elif idade < 18:
        print(f"Você está com {idade} anos. Ainda não é hora de se alistar, faltam {tempo} anos.")
    else:
        print(f"Você está com {idade} anos. O seu tempo de alistamento passou há {abs(tempo)} anos!")
else:
    print("Sexo inválido. Digite 1 para Homem ou 2 para Mulher.")
