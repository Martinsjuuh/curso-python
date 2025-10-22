# Desafio 038

#Escreva um programa que leia dois números interiros e compare-os, mostrando na tela uma mensagem:

# - 0 primeiro valor é maior
# - 0 segundo valor é maior
# - Não existe valor maior, os dois são iguais

n1 = int(input('\033[1;31m Primeiro\033[m número: '))
n2 = int(input('\033[1;34m Segundo\033[m número: '))
if n1 > n2:
    print('O\34033[1;31m PRIMEIRO\033[m valor é maior')
elif n2 > n1:
    print('O\033[1;34m SEGUNDO\033[m valor é maior ')
else:
    print('Os dois valores são IGUAIS!')

# \033[0;33;44m

# Style                                             Text                   Back
# 0 None(Sem estilo)                               30(Branco)               40
# 1 Bold(Negrito)                                  31(Vermelho)             41
# 4 Underline(Sublinhado)                          32(Verde)                42
# 7 Negative(Inverter as configurações)            33(Amarelo)              43
#                                                  34(Azul)                 44
#                                                  35(Roxo)                 45
#                                                  36(Ciano)                46
#                                                  37(Cinza)                47