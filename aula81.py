valores = []
while True:
    valores.append(int(input('Digite um valor:')))
    resp = str(input('Quer continuar?'))
    if resp in 'Nn':
        break
valores.sort(reverse=True)
print(f'Voce digitou {len(valores)} elementos')
if 5 in valores:
    print('O valor faz parte da lista')
else:
    print('O 5 nao faz parte da lista')
