n = soma = cont = 0
while n != 999:
    n = int(input('digite um numero: [999 para parar] '))
    soma += n 
    cont += 1
print(cont - 1 ,soma - 999)

---------------------------------------------
n = s = c = 0
while True:
    n = int(input('digite um valor:'))
    if n == 999:
        break
    c += 1
    s += n
print(f'{c} digitados e soma dele é {s}')

