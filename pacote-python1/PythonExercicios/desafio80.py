lista = []
for c in range(0, 5):
    numero = int(input('Digite um valor: '))
    if c == 0 or numero > lista[-1]:#se o contador foi a primeira vez, ele add como primeiro valor an lista
        lista.append(numero)#ou se o numero for maior que o ultimo elemento da lista[(len(lista)-1)] faz a mesma coisa
        print('Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(lista): #percorre a lista da posição 0 ate a ultima posição da lista
            if numero <= lista[posicao]: #verifica em cada posição da lista se o numero é menor ou igua a ele
                lista.insert(posicao, numero)  #na posicao que for menor ou igual ele ibnsere o valor
                print(f'Adicionado na posição {posicao} da lista...')
                break
            posicao += 1 #para pegar a proxima posição
print('-=' * 30)
print(f'Os valores digitados em ordem foram{lista}')