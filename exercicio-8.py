# Faça um algoritmo para, tendo como dados de entrada dois pontos quaisquer no plano P1(X1,Y1) e P2(X2,Y2), escreva a distância entre eles.
x1 = int(input('Digite um valor para a coordenada x1: '))
x2 = int(input('Digite um valor para a coordenada x2: '))
y1 = int(input('Digite um valor para a coordenada y1: '))
y2 = int(input('Digite um valor para a coordenada y2: '))
import math
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print('A distância entre os dois pontos para o plano é: {}!'.format(d))