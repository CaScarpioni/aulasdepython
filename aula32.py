ano = int(input('Digite um ano: '))

if ano % ano == 0  and ano %100 !=0 or ano % 400 == 0:
    print('ele é bissexto')
else:
    print('Ele é normal')