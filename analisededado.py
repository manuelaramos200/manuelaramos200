n = (int(input('digite um numero: ')),
    int(input('digite um numero:')),
    int(input('digite um numero:')),
    int(input('digite outro numero:')))
print(f'voce digitou os valores{n}')
print(f'o valor 9 apareceu {n.count(9)}')
if 3 in n:
  print(f'o valor 3 apareceu na {n.index(3)+1}° posição')
else:
     print('o valor 3 não foi digitado')
print('os valoresd pares digitador foram')
for num in n:
    if num % 2 == 0:
        print(num)

