n1 = float(input('primeiro segmento: '))
n2 = float(input('segundo segmento: '))
n3 = float(input('terceiro segmento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('podem formar um triangulo!', end="")
    if n1 == n2 and n2 == n3 and n1==n3:
        print('equilatero')
    elif n1!= n2 and n2!=n3 and n1!=n3:
        print('escaleno')
    else:
        print('isoceles') 


else:
    print('Ele NÃO pode formar triangulo')

    