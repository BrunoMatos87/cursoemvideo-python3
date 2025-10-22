peso_maior = 0
peso_menor = 0
for pessoa in range (1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > peso_maior:
            peso_maior = peso
        if peso < menor:
            peso_menor = peso
print('Peso maior é {}Kg, e o peso menor é {}Kg'.format(peso_maior, peso_menor))