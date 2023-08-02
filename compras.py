totcompra = maiormil = menor = 0
while True:
    nome = str(input('Qual o nome do produto: '))
    preco = int(input('Qual o preço do produto: '))
    totcompra += preco
    conti = ' '
    if preco > 1000:
        maiormil += 1
    if preco == 1:
        menor = nome
    else:
        preco == menor
        menor = nome
    while conti not in 'SN':
        conti = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    if conti == 'N':
        break
print(f'O total da compra foi R${totcompra}')
print(f'{maiormil} Produtos custaram mais de R$1000 ')
print(f' o {menor} que foi mais barato')
