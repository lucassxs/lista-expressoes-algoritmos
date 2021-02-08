# Faça um algoritmo para receber os valores dos catetos de um triângulo retângulo e apresentar o valor da hipotenusa do triângulo.

ca = float(input('Digite um valor para o cateto adjacente: '))
co = float(input('Digite um valor para o cateto oposto: '))
import math
hip = math.sqrt(ca**2 + co**2)
print('O valor da hipotenusa do triangulo em questão é: {}!'.format(hip))