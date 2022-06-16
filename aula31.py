dist=float(input('digite a distância: '))

if dist <= 200:
    prec= dist * 0.50
    print('O valor da sua viagem é de: R${:.2f}' . format(prec))
else:
    prec = dist * 0.45
    print('O valor da sua viagem é de: R${:.2f}' . format(prec))