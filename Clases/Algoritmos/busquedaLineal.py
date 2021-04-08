def busquedaLineal (lista, encontrar):
    isInList = False
    for elemento in lista:
        if elemento == encontrar:
            isInList = True
    return isInList

listaEntrada = [2,12,34,5,11,59,4,3,1]
valorEncontrar = int(input("por favor ingrese un número: "))
listaEntrada.sort()
print(busquedaLineal(listaEntrada, valorEncontrar))
import busquedabinaria as bi
import time
import random as rd
listaEntrada = []
for i in range (6645):
    listaEntrada.append(rd.randint(1,100000))
encontrar = 59
listaEntrada.sort()
inicio = time.time()
busquedaLineal(listaEntrada, encontrar)
deltaLineal = time.time() - inicio
inicio = time.time()
bi.busquedabinaria(listaEntrada, encontrar)
deltaBinario = time.time() - inicio
print(deltaBinario, deltaLineal)