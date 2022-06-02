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


def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark


def simbora(lista):
    for posicao in range(len(lista)):
        inicio = time.time()
        quickSort(lista[posicao])
        fim = time.time()
        print(fim - inicio)

lista = [cem, mil, dez_mil, vinte_mil, cinquenta_mil, cem_mil, duzentos_mil, quinhentos_mil, um_milhao, dois_milhoes, cinco_milhoes]

simbora(lista)

