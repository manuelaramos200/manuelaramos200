while True:
    tabuada = int(input('qual tabuada você deseja ver?'))
    if tabuada < 0:
        break
    for cont in range(1,11):
            print(f'{tabuada}x{cont}={tabuada*cont}')
print('tabuada finalizada')
