num1 = 0
num2 = 0
resultado = 0
menu = 0
while menu != 5:
    num1 = int(input('Digite o primeiro numero: '))
    num2 = int(input('Digite o segundo numero: '))
    print('''MENU:
        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos numeros
        [ 5 ] sair do programa
        ''')
    menu = int(input('Qaul opção deseja escolher: '))

    if menu == 1:
        resultado = num1 + num2
        print('A Soma dos numeros é: {}'.format(resultado))
    elif menu == 2:
        resultado = num1 * num2
        print('A multiplicação dos numeros é: {}'.format(resultado))
    elif menu == 3:
        if num1 > num2:
            resultado = num1
        else:
            resultado = num2
        print('O numero maior é o {}'.format(resultado))
    elif menu == 4:
        print('Digite novos números')
print('FIM')