from random import randint
contador = 0

print('=-' * 14)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 14)

while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    par_impar = ' '
    while par_impar not in 'PpIi':
        par_impar = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o compuador jogou {computador}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÌMPAR')
    if (par_impar == 'P'):
        if total % 2 == 0:
            print('Você VENCEU!')
            contador += 1
        else:
            print('Você PERDEU!')
            break
    elif (par_impar == 'I'):
        if total % 2 == 1:
            print('Você VENCEU!')
            contador += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
    print('-=' * 40)
print(f'Game Over! Você venceu {contador} vezes')