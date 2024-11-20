n1 = input('digite algo para verificação: ')

print('Abaixo mostrará qual o tipo primitivo do valor colocado, e se, ele é numerico, alpha numerico e caracter')
print(type(n1))
print(n1.isnumeric())
print(n1.isalnum())
print(n1.isalpha())