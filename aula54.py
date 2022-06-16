soma = 0
pessoas=0
menores=0
for c in range (1, 7):
    ano=int(input('digite o ano:'))
    soma = 2022 - ano
    if soma <18:
        print('de menor')
        menores= menores + 1
    elif soma >=18:
        print('de maior')
        pessoas = pessoas + 1
print(' de menor:', (menores), 'de maior:', (pessoas))