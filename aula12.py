preco = float(input('Qual o preço do produto? '))
desc = preco - (preco * 5 / 100)
print('o produto que custava {} com 5% de desconto agora custa {} reais'.format(preco, desc))