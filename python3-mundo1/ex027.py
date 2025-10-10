# Desafio 027

# Faça um programa que leia o nome completo de uma pessoa,mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza primeiro = Ana último = Souza 

n = str(input('Digite sue nome completo: ')).strip()
nome = n.split() #Jogou  para lista
print('Muito prazer em te conhecer!')
print ('Seu primeiro nome é {}'.format(nome[0]))
print ('Seu último nome é {}'.format(nome[len(nome)-1]))

