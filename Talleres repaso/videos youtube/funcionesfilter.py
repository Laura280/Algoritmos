listaPares = [2,3,4,523,32,6,8,12]
par = lambda valor : valor %2 ==0
listaPareslistaFiltrada = list (filter(par, listaPares))
print(listaPareslistaFiltrada)

mayores = lambda valor : valor >= 12
listaMayores = list (filter(mayores,listaPares))
print(listaMayores)


################## TALLER ###############
listaEnteros = [1,5,7,35,49,81]
enteros = lambda valor : valor %7 ==0
ListaEnterosFiltrada = list (filter(enteros,listaEnteros))
print(ListaEnterosFiltrada)

listaEstudiantes = ["Juan", "Carolina", "Julian", "Marina"]
lenEstudiante = lambda palabra : len (palabra) <5
listaEstudiantesFiltrada = list (filter(lenEstudiante,listaEstudiantes))
print(listaEstudiantesFiltrada)

listanumeros1 = [2,6,9,1]
pares = lambda numero : numero %2 == 0
listaPareslistaFiltrada = list (filter(pares, listanumeros1))
print(listaPareslistaFiltrada)

listanumeros2 = [3,7,45,99]
impares = lambda valor : valor %2 !=0
listaImparesFiltrada = list (filter(impares, listanumeros2))
print(listaImparesFiltrada)

listaNombres = ["Esteban", "Juan", "Elena", "Pablo"]
inicialesConE = lambda nombre : nombre[0] ==  'E'
listaInicialesConE = list(filter(inicialesConE,listaNombres))
print(listaInicialesConE)

listaEdades= [3,67,5,15,20]
mayores = lambda valor : valor >= 18
listaMayoresEdad = list (filter(mayores, listaEdades))
print(listaMayoresEdad)

listaFrases = ["ellos no te odian", "Mis padres me quieren", "Mis amigas odian el deporte"]
odiar = lambda elemento : 'odian' not in elemento
listaFrasesFilter = list(filter(odiar, listaFrases))
print (listaFrasesFilter)

