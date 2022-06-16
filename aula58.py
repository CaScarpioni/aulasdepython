from random import randint

soma=0
print('Vou pensar em um numero: adivinhe...')
n=randint(0,10)
num=0
while num != n:
    num=int(input('digite: '))
    print('voce errou')
    soma += 1

print('correto')
print(f'voce errou {soma} vezes!')
