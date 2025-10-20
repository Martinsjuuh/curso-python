# Desafio 040

#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,de acordo com a média atingida:

# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado

n1 = int(input('Primeira nota: '))
n2 = int(input('Segunda nota: '))   
media = n1 + n2 / 2
print('A media é {}'.format(media))