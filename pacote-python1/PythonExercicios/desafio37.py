num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL 
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('Sua escolha: '))

if opcao == 1:
    print('A conversão binaria é {}'.format(bin(num)[2:]))
elif opcao == 2:
    print('A conversão octal é {}'.format(oct(num)[2:]))
elif opcao == 3:
    print('A conversão hexadecimal é {}'.format(hex(num)[2:]))
else:
    print('Você digitou errado')