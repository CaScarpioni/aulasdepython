num = (int(input('Numero:')),
    int(input('Numero:')),
    int(input('Numero:')),
    int(input('Numero:')))

print(num.index(3))
print(num.count(9))

for n in num:
    if n % 2 ==0:
        print(n)