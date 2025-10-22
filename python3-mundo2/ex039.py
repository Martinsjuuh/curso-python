# Desafio 039

#faça um programa que leia o ano de nascimento de um jovem e informe,de acordo com sua idade:

# Se ele ainda vai alistar ao serviço militar
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.

# Seu programa também deverá mostrar o tempo que falta ou que passou o prazo.

from datetime import date 
atual = date.today().year # Ano atual
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDITAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}!'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}!'.format(ano))
    