from math import radians,sin,cos,tan

# Solicitar ao usuário que insira um ângulo em graus
angulo = float(input('Digite um ângulo em graus: '))

# Converter o ângulo de graus para radianos
angulo_radianos = radians(angulo)

# Calcular seno, cosseno e tangente
seno = sin(angulo_radianos)
cosseno = cos(angulo_radianos)
tangente = tan(angulo_radianos)

# Exibir os resultados
print('Para o ângulo de {:.2f} graus:'.format(angulo))
print('Seno: {:.2f}'.format(seno))
print('Cosseno: {:.2f}'.format(cosseno))
print('Tangente: {:.2f}'.format(tangente))
