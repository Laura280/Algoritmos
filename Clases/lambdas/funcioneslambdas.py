def linedesign (cantidad):
    print ("#"*cantidad)

def sumar (a,b):
    suma= a+b
    return suma

def restar (a,b):
    restar= a-b
    return restar

def multiplicar (a,b):
    multiplicar= a*b
    return multiplicar

def dividir (a,b):
    dividir = a/b
    return dividir

def calculadora (funcion, a, b):
    return funcion (a,b)

linedesign(30)
print("Hola a todos")
linedesign(20)
sumar(2,6)
print(sumar(2,6))
print(restar(2,6))
print(multiplicar(7,63))
print(dividir(25,6))
linedesign(20)
print (calculadora(sumar,12,14))

linedesignlambda = lambda cantidad=60 : print("#"*cantidad)
linedesignlambda()
sumarl = lambda a=0 , b=0 : a+b
multiplicarl = lambda a=0, b=0 : a*b
dividirl = lambda a=0, b=0 : a/b
restarl = lambda a=0, b=0 : a-b
print(sumarl(2,3))
print(multiplicarl(2,3))
print(dividirl(2,3))
calculadoral =  lambda func=  restarl, a=0, b=0 : func(a,b)
print (calculadora(multiplicarl, 56,32))

listaEdades = [18,12,14,13,12,20]
listaEdades2 = [18,123,14,13,12,20]

lambdamaximos = lambda x = [], y = [] : print (max(x), (max(y)))
lambdamaximos (listaEdades, listaEdades2)
mayorEdad = lambda edad = 0 : edad >= 18
(mayorEdad(14))
(mayorEdad(19))
mayores = list(filter(mayorEdad, listaEdades))
print(mayores)