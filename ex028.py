from datetime import date
print('DESCUBRA SE O ANO É BISSEXTO')
print('='*30)
print('='*30)

ano = int(input('QUAL ANO DESEJA SABER SE É BISSEXTO OU NAO? '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano  % 400:
    print('{} É ANO BISSEXTO'.format(ano))
else:
    print('{} ANO NÃO É BISSEXTO'.format(ano))