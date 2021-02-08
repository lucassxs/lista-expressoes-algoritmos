# Faça um algoritmo que receba um número inteiro de três dígitos e apresente separadamente os dígitos da unidade, da dezena e da centena. Exemplo: 736, Unidade 6, dezena 3, centena 7

numero = int(input('Digite um número inteiro de três dígitos: '))
n = str(numero)
print('Analisando o número: {}!'.format(numero))
print('Unidade: {}'.format(n[2]))
print('Dezena: {}'.format(n[1]))
print('Centena: {}'.format(n[0]))