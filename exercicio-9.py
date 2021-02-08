# Em épocas de pouco dinheiro, os comerciantes estão procurando aumentar suas vendas oferecendo desconto. Faça um algoritmo que receba o valor de um produto e o desconto oferecido e imprima o novo valor do produto.
vi = int(input('Digite o preço do produto: R$ '))
d = 20/100
vf = (vi - vi*d)
print('O valor do produto já incluindo o desconto é: R$ {}!'.format(vf))