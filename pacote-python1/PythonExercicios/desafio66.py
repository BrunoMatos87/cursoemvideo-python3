s = qtd = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
       break
    s += n
    qtd += 1
print(f'A soma dos vale {s} e foram digitados {qtd} numeros')