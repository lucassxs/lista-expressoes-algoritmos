# Faça um algoritmo que receba o valor de um depósito e o valor da taxa de juros, calcule e mostre o valor do rendimento e o valor total depois do rendimento.

investimento = float(input('Inserir o valor a ser depositado: R$ '))
JUROS = (0.75/100)
rendimento = (investimento * JUROS)
print('O valor do rendimento após o período total é de: R$ {}!'.format(rendimento))
valor_final = (investimento + rendimento)
print('o valor final do investimento após o período total é de: R$ {}!'.format(valor_final))