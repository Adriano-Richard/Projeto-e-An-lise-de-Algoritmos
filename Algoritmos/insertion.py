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


def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def simbora(lista):
    for posicao in range(len(lista)):
        inicio = time.time()
        insertionSort(lista[posicao])
        fim = time.time()
        print(fim - inicio)

lista = [cem, mil, dez_mil, vinte_mil, cinquenta_mil, cem_mil, duzentos_mil, quinhentos_mil, um_milhao, dois_milhoes, cinco_milhoes]

simbora(lista)
