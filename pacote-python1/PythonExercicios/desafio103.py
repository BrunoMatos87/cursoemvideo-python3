def ficha(jogador='<desconhecido>', gol=0):
    print(f'O jogador {jogador} fez {gol}(s) no campeonato')


jogador = str(input('Digite o nome do jogador: '))
gols = str(input('Digite a quantidade de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if jogador.strip() == '':
    ficha(gol=gols)
else:
    ficha(jogador, gols)