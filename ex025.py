velocidade = float(input('Qual a velocidade atual do carro (em km/h)? '))
if velocidade > 80:

    print('Voce foi multado, o limite da via é de 80km/h')
    multa = (velocidade-80)*7

    print('O valor de sua multa foi de R${:.2f}'.format(multa))

else:
    print('Voce nao foi multado.')

print('='*30)
print('DIRIJA SEMPRE COM SEGURANÇA')

