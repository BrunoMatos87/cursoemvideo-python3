soma_pares = 0
for c in range (1, 7):
    numero = int(input('Digite um valor: '))
    if numero % 2 == 0:
        soma_pares += numero  # Adiciona o número à soma se for par
print('A soma de todos números pares é {}'.format(soma_pares))
