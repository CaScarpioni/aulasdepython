sal = float(input('Qual o salario do funcionario? $'))
porc = float(input('qual a % do reajuste? '))
ajuste = sal + (sal * porc / 100 )
print('o funcionario que recebia {:.2f} reais, agora com o reajuste recebe {:.2f}'.format(sal, ajuste))