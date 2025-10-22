import random
lista_numero = random.choices(range(1, 10), k=5)
tp_num = tuple(lista_numero)
print(tp_num)
print(f'O valor maior é {max(tp_num)}')
print(f'O valor menor é {min(tp_num)}')




