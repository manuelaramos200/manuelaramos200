from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor'))
    computador = randint(0,10)
    total = computador + jogador 
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar[P/I]')).strip().upper()[0]
    print(f'voce jogou {jogador} e eu joguei {computador} e o total é {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print( 'VOCE VENCEU')
            v += 1
        else:
            print('VOCE PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU')
            v += 1
        else:
            print('VOCE PERDEU')
            break
print('Vamos Jogar Novamente')
print(f'GAME OVER, Voce Ganhou {v}x')
