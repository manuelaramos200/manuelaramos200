import math


def calcTintas(latas):
    litros = (area / 6) * 1.1
    latas = math.ceil(litros/18)
    custo = latas * 80
    print('-' * 40)
    print(f'Para pintar essa área, Você precisará de {litros:.0f} Litros e equivale a {latas:.0f} latas de 18L, valor a pagar = {custo} ')
    print('-' * 40)


def calcG(galoes):
    litros = (area / 6) * 1.1
    galoes = math.ceil(litros/3.6)
    custo = galoes * 25
    print('-' * 40)
    print(f'Para pintar essa área, Você precisará de {litros:.0f} Litros e equivale a {galoes:.0f} galoes de 3,6L, valor a pagar = {custo} ')
    print('-' * 40)


def calcP(potes):
    litros = (area / 6) * 1.1
    potes = math.ceil(litros/2.4)
    custo = potes * 18
    print('-' * 40)
    print(f'Para pintar essa área, Você precisará de {litros:.0f} Litros e equivale a {potes:.0f} latas de 2,4L, valor a pagar = {custo} ')
    print('-' * 40)


area = int(input('Área da parede: '))
calcTintas(area)
calcG(area)
calcP(area)

