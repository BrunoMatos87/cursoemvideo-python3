nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua nota foi {}. Você esta REPROVADO!'.format(media))
elif (media >= 5 and media < 7):
    print('Sua nota foi {}. Você esta RECUPERAÇÃO!'.format(media))
elif media >= 7:
    print('Sua nota foi {}. Você esta APROVADO!'.format(media))