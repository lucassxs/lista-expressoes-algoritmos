# Faça um algoritmo que receba o salário-base de um funcionário, calcule e mostre o salário líquido a receber, sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base e paga imposto de 7% sobre o salário-base.

salario_base = float(input('Digite o salário-base: R$ '))
GRAT = 5 / 100
IMPOSTO = 7/100
x = (salario_base - (IMPOSTO * salario_base))
salario_liquido = (x + GRAT * salario_base)
print('O valor do salário líquido é: R$ {}!'.format(salario_liquido))