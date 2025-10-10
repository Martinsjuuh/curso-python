# Adição +
# Subtração -
# Multiplicação *
# Divisão /
# Potência **
# Divisão Inteira //
# Resto da Divisão %
# 5 + 2 == 7
# 5 - 2 == 3
# 5 * 2 == 10
# 5 / 2 == 2.5
# 5 ** 2 == 25
# 5 // 2 == 2
# 5 % 2 == 1


# Ordem de Precedência
# 1. Parênteses ()
# 2. Exponenciação **
# 3. Multiplicação e Divisão (esquerda para direita)
# 4. Adição e Subtração (esquerda para direita)

#a = int(input("Digite um número: "))
#b = int(input("Digite outro número: "))
#c = int(input("Digite mais um número: "))
#calculo = (a + b * c)
#print('O resultado dessa operação é : {}'.format(calculo))

# 'Oi'+'Olá' = 'OiOlá'
# 'Oi'*5 = 'oioioioioi'
# '='*20 = '===================='
# print('='*20) = ====================

#nome = input('Qual é o seu nome? ')
#print('Prazer em te conhecer, {:20}!'.format(nome))
#print('Prazer em te conhecer, {:>20}!'.format(nome))
#print('Prazer em te conhecer, {:^20}!'.format(nome))
#print('Prazer em te conhecer, {:=^20}!'.format(nome))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2 
print('A soma é {}, o produto é {} e a divisão é {:.3f}.'.format(s, m, d), end= ' ')
print('Divisão inteira {} e potência {:.3f}'.format(di, p))

# Quebrar linha = \n (nova linha)
# Não quebrar no final do print = end="" 

