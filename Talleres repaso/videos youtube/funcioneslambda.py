def linedesing(cantidad):
    print("#"*cantidad)
linedesing(2)

##Funciones Lambdas##
#Estructura: lambda entradas : accion #
line = lambda cantidad=12 : print ("#"*cantidad)
line()
line(2)

sumar = lambda valor1=0, valor2=0 : valor1 + valor2
restar = lambda valor1=0, valor2=0 : valor1 - valor2
multiplicar = lambda valor1=0, valor2=0 : valor1 * valor2
dividir = lambda valor1=0, valor2=0 : valor1 / valor2

calculadora = lambda accion, valor1=0, valor2=0 : print(accion(valor1, valor2))
calculadora (multiplicar, 45,3)


################## TALLER ##################

numero= int (input("por favor ingrese un valor :"))
elevar = lambda valor : valor **3
print (elevar(numero))

linedesignlambda = lambda cantidad=1: print("El profesor nos dejó muchos ejercicios para que aprendieramos"*cantidad)
linedesignlambda()

listaNumeros1 = [5,6,7,3]
listaNumeros2 = [5,9,7,2]
lambdamayornumero = lambda x = [], y = [] : print (max(x), (max(y)))
lambdamayornumero (listaNumeros1, listaNumeros2)

par = lambda numero : numero%2 == 0
print (par(6))
print (par(99))

impar = lambda numero : numero%2 != 0
print(impar(3))
print (impar(88))

union = lambda palabra1, palabra2 : palabra1 + palabra2
print (union("Ele", "fante"))

pregunta = 'Por favor ingrese su nombre : '
nombre = input(pregunta)
saludar = lambda name = '' : print ("Hola" " "+ nombre)
saludar(nombre)

palabra= 'Otorrinolaringologo'
lenPalabra  = lambda palabra : len (palabra)
print (lenPalabra(palabra))

showlen = lambda funcion, palabra : print (funcion(palabra))
showlen(lenPalabra, palabra)

bases= [6]
alturas = [23]
divisores = [2]
calcularAreaTriangulo = lambda base = 0, altura = 0, divisores =1: base*altura/divisores
listaAreasTriangulos = list(map(calcularAreaTriangulo, bases, alturas, divisores))
print(listaAreasTriangulos)

pesos = [80]
estaturas = [1.77]
imc = lambda peso = 0, estatura = 1 : peso / estatura**2
imcListas = list(map(imc,pesos,estaturas))
print(imcListas)