# Escreva um programa que solicite ao usuário o raio(em centímetros), de uma circunferência e apresente a ele o diâmetro, a área e o perímetro da respectiva cincunferência.

# Cálculo do diâm
r = int(input('Digite um valor para o raio: '))
d = (2*r)
print('O valor do diâmetro da respectiva circunferência para um raio de {}, é: {}!'.format(r, d))
#
#
# Cálculo da área da circunferência
r = int(input('Digite um valor para o raio: '))
PI = 3.14
c = (PI*r**2)
print('O valor da área da circunferência para um raio de {}, é {}!'.format(r, c))

# Cálculo do perímetro daq circunferência:
r = int(input('Digite um valor para o raio: '))
PI = 3.14
c = (2*PI*r)
print('O valor do perimetro da circunferencia para um raio de {}, é {}!'.format(r, c))