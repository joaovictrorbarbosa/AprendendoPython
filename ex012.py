print('SEU SALARIO COM 15% DE AUMENTO, QUANTO FICARIA?')

s= int(input('Digite qual seu salario atual: '))
c15= (s*15)/100
s15= s + c15

print('Seu salario com um adicional de 15%, ficará: {}'.format(s15))