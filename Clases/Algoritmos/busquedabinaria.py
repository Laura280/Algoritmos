def busquedabinaria(lista,encontrar):
    """Busqueda binaria
    se ingresa una lista y un valor a encontrar
    y entonces se devuele si lo encontró o no
    """
    isInList = False
    lista.sort()
    izq= 0
    der = len(lista)-1
    while izq <= der and isInList == False: 
        print(lista)
        medio = (izq+der)//2
        print("calculo medio", (izq+der)//2)
        print(f"Valor izquierda {izq}, valor medio {medio}, valor derecha {der}")
        if lista[medio] == encontrar:
            isInList = True 
            return True
        elif lista[medio] > encontrar:
            der = medio -1
        else: 
            izq = medio + 1
    return isInList

listaEntrada = [2,12,34,5,11,59,4,3,1]
valorEncontrar = int(input("Por favor ingrese un número : "))
print(busquedabinaria(listaEntrada, valorEncontrar))