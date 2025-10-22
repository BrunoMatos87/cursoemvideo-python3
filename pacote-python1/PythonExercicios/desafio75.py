num_tupla = ()
pares = ()
for c in range (0, 4):
    numero = int(input('Digite um valor: '))
    num_tupla = num_tupla + (numero,)
    if numero % 2 == 0:
        pares += (numero,)
print(f'O número 9 apareceu {num_tupla.count(9)} vezes.')
if 3 in num_tupla:
    print(f'O valor 3 esta na {num_tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print(f'Os números pares foram: {pares}')


