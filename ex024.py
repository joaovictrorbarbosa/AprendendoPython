from random import randint
computador = randint(0,5) #o numero pensado pelo pc
print('=='*20)
print('VOU PENSAR NUM NUMERO, CONSEGUE ADIVINHAR?')
jogador = int(input('Digite o numero de 0 a 5, que voce acredita ser: '))

if jogador == computador:
    print('VOCE ACERTOU O NUMERO É {}'.format(computador))
else:
    print('VOCE ERROU, O NUMERO ESCOLHIDO POR MIM FOI: {}'.format(computador))




