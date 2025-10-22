soma_total = 0
cont = 0
for numero in range (1,501, 2):
    if numero % 3 == 0:
        cont += 1
        soma_total += numero
print('A soma de todos os {} os valores é {}'.format(cont, soma_total, end = ' '))