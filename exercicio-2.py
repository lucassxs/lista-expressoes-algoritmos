# Escrever as expressões lógicas relacionais que reflitam o significado das seguintes condições:

# Alternativa A : X está no intervalo aberto entre 0 e 3, (0,3])
x = int(input('Digite o valor de x: '))
if 3 > x > 0:
    print('A variável x está contida no intervalo entre 0 e 3!')
else:
    print('A variável x não está contida no intervalo entre 0 e 3!')
x = int(input('Digite o valor de x: '))
if 3 > x > 0:
    print('A variável x está contida no intervalo entre 0 e 3!')
else:
    print('A variável x não está contida no intervalo entre 0 e 3!')
x = int(input('Digite o valor de x: '))
if 3 > x > 0:
    print('A variável x está contida no intervalo entre 0 e 3!')
else:
    print('A variável x não está contida no intervalo entre 0 e 3!')

# Alternativa B: X está no intervalo fechado entre 0 e 3, [0,3]
x >= 0 and x <= 3

# Alternativa C: P excede X, ou excede Y, ou excede Z
P > x or P > y or P > Z

# Alternativa D: X é maior igual a 0 e menor igual a 6
x >= 0 and X<= 6

# Alternativa E: M é maior do que 50 ou menor do que 0
m > 50 or m < 0

# Alternativa F: x nãoé menor do que y
x > y

# Alternativa G: X não é menor do que y, nem menor do que z
x > y and x > z 

# Alternativa H: a é igual a b, e igual a c
a = b = c

# Alternativa I: A não é igual a B, e C não é igual a D, nem igual a E
a != b and c != D and c != e

# Alternativa J: A e E estão entre 1 e 10, incuindo os extremos
a >= 1 and a <= 10 and b >= 1 and b <= 10

# Alternativa K: A e B são maiores que C ou, então A e B são menores ou iguais a 20
((a > c) and (b > c)) or ((a<= 20) and (b <= 20))

# Alternativa L: Nem A, nem B é maior do que 10
a <= 10 and b<= 10

# Alternativa M: X não está entre A e B
x < a and x > b

