def contarPalabrasV1(parrafo):
    dictPalabrasOcurrencias = {}
    listaPalabras = parrafo.split()
    for palabra in listaPalabras:
        dictPalabrasOcurrencias[palabra] = listaPalabras.count(palabra)
    return dictPalabrasOcurrencias