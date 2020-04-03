# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 11:42:12 2020

@author: --
"""


# -------- Paquetes y librerías -------- #

import numpy as np

#  ------------- Solución ------------- #

def utilOperAn():
    uom = np.array([
        27834, 23789, 30189, 30967, 32501, 32701, 31665,
        17155, 4614, 834])
    return uom

# Diferencia entre utilidades oper. promedio 1ros 2 años y 2 últimos años

def difer_promedios(uom):
    long=len(uom)
    sum1 = (uom[0]+uom[1])/2
    sum2 = (uom[long-1]+uom[long-2])/2
    difPro = sum1-sum2
    return difPro

# Diferencia entre utilid mayor y utilidad menor
    
def diferencia_bajo_alto(uom):
    long = len(uom)
    utilMayor = uom[0]
    utilMenor = uom[0]
    for i in range(1,long):
        if utilMayor < (uom[i]):
            utilMayor = uom[i]
        if utilMenor > (uom[i]):
            utilMenor = uom[i]
        difMayMen = utilMayor-utilMenor
        return difMayMen

# Mediana de la utilidad oper. durante años de registro
    
def mediana_uo(uom):
    long = len(uom)
    orden = 0
    for i in range(0,long):
        for j in range(0,long-1):
            if uom[j] > uom[j+1]:
                orden = uom[j]
                uom[j] = uom[j+1]
                uom[j+1] = orden
    
    half = int(long/2)   
    if len(uom)%2 == 0:
        mediana = (uom[half]+uom[half-1])/2
    else:
        mediana = (uom[half//1])
    
    return mediana

# Media

def media_uo(uom):
    long = len(uom)
    sumatoria = uom[0]
    mediana=mediana_uo(uom)
    for i in range(1, long):
        sumatoria += uom[i]
        promedio = sumatoria/long
        difPromed = mediana-promedio
        return difPromed
    
# porcentaje de uo para ua

def porcentajeUo(uom):
    long = len(uom)
    sumatoria = 0
    porcen = 0
    for i in range(0,long):
        sumatoria += uom[i]
    sumatProm = 0
    for i in range (0, long):
        porcen = uom[i]*100/sumatoria
        sumatProm += porcen
        print("El orcentaje que aporta la Util Oper de cada año a la Oper Acumul: ")
        print (porcen)
        
# Deficit de utilidad operativa año 2017
def deficitUo2017(uom):
    deficit = uom[8] - uom[9]
    return deficit

# Deficit en utilidad operativa cada año   
def porcentajeDeficitAnual(uom):
    long = len(uom)
    for i in range (0, long-1):
        defA = uom[i]-uom[i+1]
        promDef = defA*100/uom[i]
        print("Déficit de la utilidad operacional cada año del registro: ")        
        print(promDef)
        
# Resultados #

uom=utilOperAn()

print("La diferencia del promedio de los ultimos años y los primeros años un la utilidad es: " + str(difer_promedios(uom)))
print("La diferencia de utilidades operacionales, entre el año con más y menos utilidades es: " + str(diferencia_bajo_alto(uom)))
print("La mediana de la utilidad operacional durante los años de registro es: " + str(mediana_uo(uom)))
print("La media equivale a: " + str(media_uo(uom)))
print("Déficit de la utilidad operacional del año 2017 respecto a 2016: " + str(deficitUo2017(uom)))

