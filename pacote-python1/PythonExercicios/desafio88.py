import random
from time import sleep
temp = []
lista = []
print('='*30)
print('{:^30}'.format('JOGOS DA MEGA SENA'))
print('='*30)

jogo = int(input('Quantos jogos você quer que eu sorteie? '))
print('-='*3, f'Sorteado {jogo} jogos', '-='*3)
for c in range(0, jogo):
    temp.append(random.choices(range(1, 60), k=6))
    lista.append(temp[:])
    temp.clear()
for c in range(0, len(lista)):
    print(f'Jogo {c+1}: {lista[c]}')
    sleep(1)
print('-=' * 5, 'BOA SORTE', '-=' * 5)