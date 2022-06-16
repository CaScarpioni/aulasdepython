
print ('Calculadora')

op=0
num1=int(input('Digite o primeiro valor: '))
num2=int(input('Digite o segundo valor: '))

while True:
    print('Bem vindo!')
    print('DIGITE PARA:')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Novos numeros')
    print('[5] Sair')
    op=int(input('Digite sua escolha: '))
    if op ==1:
        print(f"A soma entre {num1}+{num2}={num1+num2}")
    elif op == 2:
        print(f"A Multiplicação entre {num1}*{num2}={num1*num2}")
    elif op ==3:
        if num1>num2:
            print(f'numero {num1} é maior que {num2}')
        else:
            print(f'numero {num2} é maior que {num1}')
    elif op == 4:
        num1=int(input('Digite o primeiro valor: '))
        num2=int(input('Digite o segundo valor: '))
    elif op ==5:
        break
print('Acabou')