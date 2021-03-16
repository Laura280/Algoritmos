#Fibonacci: 0,1,1,2,3,5,8,13,21

#--- Preguntas ---#
PREGUNTA_NUMERO = "Ingrese un número entero : "
#--- Mensaje Error ---#
ERROR_ENTRADA = "Entrada no válida"
#--- Entradas ---#
numero = None
while (numero == None):
    try:
        numero = int(input(PREGUNTA_NUMERO))
    except ValueError:
        print (ERROR_ENTRADA)
print(numero)

numeroAnterior = 0
numeroActual = 1
if (numero == 1):
    print(numeroAnterior)
elif (numero ==2):
    print(numeroActual)
else:
    for i in range (2, numero+1):
        print(i)
        aux = numeroActual
        numeroActual = numeroAnterior + numeroActual
        numeroAnterior = aux
        print(numeroActual)
    print ("salida", numeroActual)
