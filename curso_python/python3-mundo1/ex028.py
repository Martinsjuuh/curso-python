# Desafio 028

#Escreva um programa que faça o computador" pensar" em um número inteiro entre 0 e 5 e peça para o usúario tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0,10) # Faz o computador "Pensar"
print('='*55)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('='*55)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta adivinhar 
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {} !'.format(computador, jogador))