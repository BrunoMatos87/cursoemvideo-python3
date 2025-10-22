jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partida {jogador["nome"]} jogou? '))
    partidas.clear()
    for n in range(0, tot):
        partidas.append(int(input(f'  Quantos gols na partida {n+1}? ')))
    jogador['gols'] = partidas[:] #faz uma copia da lista e joga no dicionario
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod', end=' ')
for i in jogador.keys(): #criando cabeçalho
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time): #indice e valores da lista
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    print('=' * 30)
    opc = int(input('Mostrar dados de qual jogador? [999 para parar] '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc >= len(time):
        print(f'ERRO! Não existe jpgador com código {opc}')
    else:
        print(F'<<<LEVANTAMENTO DO JOGADOR {time[opc]["nome"]}>>>') #busca na lista time o valor  do indice e busca nome
        for i, g in enumerate(time[opc]['gols']): # busca na lista time peli balor do indice no campo gol
            print(f'   No jogo {i+1} fez {g} gols')
    print('-' * 40)
print('<<<FIM>>')