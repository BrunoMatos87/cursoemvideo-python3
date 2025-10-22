valores = list()
par = list()
impar = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input( 'Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A Lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de ìmpares é {impar}')
