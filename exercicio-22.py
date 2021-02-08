# Fazer um algoritmo que leia o tempo de duração de um evento em uma fábrica expresso em segundos e mostre-o expresso em horas, minutos e segundos. por exemplo: 4854 segundos, representam 1 hora, 20 minutos e 54 segundos.

segundos = int(input('Digite o tempo em segundos: '))
horas = segundos//3600
res = segundos % 3600
minutos = res // 60
seg = res % 60
print('O valor de {} segundos digitado corresponde a {} horas, {} minutos e {} segundos.'.format(segundos, horas, minutos, seg))