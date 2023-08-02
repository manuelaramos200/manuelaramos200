total = cont = m = f =  0
while True:
        idade = int(input('IDADE:'))
        sexo = ' '
        while sexo not in 'MF':
            sexo = str(input('SEXO:')).strip().upper()[0]
        if idade >= 18:
            cont +=1
        if sexo in 'Mn':
            m += 1
        if sexo in 'Ff'and idade < 20:
                f += 1
        pergunta = ' '
        while pergunta not in 'SN':           
            pergunta = str(input('Quer continuar?[N/S]?')).strip().upper()[0]
        if pergunta == 'N':
            break
print(f'Total de {cont }pessoa com mais de 18 anos')
print(f'Ao todo temos {m} Homens Cadastrados')
print(f'temos {f} Mulheres com menor de 20 anos')
