ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
print(ficha)
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(ficha): #indice e valores
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}') #indice, valor na primeira posição, valor na ultima posição (8 posições sendo 1 decimal)
while True:
    print('=' * 30)
    opc = int(input('Mostrar notas de qual aluno? [999 para parar] '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1: # se o numero digitado for menor do que a qtd de alunos cadastrados (-1 pq o primeiro é 0)
        print(f'Notas do aluno {ficha[opc][0]} são {ficha[opc][1]}') #Pega dentro da lista o valor pelo codigo que foi passado
print('<<<VOLTE SEMPRE>>>')
