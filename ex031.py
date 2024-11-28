print('NEM SEMPRE 3 RETAS FORMAM TRIANGULOS')
print('='* 50)

r1 = int(input('Primeira reta: '))
r2 = int(input('Segunda reta: '))
r3 = int(input('Terceira reta: '))

if r1 < r2+r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas formam um triangulo!')
else:
    print('As retas nao formam um triangulo')




