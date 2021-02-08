# Faça um algoritmo que converta uma temperatura em graus Celsius para graus Fahrenheit e para Kelvin.

# Celsius para Fahrenheit
c = float(input('Digite o valor da temperatura em graus Celsius: '))
f = (9*c + 160)/5
print('O valor da temperatura de {} graus convertido para Farenheit é {}!'.format(c, f))

# Celsius para Kelvin
c = float(input('Digite o valor da temperatura em graus Celsius: '))
k = (c + 273.15)
print('O valor da temperatura de {} graus convertido para Kelvi é {} graus Kelvin!'.format(c, k))