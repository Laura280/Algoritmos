import time
import ordenamiento_burbuja as ob
import ordenamiento_insercion 
import random as r

lista = []
for i in range (1200):
    lista.append(r.randint (1,10000))
listaCopia = lista.copy()

#--- INICIO ---#
inicio = time.time()
#---INSTRUCCIONES ---#
ob.ordenamientoBurbuja(lista)
#--- DELTA ---#
deltaOb = time.time() - inicio

#--- INICIO ---#
inicio = time.time()
#---INSTRUCCIONES ---#
listaCopia.sort()
#--- DELTA ---#
deltaSort = time.time() - inicio

print(deltaOb)
print(deltaSort)
print(deltaSort >= deltaOb)