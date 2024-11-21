n1 = input('digite algo para verificação: ')


print( 'O tipo primitivo deste valor é: ', type(n1))
print( 'Só tem espaços? ', n1.isnumeric())
print('É um numerico? ', n1.isalnum())
print('É um alphanumerico? ', n1.isalpha())
print('Tem caracteres? ', n1.isalpha() )