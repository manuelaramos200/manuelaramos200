valor = int(input('qual será o valor a ser sacado: R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced: #quantas x consegue tirar do o valor do total 
        total -= ced
        totced += 1
    else:
        if totced > 0: # mostrar as notas maiores que 0
            print(f'total de {totced} de R$ {ced}')
        if ced == 50: # tira ate 50 e sucessivamente 
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if ced == 0:
            break
        
