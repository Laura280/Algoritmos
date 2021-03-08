numerosListas = [3,5,8,2,7]
cuadrado = lambda base : base **2 
listaCuadrados = list (map(cuadrado, numerosListas))
print (listaCuadrados)

restar = lambda numero : numero -2
listaRestar = list (map(restar, numerosListas))
print(listaRestar)

################ TALLER  ###################

numerosListas2 = [7,8,4,2]
cuadrado = lambda base : base **2
listaAlCuadrado = list (map(cuadrado, numerosListas2))
print (listaAlCuadrado)

numerosListas3 = [3,2,5,6,7,]
mayor = max(numerosListas3)
dividir= lambda numero : numero/mayor
listaNormalizada = list (map(dividir, numerosListas3))
print(listaNormalizada)

numerosListas4 = [6,7,2,3,5]
restarN = lambda numero : numero -4
listaRestar = list (map(restarN, numerosListas4))
print(listaRestar)

numerosListas5 = [4,6,2,9,8,0]
sumar = lambda numero : numero +6
listaSumar = list (map(sumar,numerosListas5))
print(listaSumar)

numerosListas6 = [5,7,8,4,2]
multiplicar = lambda numero : numero *5
listaMultiplicar = list (map(multiplicar, numerosListas6))
print(listaMultiplicar)