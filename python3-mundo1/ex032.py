# Desafio 032

#faça um programa que leia um ano qualuqer e mostre se ele é BISSEXTO.

# Ano BISSEXTO
from datetime import date
ano = int(input('Qual ano quer analizar?Coloque 0 para analizar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # Divisivel por 4 e também pode ser divisivel por 100 ,não pode ser diferente de 0 ou então o ano ser divisivel por 400
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))

# and -> e
# or -> ou
# != -> diferente
# == -> igual