ano= int(input("digite o ano atual: "))
nasc = int(input("digite o ano de nascimento"))

idade= ano - nasc


if idade == 18:
    print('você precisa de alistar')
elif idade > 18:
    idade = idade - 18
    print('você está {} anos atrasado para se alistar' .format(idade))
elif idade < 18:
    idade = 18 - idade
    print ('faltam {} anos para voce se alistar'.format(idade))

