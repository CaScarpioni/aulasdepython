soma=0
for c in range (1, 7):
    num = int(input('digite um valor'))
    if num % 2 == 0:
        soma = soma + num
    else:
        print('impar')
print(soma)