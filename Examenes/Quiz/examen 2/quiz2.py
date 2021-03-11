### MOSTRAR EN PANTALLA LOS PACIENTES TRATADOS EN MEDELLIN DURANTE EL AÑO 2020 ###
import pandas as pd
dicMesesDelA = {}
dicMesesDelA["Enero"] = 32121
dicMesesDelA["Febrero"] = 14564
dicMesesDelA["Marzo"] = 65465
dicMesesDelA["Abril"] = 85202
dicMesesDelA["Mayo"] = 93213
dicMesesDelA["Junio"] = 100231
dicMesesDelA["Julio"] = 120213
dicMesesDelA["Agosto"] = 65421
dicMesesDelA["Septiembre"] = 46546
dicMesesDelA["Octubre"] = 46547
dicMesesDelA["Noviembre"] = 84651
dicMesesDelA["Diciembre"] = 140521
serieMesesDelA = pd.Series(dicMesesDelA)
print(serieMesesDelA)

### MOSTRAR INFORMACIÓN EN CUATRIMESTRES ###
print ("A continuación se muestra el primer cuatrimestre")
print(serieMesesDelA["Enero":"Abril"])

print ("Esta es la información del segundo cuatrimestre")
print(serieMesesDelA["Mayo":"Agosto"])

print ("Esta es la información del tercer cuatrimestre")
print(serieMesesDelA["Septiembre":"Diciembre"])

### MOSTRAR EL PROMEDIO DE LOS PACIENTES ATENDIDOS POR MES EN MEDELLIN (2020) ###
from functools import reduce
listaPacientes = [32121, 14564, 65465, 85202, 93213, 100231, 120213, 65421, 46546, 46547, 84651, 140521]
promediar = lambda acumulador = 0, elemento = 0 : acumulador + elemento
resultadopromedio = reduce (promediar, listaPacientes) /len (listaPacientes)
print (resultadopromedio)

### MOSTRAR EN PANTALLA LAS ENFERMEDADES EN BOGOTA DURANTE EL PRIMER SEMESTRE (2020) ###
dicDistribucionEnfermedades = {
    "Enfermedades General": [32121, 14564, 65465, 85202, 93213, 100231],
    "covid-19" : [0, 0, 223, 3453, 4543, 43643],
    "Traumatismos" : [6545, 43243, 67657, 435435, 435435, 43543],
    "Cancer" : [6541, 4334, 4323, 34545, 5454, 7675]
}
listaMeses = ["Enero","Febreo","Marzo","Abril","Mayo","Junio"]
dataFrameDistribucionEnfermedades = pd.DataFrame(dicDistribucionEnfermedades, index= listaMeses)
print(dataFrameDistribucionEnfermedades)

### MOSTRAR EN PANTALLA EL PROMEDIO DE LOS PACIENTES POR COVID DE ABRIL, MAYO Y JUNIO
listaNumeroPacientes = [3453, 4543, 43643]
promediar = lambda acumulador = 0, elemento = 0 : acumulador + elemento
resultadopromedio = reduce (promediar, listaNumeroPacientes) /len (listaNumeroPacientes)
print ("Este es le promedio de pacientes por covid duerante los meses de abril, mayo y junio: ")
print (resultadopromedio)

### MOSTRAR EN PANTALLA LA INFORMACIÓN DE LOS PRIMEROS TRES MESES DE PACIENTES TRATADOS POR TRAUMATISMO O CANCER
print(dataFrameDistribucionEnfermedades[["Traumatismos","Cancer"]]["Enero":"Marzo"])

### FUNCION FILTER QUE MUESTRE LOS PACIENTES QUE SUPERAN 40000 EN ENFERMEDAD GENERAL
listaEnfermedadesGeneral = [32121, 14564, 65465, 85202, 93213, 100231]
superar = lambda valor : valor > 40000
listaQueSobrepasa = list (filter(superar, listaEnfermedadesGeneral))
print ("Estos son los pacientes de enfermedad general por encima de 40000 personas : ")
print(listaQueSobrepasa)

### FUNCION MAP PARA MULTIPLICAR LOS PACIENTES CON CANCER POR 10%
listaPacientesConCancer = [6541, 4334, 4323, 34545, 5454, 7675]
multiplicar = lambda numero : numero *0.1
listaMultiplicar = list (map(multiplicar, listaPacientesConCancer))
print(listaMultiplicar)

### FUNCION REDUCE PARA LA SUMA DE PACIENTES CON TRAUMATISMOS
listaPacientesConTraumatismo = [6545, 43243, 67657, 435435, 345345, 43543]
sumador = lambda acumulador = 0, valor = 0 : acumulador + valor
resultado = reduce (sumador, listaPacientesConTraumatismo)
print("Esta es la suma de pacientes con traumatismo: ")
print (resultado)