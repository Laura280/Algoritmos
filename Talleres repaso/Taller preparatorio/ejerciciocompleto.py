##   Crear un elemento donde muestre las ventas totales mes a mes
# de una empresa durante un año.
import pandas as pd 
dicEarningsPerYear = {}
dicEarningsPerYear["Enero"] = 1234124
dicEarningsPerYear["Febrero"] = 1297
dicEarningsPerYear["Marzo"] = 16566
dicEarningsPerYear["Abril"] = 890124
dicEarningsPerYear["Mayo"] = 1055124
dicEarningsPerYear["Junio"] = 13904124
dicEarningsPerYear["Julio"] = 673124
dicEarningsPerYear["Agosto"] = 894124
dicEarningsPerYear["Septiembre"] = 34124
dicEarningsPerYear["Octubre"] = 934124
dicEarningsPerYear["Noviembre"] = 5774124
dicEarningsPerYear["Diciembre"] = 40368
serieEarningsPerYear =pd.Series(dicEarningsPerYear)
print(serieEarningsPerYear)

#Muestren en pantalla las ganancias por trimestre
print ("primer trimestre")
print(serieEarningsPerYear["Enero":"Marzo"])
print ("tercer trimestre")
print(serieEarningsPerYear["Julio":"Septiembre"])
print ("tercer trimestre")
print(sum(serieEarningsPerYear["Julio":"Septiembre"]))

dicGananciasTrimestrales = {}
dicGananciasTrimestrales["1er trimestre"] = sum (serieEarningsPerYear["Enero":"Marzo"])
dicGananciasTrimestrales["2do trimestre"] = sum (serieEarningsPerYear["Abril":"Junio"])
dicGananciasTrimestrales["3er trimestre"] = sum (serieEarningsPerYear["Julio":"Septiembre"])
dicGananciasTrimestrales["4to trimestre"] = sum (serieEarningsPerYear["Octubre":"Diciembre"])
seriesGananciasTrimestrales = pd.Series(dicGananciasTrimestrales)
print(seriesGananciasTrimestrales)
print(sum(serieEarningsPerYear))

#Ganancias por mes por departamento Antioquia, Amazonas, Cundinamarca
dicGananciasPorDepartamento = {
    "Antioquia": [3453,6235,8642,5788,2564,7899],
    "Amazonas" : [466567,76546,4554,34656,45656,5774],
    "Cundinamarca" : [254656,8865,2454,96875,4345,6588]
}
listaMeses = ["Enero","Febreo","Marzo","Abril","Mayo","Junio"]
dataFrameGananciasPorDepartamento = pd.DataFrame(dicGananciasPorDepartamento, index= listaMeses)
print(dataFrameGananciasPorDepartamento)

print(dataFrameGananciasPorDepartamento[["Antioquia","Amazonas"]]["Marzo":"Mayo"])