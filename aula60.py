num=int(input('digite um número para ver o fatorial:'))
cont=num
f = 1
while cont > 0:
    print('{} '.format(cont), end='')
    print(' x ' if cont > 1 else '=', end='')
    f = f * cont
    cont = cont - 1

    
print(f)