# Faça um algoritmo que receba o salário de um funcionário e o percentual de aumento. Calcule e mostre o valor do aumento e o novo salário.

salario = float(input('Digite o valor do salário: '))
aumento = float(input('Digite o percentual de aumento: '))
novo_salario = (salario + ((aumento/salario)*10000))
print('O novo salário do funcionário será: R$ {} !'.format(novo_salario))