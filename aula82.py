num = list()
par = []
impar = []
while True:
    num.append(int(input('Digite um numero:')))
    resp = str(input('Quer continuar?'))
    if resp in 'Nn':
        break
for i,v in enumerate(num):
    if v % 2 ==0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)

print(num)
print(par)
print(impar)