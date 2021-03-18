import time
timepoInicial = time.time()
print("Hola a todos")
time.sleep(2)
tiempoFinal = time.time()
delta = tiempoFinal - timepoInicial
print(delta)

# Inico de conteo #
timepoInicial = time.time()
#--Instrucciones--#
print("Hola a todos")
x = 8
for i in range(x):
    print(i)
# Ciere de conteo #
tiempoFinal = time.time()
delta = tiempoFinal - timepoInicial
print(delta)


# Inico de conteo #
timepoInicial = time.time()
#--Instrucciones--#
print("Hola a todos")
x = 8
for i in range(x):
    for j in range(x):
        print(i)
# Ciere de conteo #
tiempoFinal = time.time()
delta = tiempoFinal - timepoInicial
print(delta)