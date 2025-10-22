nome = str(input('Digite seu nome: ')).strip()
primeiro = nome.split()[0]
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))
print(len(primeiro))
