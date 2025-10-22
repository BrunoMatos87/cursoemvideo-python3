from random import randint
computador = randint(0, 10)
print('Sou um computador... Acabei de pensar em um numeo de 0e 10.')
print('Sera que você consegue adivinhar?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Digite o seu palpite: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
print('Acertou com {} palpites.'.format(palpites))