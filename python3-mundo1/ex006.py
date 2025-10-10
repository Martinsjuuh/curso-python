# Desafio 006
# Crie um algoritmo que leia um número e mostre o seu dobro e seu triplo e raiz quadrada.

n = int(input('Digite um número: '))
# d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n , (n*2)))
print('O triplo de {} vale {}.\nA raiz quadrada de {} vale {:.2f}.'.format(n, t, n, r))

#raiz quadrada = pow(n, (1/2)) ou  n ** (1/2)