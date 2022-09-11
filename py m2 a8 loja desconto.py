print('{:=^40}'.format('lojas do jon'))
preço = float(input('preços das compras: R$'))

print('''FORMAS DE PAGAMENTO
[1] á vista dinheiro/cheque
[2] á vista no cartão
[3] 2x no cartão
[4] 3x ou mais no cartão ''')

opção = int(input('qual opção? '))

if opção == 1:
    total = preço-(10/100*preço) 
elif opção == 2:
    total = preço-(5/100*preço) 
    print('sua compra de r${:.2f} vai custar r${:.2f} no final.'.format(preço,total)) 

elif opção == 3:
    total = preço
    parcela = total /2
    print('sua compra sera parcelada em 2x de R${:.2f} reais'.format(parcela))
    print('sua compra de R${:.2f} vai custar no final R${:.2f}'.format(preço,total))
elif opção == 4:
    total = preço + (20/100*preço)
    totparc = int(input('quantas parcelas? '))
    parcela = total / totparc
    print('sua compra será parcelada em{}x de r${} com juros'.format(totparc, parcela))
    print('sua compra passará a custar R${:.2f}reais'.format(total))

else:
    print('opção invalida de pagamaento, sua compra ira custar{:.2f}'.format(preço))

