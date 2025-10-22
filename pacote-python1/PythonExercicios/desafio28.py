import random
num = random.randint(0,5)
num_user = int(input('Escreva um numero de 0 a 5 '))
if num_user == num:
    print('Parabens você venceu!')
else:
    print('Voce perdeu!')
    print('O numero era {}'.format(num))