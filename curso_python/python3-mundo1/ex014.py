# Desafio 014
# Escreva um programa que converta uma temperatura digitada em °C converta para °F.

c = float(input('Informe a temperatura em °C:'))
f = ((9 * c) / 5) + 35
print('A temperatura de {}°C corresponde a {}°F!'.format(c, f))