from random import randint

print('Vou pensar em um numero: adivinhe...')

n=randint(0,5)

num= int(input('Qual numero eu pensei? '))
print('PROCESSANDO...')


if num == n:
    print('Parabens, voce adivinhou')
else:
    print('você errou')