# Efetuar o cálculo em litros de combustível gastos em uma viagem, sabendo-se que o carro faz 12km por litro. Deverão ser fornecidos o tempo gasto na viagem e a velocidade média. o algoritmo deverá apresentar os valores da velocidade média, tempo gasto na viagem, distância percorrida e quantidade de litros utilizados na viagem.

# Cálculo do combustível gasto na viagem.
d = float(input('Digite o valor da distância em km a percorrer: '))
AUT = 12
consumo = (d/AUT)
t = float(input('Digite o tempo em horas de duração da viagem: '))
vm = (d/t)
print('A velocidade média da viagem é de: {} km/h'.format(vm))
print('O tempo gasto na viagem será de: {} horas'.format(t))
print('A distância percorrida nessa viagem é de: {} quilômetros!'.format(d))
print('O consumo de combustível nessa viagem será de: {} litros!'.format(consumo))