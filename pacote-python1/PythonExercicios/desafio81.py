valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input( 'Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print(f'O Valor 5 esta na lista')
else:
    print(f'O Valor 5 NÂO esta na lista')
