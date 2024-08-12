import math


def calcTintas(area):
    litros = (area / 6) * 1.1
    latas = math.ceil(litros/18)
    custo = latas * 80
    print('-' * 40)
    print(f'Você precisará de {litros:.0f} Litros:\n{latas:.0f} latas de 18L,')
    print(f'Total à vista em cartão = R${custo}\n'
          f'Parcelado em 12X = R${(custo + (custo * 6.5 / 100))/12:.2f}\n'
          f'valor via Pix = R${custo - (custo * 15/100)}')
    print('-' * 40)


def calcG(area):
    litros = (area / 6) * 1.1
    galoes = math.ceil(litros/3.6)
    custo = galoes * 25
    print('-' * 40)
    print(f'Você precisará de {litros:.0f} Litros e equivale a {galoes:.0f} Galoes de 3,6L,')
    print(f'Total à vista em cartão = R${custo}\n'
          f'Parcelado em 12X = R${(custo + (custo * 3.6 / 100)) / 12:.2f}\n'
          f'valor via Pix = R${custo - (custo * 15 / 100)}')
    print('-' * 40)


def calcP(area):
    litros = (area / 6) * 1.1
    potes = math.ceil(litros/2.4)
    custo = potes * 18
    print('-' * 40)
    print(f'Você precisará de {litros:.0f} Litros e equivale a {potes:.0f} Potes de 2,4L, ')
    print(f'Total à vista em cartão = R${custo}\n'
          f'Parcelado em 12X = R${custo + (custo * 2.4 / 100)/12:.2f}'
          f'valor via Pix = R${custo - (custo * 15 / 100)}')
    print('-' * 40)

def calcMistura(area):

    



area = int(input('Área da parede: '))
calcTintas(area)
calcG(area)
calcP(area)
calcMistura(area)

