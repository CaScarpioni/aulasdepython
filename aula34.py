sal = float(input('Digite seu salario: '))

if sal >=1250:
    novosal= sal + ((sal/100)*10)
    print('Novo salario de {}'.format(novosal))
else:
    novosal= sal + ((sal/100)*15)
    print('Novo salario de {}'.format(novosal))