num = list()
while True:
    n = int(input('Digite um valor'))
    if n not in num:
        num.append(n)
        print('Valor adicionado')
    else:
        print('valor duplicado')
    r = str(input('Quer continuar?'))
    if r in 'Nn':
        break

num.sort()
print(f'Voce digitiou os valores {num}')