
duração=float[] #duração dos filmes
cont=0 #contador de dias
dias=0 #dias para assistir os filmes
corr= 0 #correção do número

while cont != 5: 
    cont += 1
    duração=float(input(f"Digite a duração do {cont}º filme: "))
    while True:
        if duração < 1.01 or duração >1.80:
            print('A duração não pode ser menor que 1.01 horas ou maior que 3 horas, digite novamente o valor:')
            corr=float(input('Digite Novamente entre 1.01 horas até 3 horas:'))
            duração[cont]=corr #duração nova será corrigida no número do contador com a nova variavel corr (correção do numero)
            if corr > 1.01 or corr<1.80:
                break
        else:
            break

media = sum(duração) / 1.80
media = ceil(media)

print(f'Ana vai demorar {media} dias para assistir a esses filmes!')

print('Fim do exercício')