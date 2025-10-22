frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() ##separar palavras
junto = ''.join(palavras) ##junta todas as palavras
inverso = ''
for letra in range (len(junto) - 1, -1, -1): ## qtd de letra, - 1 pq vai ate a penultima, -1 anda de tras pra frente
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')



