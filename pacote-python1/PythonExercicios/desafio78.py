valores = []
maior = menor = 0
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0:
        maior = menor = valores[cont]
    else:
        if valores[cont] > maior: #Verifica se o valor na posição do contador é maior
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]

print('=-=' * 15)
print(f'Voce digitou os valores {valores}')
print(f'O maior valor foi {maior} nas posições ', end='') # end serve para continuar sem quebrar linha
for i, v in enumerate(valores): # indice e valor, varifica na lista
    if v == maior: # se o valor é maior
        print(f' {i}...', end = ' ') # add o valor do indice para saber a posição do valor
print()
print(f'O menor valor foi {menor} nas posições', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f' {i}...', end = ' ')


