import random

n1= input('NOME DOS ALUNO: ')
n2= input('NOME DOS ALUNO: ')
n3= input('NOME DOS ALUNO: ')
n4=input('NOME DOS ALUNO: ')
alunos = [n1,n2,n3,n4]
random.shuffle(alunos)

print('A ordem de escolha será: ')
print(alunos)
