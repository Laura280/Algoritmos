def contarPalabrasV2(parrafo):
    dictPalabrasOcurrencias = {}
    listaPalabras = parrafo.split()
    for palabra in listaPalabras:
        dictPalabrasOcurrencias[palabra] = 0
        for i in range (len(listaPalabras)):
            if palabra == listaPalabras[i]:
                dictPalabrasOcurrencias[palabra] += 1
    return dictPalabrasOcurrencias