
somaidade=0
mediaidade=0
maioridadehomem=0
nomevelho=''
totmulher20 = 0
for p in range (1,5):
    nome=str(input('nome:'))
    idade = int(input('idade'))
    sexo = str(input('sexo f ou m'))
    somaidade += idade
    if p ==1 and sexo in 'Mm':
        maioridadehomem=idade
        nomevelho=nome
    if sexo in "Mn" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1

mediaidade = somaidade/4
print('media de idade:', mediaidade)
print('O homem mais velho tem {} e se chama {}'.format(maioridadehomem,nomevelho))
print('total de mulher menos de 20 anos', (totmulher20))