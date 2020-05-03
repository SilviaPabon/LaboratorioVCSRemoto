# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:04:54 2020

@author: --
"""
# ----- Paquetes y librerías ----- #

import random


# -----Funciones----- #

# 13
def combinar(ponderado, simbolos):
    baraja = {} 
    for element in simbolos:    
        for key in ponderado:
            baraja[key+element] = ponderado[key]
        
    return baraja

#Está mal
def revolver(combinatoria):
    combinar(ponderado, simbolos)
    
    simbolos2 = simbolos.copy()
    simbolos2 = []
    
    t = random.sample(simbolos2, len(simbolos2))
    simbolos2.append(t)
    
    baraja = {}     
    for element in simbolos2:    
        for key in ponderado:
            baraja[key+element] = ponderado[key]
    return baraja

# 14
def revolver2(combinatoria):
    combi = combinatoria.copy()
    llaves = []
    for i in combinatoria:
        llaves.append(i)
    llaves = random.sample(llaves, len(llaves))
    baraja = {}
    for element in llaves:
        for value in combi:
            if value[0] == element[0]:
                baraja[element] = combi[value]
            elif value == 1 and element[0] == "A":
                baraja[element] = combi[value]

    return baraja


def generador(listA, n):
    R = []
    for i in listA:
        R.append(i)
    R = random.sample(R, n)
    return R

# -----Principal----- #

# 11
ponderado = {"A": [1],
             "2": [2],
             "3": [3],
             "4": [4],
             "5": [5],
             "6": [6],
             "7": [7],
             "8": [8],
             "9": [9],
             "J": [10],
             "Q": [10],
             "K": [10]}

# 12
simbolos = ["C", "D", "T", "P"]

# 13
combinatoria = combinar(ponderado, simbolos)
print(combinatoria)

# 14 - 15
cartas_jugador = revolver2(combinatoria)
cartas_tallador = revolver2(combinatoria)
print (cartas_jugador)