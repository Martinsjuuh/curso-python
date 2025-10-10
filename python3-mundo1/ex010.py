# Desafio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere Us$1,00 = R$5,47 

real = float(input('Quanto  dinheiro você tem na carteira? R$'))
dolar = real / 5.47
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))