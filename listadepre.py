lista = ('lapis',1.50,
        'borracha',0.50,
        'apontador',2.00,
        'caderno',25.00,
        'caneta',3,00)
for pos in range(0,len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R${lista[pos]:>7.2f}')

        
