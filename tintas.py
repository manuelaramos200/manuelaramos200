import math


def calcL(area):
    litros = (area / 6) * 1.1
    latas = math.ceil(litros/18)
    custo = latas * 80
    juros = (custo + (custo * 6.5 / 100))/12
    print('-' * 40)
    print(f'Você precisará de {litros:.0f} Litros:\n{latas:.0f}° latas de 18L,')
    print(f'Valor total = R${custo:.2f}')
    print(f'Total à vista em cartão = R${custo:.2f}\n'
          f'Valor Total com 6.5% de juros R${juros * 12:.2f}\n'
          f'  Parcelado em 12X = R${juros:.2f}\n'
          f'valor via Pix = R${custo - (custo * 15/100)}')
    print('-' * 40)


def calcG(area):
    litros = (area / 6) * 1.1
    galoes = math.ceil(litros/3.6)
    custo = galoes * 25
    juros = (custo + (custo * 6.5 / 100)) / 12
    print('-' * 40)
    print(f'Você precisará de {litros:.0f} Litros e equivale a {galoes:.0f}° Galoes de 3,6L,')
    print(f'Valor total = R${custo:.2f}')
    print(f'Total à vista em cartão = R${custo:.2f}\n'
          f'Valor Total com 6.5% de juros R${juros * 12:.2f}\n'
          f'  Parcelado em 12X = R${juros:.2f}\n'
          f'valor via Pix = R${custo - (custo * 15 / 100)}')
    print('-' * 40)


def calcP(area):
    litros = (area / 6) * 1.1
    potes = math.ceil(litros/2.4)
    custo = potes * 18
    juros = (custo + (custo * 6.5 / 100)) / 12
    print('-' * 40)
    print(f'Você precisará de {litros:.0f} Litros e equivale a {potes:.0f}° Potes de 2,4L')
    print(f'Valor Total = R${custo:.2f}')
    print(f'Total à vista em cartão = R${custo:.2f}\n'
          f'Valor Total com 6.5% de juros R${juros * 12:.2f}\n'
          f' Parcelado em 12X = R${juros:.2f}\n'
          f'valor via Pix = R${custo - (custo * 15 / 100)}')
    print('-' * 40)

def calcMistura(area):
    litros = (area / 6) * 1.1
    latas = math.floor(litros / 18)
    sobraL = litros- (latas * 18)

    galoes = math.floor(sobraL / 3.6)
    sobraG = sobraL - (galoes * 3.6)

    potes = math.ceil(sobraG / 2.4)
    custoTot= ((latas * 80) + (galoes * 25) + (potes * 18))
    juros = (custoTot + (custoTot * 6.5 / 100)) / 12

    print('-' * 40)
    print(f'Você precisará de {litros:.0f} Litros e equivale a {latas}° latas, {galoes}° galoes, {potes:.0f}° Potes de 2,4L')
    print(f'Valor Total = R${custoTot:.2f}')
    print(f'Total à vista em cartão = R${custoTot:.2f}\n'
          f'Valor Total com 6.5% de juros R${juros * 12:.2f}\n'
          f' Parcelado em 12X = R${juros:.2f}\n'
          f'valor via Pix = R${custoTot - (custoTot * 15 / 100)}')
    print('-' * 40)


area = int(input('Área da parede: '))
calcL(area)
calcG(area)
calcP(area)
calcMistura(area)


