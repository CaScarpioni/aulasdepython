from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''suas opções:
(0)pedra
(1) papel
(2) tesoura''')
jogador = int(input('qual é a sua jogada?'))
print('-='*11)
print('o computador jogou: {}' .format(itens[computador]))
print('o jogador jogou: {}' .format(itens[jogador]))
print('-='*11)
if computador == 0:
    if jogador == 1:
        print('voce ganhou!')
    elif jogador == 0:
        print('empate')
    elif jogador == 2:
        print('voce perdeu')
    else:
        print('invalido')

elif computador == 1:
    if jogador == 1:
        print('empate')
    elif jogador == 0:
        print('voce perdeu')
    elif jogador == 2:
        print('voce ganhou')
    else:
        print('invalido')

elif computador == 2:

    if jogador == 1:
        print('voce perdeu')
    elif jogador == 0:
        print('ganhou')
    elif jogador == 2:
        print('empate')
    else:
        print('invalido')