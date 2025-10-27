# Desafio 044

# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# - à vista dinheiro/cheque:10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS '))
compras = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
print([ 1 ] à vista dinherio /cheque
print([ 2 ] à vista cartão
print([ 3 ] 2x no cartão
print([ 4 ] 3x ou mais no cartão''')
opçao = int(input('Qual é a opção? '))
if opçao == 1:
    total = compras - (compras * 10 / 100)
elif opçao == 2:
    total = compras - (compras * 5 / 100)
elif opçao == 3:
    total = compras
    parcelas = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcelas))
elif opçao == 4:
    total = compras + (compras  * 20 / 100)
    totparc = int(input('quantas parcelas '))
    parcelas = total / totparc
    print('Sua compra de R$')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compras, total))
