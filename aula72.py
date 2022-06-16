lista = ('zero', 'um', 'dois', 'tres', 'quatro','cinco')
num = 90
while True:
    num = int(input('Digite um numero inteiro'))
    if num < 0 or num >5:
        print('digite novamente')
    else:
        print(lista[num])