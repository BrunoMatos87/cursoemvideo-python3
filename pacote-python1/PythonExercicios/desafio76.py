lista_produtos = ('Lapis', 1.75, 'Borracha', 2.00, 'Caderno', 15.9, 'Estojo', 25.00)
print('-' * 40)
print('{:^40}'.format('LISTA DE PREÇO'))
print('-' * 40)
for pos in range(0, len(lista_produtos)):
    if pos % 2 == 0:
        print(f'{lista_produtos[pos]:.<30}', end='') #alinha com pontos a esquerda <
    else:
        print(f'R${lista_produtos[pos]:>7.2f}') # alinha para direita


