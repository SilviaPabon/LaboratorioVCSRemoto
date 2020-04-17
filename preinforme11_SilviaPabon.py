# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 09:24:23 2020

@author: --
"""


# -------- Paquetes y librerÃ­as -------- #

import numpy as np

#  ------------- Funciones ------------- #
# Array con los valores mmeteorolÃ³gicos, almacenados en la variable clima
def clima():
    clima = np.array([
        [[33,35,40],[8,8.2,8.5],[10,10,10]],
        [[30,28,27],[7,7.5,7.4],[10,10,10]],
        [[10,9,8],[5.9,6,6.2],[10,10,10]]])        
    return clima
"""
Funcion promTemp, para calcular el promedio de la temperatura. 
Se hace uso de la variable s para almacenar el acumulado que se obtiene a partir del ciclo for.
Despues se calcula el promedio utilizando la variable s y dividiendola en la cantidad de numeros sumados 
"""

def promTemp(clima, fila):
    s = 0
   
    for i in range(0,len(clima[0,fila])):
        s += clima[fila, 0, i]
       
    
    prom = round((s/(len(clima[fila,0]))),2)

    return prom

"""
La funcion humedadRelativa calula la humedad relativa de cada ciudad
las variables va y vs representan el vapor de agua y el vapor de agua saturado respectivamente
Se utiliza un ciclo for para calcular el acumulado de vapor de agua y vapor de agua saturado
Despues se divide estos valores entre la cantidad de numeros sumados
Por ultimo se aplica la formula de humedad para obtener el resultado

"""

def humedadRelativa(clima, fila):
    va = 0
    vs = 0 
    for i in range(0,clima.shape[fila]):
        va += clima[fila, 1, i]
        vs += clima[fila, 2, i]
    va = va/(len(clima[fila,1]))
    vs = vs/(len(clima[fila,2]))
    
    humedad = round(((va/vs)*100),2)
    return humedad

"""
La funcion puntoRocio calcula el punto de rocÃ­o en cada ciudad
primero se utilizan las dos funciones anteriores para calular la temperatura y la humedad relativa
Por ultimo, se calcula el punto de rocÃ­o mediante la fÃ³rmula. 

"""

def puntoRocio(clima, fila):
    temp = promTemp(clima, fila)
    HR = humedadRelativa(clima, fila)
    Pr = round((((HR/100)**(1/8))*(110+temp)-110),2)
    return Pr
    
    
    
    

# ------------------------------------------ Principal ------------------------------------------ #

clima = clima()

print("La temperatura promedio de Barrancabermeja es:", promTemp(clima, 0))
print("La temperatura promedio de Bucaramanga es:", promTemp(clima, 1))
print("La temperatura promedio de BogotÃ¡ es:", promTemp(clima, 2))

print("El promedio de la humedad relativa de Barrancabermeja es:", humedadRelativa(clima, 0), "%")
print("El promedio de la humedad relativa de Bucaramanga es:", humedadRelativa(clima, 1), "%")
print("El promedio de la humedad relativa de BogotÃ¡ es:", humedadRelativa(clima, 2),"%")

print("El promedio del punto de rocÃ­o de Barrancabermeja es:", puntoRocio(clima, 0))
print("El promedio del punto de rocÃ­o de Bucaramanga es:", puntoRocio(clima, 1))
print("El promedio del punto de rocÃ­o de BogotÃ¡ es:", puntoRocio(clima, 2))
