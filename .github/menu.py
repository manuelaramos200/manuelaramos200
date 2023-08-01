n1 = int(input('1° numero:'))
n2 = int(input('2° numero:'))
opcao = 0

while opcao != 5:
    print('''[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5] sair do programa''')
    opcao = int(input('qual sua opção?'))
    if opcao == 1:
        soma = n1 + n2
        print('soma de {} + {} = {}'.format(n1,n2,soma))
    elif opcao == 2:
        mult = n1 * n2
        print('a multiplicação de {} x {} = {}'.format(n1,n2,mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
            print('entre {} e {} o maior numero é {}'.format(n1,maior))
    elif opcao == 4:
        n1 = int(input('1° valor:'))
        n2 = int(input('2° valor'))
    elif opcao == 5:
       print('voce saiu')
       
    else:
        print('opcão invalida, tente novamente')

