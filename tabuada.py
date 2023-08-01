tabuada = cont = 1

while True:
    tabuada = int(input('qual tabuada você deseja ver?'))
    if tabuada >= 1:
        if cont < 10:
            cont *= tabuada
            print(tabuada,cont)
