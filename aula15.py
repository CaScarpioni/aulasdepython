aluguel = int(input('quantos dias ficou com o carro? '))
km = float(input('quantos km foi utilizado? '))
preco = (aluguel * 60) + (km * 0.15)
print('o preço sera {:.2f}'.format(preco))
