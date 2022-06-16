sexo = "a"
while sexo!='M' and sexo!="F":
    sexo = str(input("digite se é F ou M:   ")).upper()
    if sexo == "F" and sexo== "M":
        break
    else:
        print('digitou errado')
print('fim')