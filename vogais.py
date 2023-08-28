palavras = ('curso','gratis','aprender',
            'estudar', 'copiar', 'ler')
for p in palavras:
    print(f'Na palavra {p.upper()}')
    for letras in p:
        if letras.lower() in 'aeiou':
            print(letras)
