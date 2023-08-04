totcompra = maiormil = menor = cont = 0
barato = ''
while True:
    nome = str(input('Qual o nome do produto: '))
    preco = int(input('Qual o preço do produto: '))
    totcompra += preco
    cont +=1
    if preco > 1000:
        maiormil += 1
    if cont == 1 or preco < menor :
        menor = preco
        barato = nome
    conti = ' '
    while conti not in 'SN':
        conti = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    if conti == 'N':
        break
print(f'O total da compra foi R${totcompra}')
print(f'{maiormil} Produtos custaram mais de R$1000 ')
print(f' o {barato} mais barato custour {menor}')
