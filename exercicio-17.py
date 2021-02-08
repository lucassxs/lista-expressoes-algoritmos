# Escreva um programa que solicite dois números inteiros para serem divididos e apresente em seguida, o dividendo, divisor, quociente e resto da divisão.

x = int(input('Digite o dividendo inteiro: '))
y = int(input('Digite o divisor: '))
quociente = (x/y)
resto = (x%y)
print('O dividendo apresentado é: {}!'.format(x))
print('O divisor apresentado é: {}!'.format(y))
print('O quociente da divisão será: {}!'.format(quociente))
print('O resto da divisão será: {}'.format(resto))