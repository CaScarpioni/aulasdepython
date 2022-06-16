print('{:=^40}'.format ('LOJA DA CAMILA'))
valor = float(input('digite o valor da compra: '))
print('''FORMAS DE PAGAMENTO
(1)a vista dinheiro
(2) a vista cartao
(3) 2x cartao
(4) 3 vezes cartao''')

opção = int(input('qual o pagamento?'))

if opção ==1:
    total = valor - (valor * 10/100)
elif opção == 2:
    total = valor - (valor * 5/100)
elif opção ==3:
    total = valor
    print('sua compra será parcelada em 2x')
elif opção == 4:
    total = valor + (valor * 20 / 100)
    totalparc = int(input('quantas parcelas'))
    parcela = total / totalparc
    print('Sera parcelado em', (totalparc), "aprcelas de {}".format(parcela))
else:
    print( 'invalido')


print('o valor da sua compra foi de {}'.format(total))


