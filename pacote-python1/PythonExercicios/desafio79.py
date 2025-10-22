valores = list()
while True:
    num = int(input('Digite um valor: '))
    if num not in valores: # o valor digitado não estiver na lista
        valores.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 30)
valores.sort()
print(f'Voce digitou os valores {valores}')