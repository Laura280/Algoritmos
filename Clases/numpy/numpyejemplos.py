import numpy as np 
lista = [1,2,3,4,5]
listaC = []
for i in range (200,800,2):
    listaC.append(i)
print(listaC)
listaN = np.arange (200,801,2)
listaNu = np.arange (1,11,1)
print(listaN)
print(listaN[:101])

print(listaNu)
print(listaNu[::2])
listaNu[::2]=200
print(listaNu)

#indexación lógica
edades = [14,23,43,56,78,5,8]
edades = np.array (edades)
indEdades = edades > 18
print(edades)
print (indEdades)
totalMayorEdad = np.sum (indEdades)
print (totalMayorEdad)
indEdades2 = edades == 23 
indEdades3 = edades == 78
indEdades4 = indEdades2 | indEdades3
print(indEdades2)
print(indEdades2)
print(indEdades4)
print (np.sum(indEdades4))

#Entre 23 y 50.
indEdadesIntervalo1 = edades >= 23
indEdadesIntervalo2 = edades <= 50
print("#"*30)
print (indEdadesIntervalo2)
print (indEdadesIntervalo1)
indEdadesIntervalo = indEdadesIntervalo2 & indEdadesIntervalo1
print(indEdadesIntervalo)
print(np.sum(indEdadesIntervalo))
print("#"*30)

#promedio
print("#"*30)
acum = 0
for elemento in edades:
    acum += elemento
    print (acum/len(edades))
print (np.mean(edades))
print("#"*30)

#---mamás---#
print("#"*30)
mamas = [56,78,34,56,22,36,45]
mamas = np.array (mamas)
hijosMayores30 = edades > 30
print(hijosMayores30)
print (mamas[hijosMayores30])
print(mamas)
print( np.mean(mamas[hijosMayores30]))
print("#"*30)
#Matriz Numpy
edadesHijos = np.array([14,18,22,24])
edadesMamas = np.array([45,54,67,74])
childrenMoms = np.array([edadesHijos,edadesMamas])
print(childrenMoms)
#Transponer Matriz
inKids = childrenMoms[0] >= 18
print(childrenMoms.transpose())
print (np.sum(inKids))
print ("#"*30)
print (np.mean(childrenMoms [1][inKids]))
#ordenando lista
listaEdades = [12,234,54,6,123,54]
#listaEdades.sort()
print (listaEdades)
listaEdadesNp = np.array(listaEdades)
listaEdadesNpord = np.sort(listaEdadesNp)
print(listaEdadesNpord)
print("El que más años tiene es ..", max(listaEdades))
print("El que menos años tiene es ..", min(listaEdades))

#Máximo o mayor y minimo.
print("El que más años tiene es ..", np.max(listaEdadesNp))
print("El que máenos años tiene es ..", np.min(listaEdadesNp))
#mayor a 200
mayoresADoce = listaEdadesNp > 12
print (listaEdadesNp[mayoresADoce])
mayoresAOcho = np.where(listaEdadesNp>8)
print(mayoresADoce)
print(mayoresAOcho[0])
print(listaEdades)
print(listaEdadesNp[mayoresAOcho[0]])
