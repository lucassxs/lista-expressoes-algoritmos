# Antes do racionamento de energia ser decretado, quase ninguém falava em quilowatts, mas agora todos incorporaram essa palavra em seu vocabulário. Sabendo-se que 80 quilowatts de energia custam 1/5 do salário mínimo, faça um algoritmo que receba o valor do salário mínimo e a quantidade de quilowatts gasta por uma residência e calcule:
# O valor em reais de um quilowatt
# o valor em reais a ser pago
# o novo valor a se pago por essa residência com um desconto de 10%

SALARIO_MINIMO = 1100
KWH = 2.75
print('O valor do kwh é de: {}!'.format(KWH))
qw_gasto = int(input('Inserir o valor total de quilowatts gasto no mês: '))
valor = (KWH * qw_gasto)
print('O valor a ser pago nesse mês é: R$ {}!'.format(valor))
valor_desc = (valor - (valor*10/100))
print('O valor com desconte corresponde a: R$ {}!'.format(valor_desc))