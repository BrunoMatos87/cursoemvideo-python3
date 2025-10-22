matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_par = maior = soma_3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz [l][c] = int(input(f'Digite um valor para [{l}.{c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz [l][c] % 2 == 0:
            soma_par += matriz [l][c]
        if c == 2:
            soma_3 = soma_3 + matriz [l][c]
        if l == 1:
            if matriz [l][c] > maior:
                maior = matriz [l][c]
    print()
print('-=' * 30)
print(f'A soma de todos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_3}')
print(f'O maior valor da segunda linha é {maior}')


