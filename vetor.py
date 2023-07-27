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
            
    
