# Cores no Terminal
# ANSI(escape sequence)
# \033[ (Aqui vai ser o style, back, text) m

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

#print('\033[1;34m Olá, Mundo!\033[m')
#nome = str(input('\33[35mQual é o seu nome?\033[m'))
#print('Olá,\33[30;45m{}\033[m.Boa Tarde!\33[30;45mJá pode ir para casa!\033[m'.format(nome))

#a = 3
#print('Os valores são \033[32m{}\033[m e \033[34m{}\033[m !'.format(a, b))

nome = 'Juliana'
print('Olá! Muito prazer em te conhcer, \033[4;35m{}\033[m!'.format(nome))