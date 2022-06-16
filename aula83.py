ex  = str(input('digite uma expressao'))
pilha = []

for simb in ex:
    if simb == '(':
        pilha.append('(')

    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0 :
    print('Valida')
else:
    print('errada')