lista = ('lapis', 1.75, 
'borracha', 2,
'mochila', 30,
'estojo', 7)

for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<20}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')