from itertools import count

n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite o 2º numero: '))
n3 = int(input('Digite o 3º numero: '))

#verificando qual menor:
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n2 and n3 < n1:
    menor = n3

#verificando qual maior:
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor numero é {}'.format(menor))
print('O maior numero é {}'.format(maior))