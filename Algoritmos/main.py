import time

import random

cem = random.sample(range(0, 999999), 100)
dez_mil = random.sample(range(0, 999999), 10000)
quinhentos_mil = random.sample(range(0, 999999), 500000)
cinquenta_mil = random.sample(range(0, 999999), 50000)
mil = random.sample(range(0, 999999), 1000)
vinte_mil = random.sample(range(0, 999999), 20000)
cem_mil = random.sample(range(0, 999999), 100000)
um_milhao = random.sample(range(0, 9999999), 1000000)
duzentos_mil = random.sample(range(0, 999999), 200000)
cinco_milhoes = random.sample(range(0, 9999999), 5000000)
dois_milhoes = random.sample(range(0, 9999999), 2000000)


def bubbleSort(result):
    for passnum in range(len(result) - 1, 0, -1):
        for i in range(passnum):
            if result[i] > result[i + 1]:
                temp = result[i]
                result[i] = result[i + 1]
                result[i + 1] = temp

def simbora(lista):
    for posicao in range(len(lista)):
        inicio = time.time()
        bubbleSort(lista[posicao])
        fim = time.time()
        print(fim - inicio)

lista = [cem, mil, dez_mil, vinte_mil, cinquenta_mil, cem_mil, duzentos_mil, quinhentos_mil, um_milhao, dois_milhoes, cinco_milhoes]

simbora(lista)
