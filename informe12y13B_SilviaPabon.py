# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:04:54 2020

@author: --
"""
# ----- Paquetes y librerías ----- #

import random

# -----Funciones----- #

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


# -----Principal----- #
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

simbolos = ["C", "D", "T", "P"]

combinatoria = combinar(ponderado, simbolos)
print(combinatoria)

cartas_jugador = revolver(combinatoria)

print (cartas_jugador)