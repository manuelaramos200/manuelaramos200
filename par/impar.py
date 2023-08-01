from random import randint
v = 0
while True:
    computador = randint(0,10)
    jogador = int(input('digite um valor: '))
    soma = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('PAR OU IMPAR [P/I]:')).strip().upper()[0]
        print(f' voce jogou {jogador}, eu pensei { computador} e o total é {soma}')
        print('DEU PAR' if soma % 2 == 0 else 'DEU IMPAR')
        if tipo == 'P':
            if soma % 2 == 0:
                print('voce venceu')
                v += 1
            else:
                print('voce perdeu')
                break
        elif tipo == 'I':
            if soma % 2 == 1:
                print('voce venceu')
                v += 1
            else: 
                print('voce perdeu')
                break
    print('vamos jogar novamente')
print(f'GAME OVER, voce ganho {v}x')
            


