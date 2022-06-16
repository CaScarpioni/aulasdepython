palavra = ('camila', 'maggie', 'estudar', 'aprender')

for p in palavra:
    print(f'\n na palava {p.upper()} temos:', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')