expr = str(input('Digite sua expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(') #adiciona na lista para verificar que abriu uma expressao
    elif simb == ')': #verifica se tbm tem parentese fechando
        if len(pilha) > 0:
            pilha.pop() #se existir aberto e fechado ele remove os 2
        else:
            pilha.append(')') # se nao ele add na lista pra mostrar que não eiste par
            break
if len(pilha) == 0: # se a lista nao estiver vazia é sinal que nao fechou o par de parenteses
    print('Sua expressão esta válida')
else:
    print('Sua expressão esta errada')