# alternativa a
x = int(input('Digite um valor para x: '))
i = int(input('Digite um valor para i: '))
j = int(input('Digite um valor para j: '))
r = x**(i+j)
print('O resultado de {} elevado a {} + {} é {}!'.format(x, i, j, r))

# alternativa b
print('Letra B:')
a = int(input('Digite um valor para x: '))
b = int(input('Digite um valor para b: '))
c = int(input('Digite um valor para c: '))
r = (a + b) * (2 - c**2/(1 - c**3))
print('O resultado de {} + {}, multiplicado pelo produto da subtração de 2, por {} elevado ao quadrado, dividido pela subtração de 1 por {} elevado ao cubo é: {}!'.format(a, b, c, c, r))

# alternativa c
y = int(input('Digite um valor para y: '))
r = 2/(2 - 5*y)
print('O resultado do cálculo para y = a {} é: {}!'.format(y, r))

# alternativa d
a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))
c = int(input('Digite um valor para c: '))
d = int(input('Digite um valor para d: '))
r = a + b/(c + d)
print('O resultado para o cálculo em questão é: {}!'.format(r))

# alternativa e
r = int(input('Digite um valor para r: '))
s = int(input('Digite um valor para s: '))
t = int(input('Digite um valor para t: '))
resultado = 1/(1/r + 1/s + 1/t)
print('o resultado para o cálculo acima é: {}!'.format(resultado))

# alternativa f
m = int(input('Digite um valor para m: '))
n = int(input('Digite um valor para n: '))
r = 20/(m - n)
print('O resultado para m = {} e n = {} é {}!'.format(m, n, r))

# alternativa g
p = int(input('Digite um valor para p: '))
w = int(input('Digite um valor para w: '))
u = int(input('Digite um valor para u: '))
v = int(input('Digite um valor para v: '))
resultado = (p + w/(u + v))/(p - w/(u - v))
print('O resultado para o cálculo é: {}!'.format(resultado))

# alternativa h
a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))
c = int(input('Digite um valor para c: '))
d = int(input('Digite um valor para d: '))
resultado = a/(b + c/d)
print('O resultado para o cálculo é: {}'.format(resultado))

# alternativa i
n = int(input('Digite um valor para n: '))
resultado = (1 + 1/n)**n
print('O resultado para o cálculo é: {}'.format(resultado))

# alternativa j
x = int(input('Digite um valor para x: '))
y = int(input('Digite um valor para y: '))
import math
resultado = 1/2*math.sqrt(x**2 + y**2)
print('O resultado para o cálculo é: {}!'.format(resultado))

# alternativa k
a = int(input('Digite um valor para a: '))
b = int(input('Digite um valor para b: '))
c = int(input('Digite um valor para c: '))
import math
resultado = math.sqrt(a + b)/(c**2 - 2*a)
print('O resultado para o cálculo é: {}!'.format(resultado))