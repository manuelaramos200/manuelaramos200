resp = 'S'
n = quant = media = soma = menor = maior = 0
while resp in 'Ss':
    n = int(input('digite um numero:'))
    soma += n
    quant += 1
    media =  soma / quant
    if quant == 1:
        maior = menor = n
    else: 
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('deseja continuar [S/N]:')).upper().strip()[0]
print('voce digitou {} numero e media foi {}'.format(quant,media))
print( 'o maior valor é {} o menor valor é {}'.format(maior,menor))
print('acabou')
------------------------------------------------------------------
n = cont = soma = media = menor = maior = 0
c = 'S/N'
while c not in 'Nn':
    n = int(input('digite um numero:'))
    c= str(input(' quer continuar: [S/N]')).upper()
    cont += 1
    soma += n 
    media = soma / cont
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(cont,maior,menor,soma,media)
            
    
