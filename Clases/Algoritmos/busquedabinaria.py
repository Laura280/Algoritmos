def busquedabinaria(lista,encontrar):
    """Busqueda binaria
    se ingresa una lista y un valor a encontrar
    y entonces se devuele si lo encontró o no
    """
    isInList = False
    izq= 0
    der = len(lista)-1
    while izq <= der and isInList == False: 
        medio = (izq+der)//2
        if lista[medio] == encontrar:
            isInList = True 
            return True
        elif lista[medio] > encontrar:
            der = medio -1
        else: 
            izq = medio + 1
    return isInList

