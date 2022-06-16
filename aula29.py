vel = float(input('Digite a velocidade: '))

if vel >80:

    multa = 7 * (vel - 80)
    print('multado!, sua multa foi de {:.2f}' .format (multa))

else:
    print('está dentro da velocidade')