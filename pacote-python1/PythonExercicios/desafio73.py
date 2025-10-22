times = ('Palmeiras', 'Flamengo', 'Mirassol', 'Botafogo', 'Bahia', 'Fluminense', 'Bragantino', 'Ceará SC',
'Vasco da Gama', 'Chapecoense', 'Grêmio', 'Atlético-MG', 'Internacional', 'Santos', 'EC Vitória', 'Fortaleza',
'Juventude', 'Sport', 'Recife', 'Corinthians')

print('-=' * 40)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 40)
print(f'Os 5 primeiros são: {times[:5]}')
print('-=' * 40)
print(f'Os 4 ultimos são: {times[-4:]}')
print('-=' * 40)
print(f'Time em ordem alfabética: {sorted(times)}')
print('-=' * 40)
print(f'O Chapecoense está na {times.index("Chapecoense")+1} posição')
print('-=' * 40)
