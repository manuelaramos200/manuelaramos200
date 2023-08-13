time = 'Atletico','São Paulo','Corinthians','Flamengo','Sport','Santa cruz','Chapecoense','Palmeiras'
print(f'lista dos times do Brasileirão:{time}')
print(f'os 5 primeiros colocados são:{time[0:5]}')
print(f'os 4 ultimos são:{time[-4:]}')
print(f'times em ordem alfabetica{(sorted(time))}')
print(f'Chapecoense esta na {time.index("Chapecoense")+1}')
