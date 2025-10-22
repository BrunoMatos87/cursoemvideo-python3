from random import randint
from time import sleep
from operator import itemgetter # importar para colocar o rankin a posição crescente
jogo = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
ranking = list()
print('Valores sorteados')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #coloca em ordem de valores por ser a chave 1 se fosse 0 seria por chavez
print('-=' * 25)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking): #o dicionario gera uma lista por isso a busca por valor no enumerate
    print(f'   {i+1}º lugar: {v[0]} com {v[1]} no dado. ')  # Pega o indice +1 para não começão com 0 an posição depois pega o primeiro valor e segundo valor
    sleep(1)



