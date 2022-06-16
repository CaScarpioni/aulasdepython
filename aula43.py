peso = float(input('digite seu peso:'))
alt= float(input('digite sua altura: '))
imc = peso / (alt ** 2)

if imc <18.5:
    print('abaixo do peso')
elif imc > 18.6 and imc < 25:
    print('ideal')
elif imc > 25.1 and imc < 30:
    print('sobrepeso')
elif imc > 30.1 and imc < 40:
    print('obeso')
elif imc > 40.1:
    print('obesidade morbida')