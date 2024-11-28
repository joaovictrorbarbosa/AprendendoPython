viagem = float(input('Digite a distancia de sua viagem em Km: '))
print('Voce fara uma viagem de {} Km'.format(viagem))
if viagem <= 200:
    preco = viagem * 0.50
else:
    preco = viagem * 0.45

print('=' * 30)
print('=' * 30)
print('O preço de sua passagem será de R${:.2f}'.format(preco))
