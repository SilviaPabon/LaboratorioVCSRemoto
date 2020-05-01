# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 21:55:32 2020

@author: --
"""



#La función clima devuelve un diccionario donde cada llave es una ciudad y los valores dentro de ellas son una lista de listas.
#Las listas representan la temperatura, vapor de agua y vapor de agua saturado, respectivamente.
def clima():
    clima = {"Barrancabermeja" : [[33,35,40],[8,8.2,8.5],[10,10,10]],
             "Bucaramanga": [[30,28,27],[7,7.5,7.4],[10,10,10]],
             "Bogotá": [[10,9,8],[5.9,6,6.2],[10,10,10]]}
    return clima

#La función promTemp calcula el promedio de la temperatura.
#Tiene como valores de entrada el diccionario y una llave
#Se utiliza un ciclo for para calcular la suma de las temperaturas y luego se dividen entre la cantidad sumada.
def promTemp(clima, ciudad):
    suma = 0
    for i in clima[ciudad][0]:
        suma += i
    prom = round((suma/(len(clima[ciudad][0]))),2)
    return prom

# La función humedadRelativa calcula la humedad relativa en las 3 ciudades.
#Se realiza un for para calcular la sumatoria del vapor de agua(va) y el vapor de agua saturado(vs), para después dividirlo entre la cantidad de datos sumados y así obtener el promedio de ambos.
#Por ultimo, se calcula la humedad relativa mediante la formula (va/vs)*100
def humedadRelativa(clima, ciudad):
    va = 0
    vs = 0 
    for i in range(0, len(clima[ciudad])):
        va += clima[ciudad][1][i]
        vs += clima[ciudad][2][i]
        
    va = va/(len(clima[ciudad][1]))
    vs = vs/(len(clima[ciudad][2]))
    
    humedad = round(((va/vs)*100),2)
    return humedad

#La función puntoRocío calcula la media del punto de Rocío de cada ciudad
#Se utilizan las funciones anteriorres para obtener la temperatura y la humedad relativa y posteriormente se aplica la fórmula ((HR/100)**(1/8))*(110+temp)-110)
def puntoRocio(clima, ciudad):
    temp = promTemp(clima, ciudad)
    HR = humedadRelativa(clima, ciudad)
    Pr = round((((HR/100)**(1/8))*(110+temp)-110),2)
    return Pr


#----------------------Principal--------------------------#

clima = clima()
print("El promedio de temperatura en Barrancabermeja es: " + str(promTemp(clima, "Barrancabermeja")))
print("El promedio de temperatura en Bucaramanga es: " + str(promTemp(clima, "Bucaramanga")))
print("El promedio de temperatura en Bogotá es: " + str(promTemp(clima, "Bogotá")))
print("\n")

print("El promedio de la humedad relativa de Barrancabermeja es: " + str(humedadRelativa(clima, "Barrancabermeja")) + "%")
print("El promedio de la humedad relativa de Bucaramanga es: " + str(humedadRelativa(clima, "Bucaramanga")) + "%")
print("El promedio de la humedad relativa de Bogotá es: " + str(humedadRelativa(clima, "Bogotá")) + "%")
print("\n")

print("El promedio del punto de rocío de Barrancabermeja es: " + str(puntoRocio(clima, "Barrancabermeja")))
print("El promedio del punto de rocío de Bucaramanga es: " + str(puntoRocio(clima, "Bucaramanga")))
print("El promedio del punto de rocío de Bogotá es: " + str(puntoRocio(clima, "Bogotá")))