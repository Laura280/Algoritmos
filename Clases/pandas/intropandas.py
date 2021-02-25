import pandas as pd 
listaVariada = ["a",1,2,4.6]
print (listaVariada)
seriesPandas = pd.Series ([1,2,5])
print (seriesPandas)
print(2**64)
seriesPandas = pd.Series ([4.6,5.7,0.1])
print (seriesPandas)
dicGanancias = {}
dicGanancias["Enero"] = 4300
dicGanancias["Febrero"] = 4356
dicGanancias["Marzo"] = 7434
dicGanancias["Abril"] = 7621
serieGananciaPorMes = pd.Series([4300,4356,7434,7621])
print(serieGananciaPorMes)
seriesGananciaPorMEsDic = pd.Series (dicGanancias)
print ("Enero", seriesGananciaPorMEsDic ["Enero"])
print (seriesGananciaPorMEsDic ["Enero":"Marzo"])

matrizEstudiantes = {
                        "Grupo1" : ['Karla', 'Mario', 'Laura'],
                        "Grupo2" : ['Santi', 'Arturo', 'Vale'],
                        "Grupo3" : ['Juan', 'Melany', 'Laura'],
                        "Grupo4" : ['Mafer', 'Esteban', "Daniel"],
}
dataFrameNombres = pd.DataFrame(matrizEstudiantes)
print (dataFrameNombres)

dicVentasPorMes = {
    "Marzo (millones de pesos)" : [1356,2578,9802],
    "Abril (millones de pesos)" : [1356,2785,96702],
    "Mayo (millones de pesos)" : [1554,7378,2681]
}
dataFrameVentas = pd.DataFrame (dicVentasPorMes, index= ["Tomates","Papa","Yuca"])
print(dataFrameVentas)