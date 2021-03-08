from functools import reduce
lista = [3,5,6,2,5]
sumador = lambda acumulador = 0, elemento = 0 : acumulador + elemento
resultado = reduce (sumador, lista)
print (resultado)

listaPalabras = ["¿", "Hola", ",", "cómo", "están", "?"]
union = lambda frase, palabra : frase + " " + palabra
resultadoFrase = reduce (union, listaPalabras)
print(resultadoFrase)

############# TALLER ##########
listaElementos = [8,3,6,8,1]
restador = lambda acumulador = 0, elemento = 0 : acumulador - elemento
resultadoResta = reduce (restador, listaElementos)
print (resultadoResta)

ListaDePalabras = ["A", "mi", "me", "gusta", "mucho", "dormir"]
unionPalabras = lambda frase, palbra : frase + " " + palbra
resultadoDePalabras = reduce (unionPalabras, ListaDePalabras)
print(resultadoDePalabras)

listaNumeros1 = [56,52,51,22,2]
sumatoria = lambda acumulador = 0, elemento = 0 : acumulador + (elemento/2)
resultadoSumatoria = reduce (sumatoria, listaNumeros1) 
print (resultadoSumatoria)

listaNumeros = [3,5,1,2,2]
promediar = lambda acumulador = 0, elemento = 0 : acumulador + elemento
resultadopromedio = reduce (promediar, listaNumeros) /len (listaNumeros)
print (resultadopromedio)

listaElementos2 = [7,23,6,4,2]
multiplicar = lambda acumulador = 0, elemento = 0 : acumulador * elemento
resultadoMultiplicar = reduce (multiplicar, listaElementos2)
print (resultadoMultiplicar)