# Escreva um programa que pergunte o nome, a altura em metros e a massa em kg do usuário. Em seguida o programa deverá emitir uma mensagem dizendo o nome do usuário e o seu indice de massa corporal.
nome = input('Digite o nome do paciente: ')
altura = float(input('Digite a altura, em metros: '))
massa = float(input('Digite a massa, em quilos, do paciente: '))
imc = (massa/altura**2)
print('O IMC do Sr. {} é {} kg/m^2!'.format(nome, imc))