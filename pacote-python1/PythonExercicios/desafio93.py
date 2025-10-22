jogador = dict()
partidas = list()

jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partida {jogador["nome"]} jogou? '))
for n in range(0, tot):
    partidas.append(int(input(f'  Quantos gols na partida {n}? ')))
jogador['gols'] = partidas[:] #faz uma copia da lista e joga no dicionario
jogador['total'] = sum(partidas)
print('-=' *30)
print(jogador)
print('-' * 30)
for k, v in jogador.items():
    print(f'   {k} tem o valor {v}')
print('-=' *30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):# pegar a lista que foi copiada
    print(f'   => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')



