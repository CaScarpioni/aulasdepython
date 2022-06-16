nome = str(input("qual é seu nome? "))
if nome == "camila":
    print("que nome bonito!!")
elif nome == "maggie":
    print("oi princesa")
elif nome in 'Ana claudia, juliana, sofia':
    print('Amei os nomes')
print('tenha um bom dia {}'.format(nome))