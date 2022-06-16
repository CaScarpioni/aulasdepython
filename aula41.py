nasc=int(input("digite o ano de nascimento: "))
ano = int (input("digite o ano atual: "))

idade = ano - nasc

if idade <= 9:
    print('mirim')
elif idade >= 10 and idade<= 14:
    
    print('infantil')
elif idade >= 15 and idade<= 19:
    print('junior')
elif idade == 20:
    print('senior')
elif idade >= 21:
    print('master')