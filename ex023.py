frase = str(input('digite uma frase: '))

qa = frase.count('a')
oca = frase.find('a')
ua = frase.rfind('a')

print('sua frase tem {} a'.format(qa))
print('o a aparece primeiro em {}'.format(oca))
print('o a aparece pela ultima vez em {}'.format(ua))