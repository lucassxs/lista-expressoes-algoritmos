# Faça um programa que receba um ângulo em graus e apresente o seno, cosseno, tangente, secante e cossecante desse ângulo.

angulo = float(input('Digite o valor em graus do ângulo: '))
import math
sen = math.sin(math.radians(angulo))
print('O seno do angulo {} é {}!'.format(angulo, sen))
cos = math.cos(math.radians(angulo))
print('O cosseno do angulo: {} é {}!'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('A tangente do angulo {}, é {}!'.format(angulo, tan))
cossec = math.acos(math.radians(angulo))
print('A cossecante do angulo {} é {}!'.format(angulo, cossec))
sec = math.acos(math.radians(angulo))
print('O valor da secante do angulo {} é {}!'.format(angulo, sec))