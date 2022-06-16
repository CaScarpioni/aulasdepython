from termios import NCCS


num = int(input('digite um numero:'))
for c in range ( 1, num+1):
    if num % c ==0:
        print(end='')
    else:
        
    print('{}'.format(c), end='')