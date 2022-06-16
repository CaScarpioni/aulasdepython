num = []
maior = 0
men = 0
for c in range(0,5):
    num.append(int(input('Digite um numero')))
    if c == 0:
        mai = men = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < men:
            men = num[c]

print(f'voce digitou os valores{num}')
print(f'O maior {maior} e menor {men}')
