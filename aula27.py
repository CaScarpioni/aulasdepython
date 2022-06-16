nome = str(input("digite seu nome: ")).strip()
n = nome.split()

print('muito prazer {}!' .format(nome))
print('seu primeiro nome é {}' . format(n[0]))
print('seu ultimo nome é {}' . format(n[len(n)-1]))