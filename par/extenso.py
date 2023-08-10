cont = ('zero', 'um', 'dois', 'três', 'quatro',
      'cinco', 'seis','sete','oito','nove',
      'dez', 'onze','doze','treze','cartoze',
      'quinze', 'dezesseis','dezessete','dezoito',
      'dezenove','vinte')
while True:
    n = int(input('digite um numero:'))
    if 0 <= n <= 20:
        break
    print('tente novamente.')
print(f'voce digitou o {cont[n]}')
        
