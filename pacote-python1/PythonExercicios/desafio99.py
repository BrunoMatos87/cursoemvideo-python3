from time import sleep
def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...', flush=True)
    for valor in num:
        print(valor, end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior += valor
        else:
            if maior > valor:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo', flush=True)
    print(f'O maior valor informado foi {maior}', flush=True)
maior(2,3,4,5,6,7,8,9)
maior(4, 7 , 0)
maior(2, 1)
maior(6)
maior()
