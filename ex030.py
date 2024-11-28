salario = float(input('Qual seu salario? '))
aumento10 = (salario*10)/100
aumento15 = (salario*15)/100
if salario > 1250:
    a1 = (salario + aumento10)
    print('seu salario sera de R${:.2f}'.format(a1))
else:
    a2 = salario + aumento15
    print('Seu salario será de R${}'.format(a2))
