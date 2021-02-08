# Faça um algoritmo que receba 4 notas, calcular e informar a média ponderada, considerando que os pesos são respectivamente 2,2,3,3

n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))
n4 = int(input('Digite a quarta nota: '))
resultado = ((n1*2 + n2*2 + n3*3 + n4*3)/(2 + 2 + 3 + 3))
print('O resultado da média ponderada entre {}, {}, {} e {}, é: {}!'.format(n1, n2, n3, n4, resultado))
