list_prin =[[], []]
valor = 0
for cont in range (1, 8):
    valor = (int(input(f'Digite o {cont}o. numero: ')))
    if valor % 2 == 0:
        list_prin[0].append(valor)
        list_prin[0].sort()
    else:
        list_prin[1].append(valor)
        list_prin[1].sort()

print(f'Os valores pares digitados foram: {list_prin[0]} ')
print(f'Os valores pares digitados foram: {list_prin[1]} ')



