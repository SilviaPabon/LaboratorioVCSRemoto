# -*- coding: utf-8 -*-
"""
Created on Sat May  2 00:04:54 2020

@author: --
"""
#------------------------PARTE B-------------------------------------#


# ----- Paquetes y librerías ----- #

import random

# -----Funciones----- #

# La función combinar utiliza ciclos para combinar los elementos de una lista con las llaves de un diccionario; lo que crea otro diccionario con los elementos combinados como llaves
def combinar(ponderado, simbolos):
    baraja = {} 
    for element in simbolos:    
        for key in ponderado:
            baraja[key+element] = ponderado[key]
        
    return baraja


#La función revolver, tiene por parámetro el diccionario creado antes. 
#Utiliza la creación de una lista con las llaves del diccionario creado previamente, que luego es combinada aleatoriamente. Se crea un nuevo directorio por medio de ciclos, donde se van juntando la lista aleatorizada junto con los valores del anterior diccionario, siempre y cuando los valores coincidan con el número o la A que tiene la llave en primera posición.  
def revolver(combinatoria):
    combi = combinatoria.copy()
    llaves = [i for i in combinatoria]
    llaves = random.sample(llaves, len(llaves))
    baraja = {}
    for element in llaves:
        for value in combi:
            if value[0] == element[0]:
                baraja[element] = combi[value]
            elif value == 1 and element[0] == "A":
                baraja[element] = combi[value]

    return baraja

#La función repartir reparte cartas de la baraja al jugador y al tallador. Utiliza un condicional para saber si el jugador y el tallador no poseen cartas
#Si no tienen ninguna carta se reparten 2, utilizando un ciclo for para ello, y se eliminan esas cartas repartidas.
#Si ya tienen cartas solo les reparte 1 y también se elimina de la baraja

def repartir(baraja_usuario ,carta):
    baraja_copia = carta.copy()
    cartasBaraja = [key for key in baraja_copia]
    cartasRepartidas = []
    
    if len(baraja_usuario) == 0 :
        for i in range(2):
            cart = random.choice(cartasBaraja)
            cartasRepartidas.append(cart)
            del baraja_copia[cart]
    else:
        cartasRepartidas = baraja_usuario
        cart = random.choice(cartasBaraja)
        cartasRepartidas.append(cart)
        del baraja_copia[cart]
        
    return cartasRepartidas

#La función sumar_cartas realiza la suma de los valores de las cartas. Hace uso de ciclos for para ir sumando cada valor.
#A su vez, cálcula si en la primera barraja hay un BlackJack y cuando A vale 1 u 11.  

def sumar_cartas(cartas):
    blackjack = False
    AS = False
    
    suma = 0

    for carta in cartas:
        for cart in baraja:
            if carta==cart :
                suma += baraja[cart]
    
    for elemento in cartas:
        for valor in elemento:
            if valor == "A":
                AS = True
            if valor == "J" or valor == "K" or valor == "Q" :
                blackjack = True
                
    if (blackjack and AS) and len(cartas)==2 :
        suma = 21
    
    if AS == True and blackjack == False:
        suma21 = suma-1
        if (suma21+11) <= 21 :
            suma=suma21+11
            
    return suma

#La función mostrar muestra las cartas del jugador o tallador, junto su suma y si sobrepasaron el 21, significando una derrota.
def mostrar(lista):
    if sumar_cartas(lista) > 21 :
        return "Has perdido"
    else:
        return ("Las cartas que posee son: " + str(lista) + " que suman " + str(sumar_cartas(lista)))
    
#La función tomar_cartas_jugador toma cartas de la baraja para darselo a las cartas del usuario hasta que el no decida tomar más o se pase de 21
#Se utiliza un ciclo while para ir preguntale al jugador si quiere tomar una carta de la baraja(con la función repartir) hasta que diga no o se pase de 21
def tomar_cartas_jugador(jugador):
    
    print("\n" + "Jugador: " + str(mostrar(jugador)))
    if sumar_cartas(jugador) == 21 :
        return jugador
    tomar = input("¿Quiere tomar otra carta? ")
    cartas_jugador = jugador
    while (tomar == "si" or tomar == "yes") :     
        
        cartas_jugador = repartir(cartas_jugador, baraja)
        print(mostrar(cartas_jugador))  
        
        if mostrar(cartas_jugador) == "Has perdido":
            break
        tomar = input("¿Quiere tomar otra carta? ")

    return cartas_jugador
#La función tomar_cartas_tallador toma las cartas para el tallador o repartidor hasta que supere, iguale al jugador o sobrepase los 21.
#utiliza un ciclo while para tomar cartas de la baraja hasta que se cumplan una de las condiciones ya mencionadas.
def tomar_cartas_tallador(tallador):
    
    print("\n" + "Tallador: " + str(mostrar(tallador)))
    if sumar_cartas(tallador) == 21 :
        return tallador
    if sumar_cartas(cartas_jugador) > 21:
        return tallador
    cartas_tallador = tallador
    while (sumar_cartas(cartas_tallador) < sumar_cartas(cartas_jugador) 
           or sumar_cartas(cartas_tallador) == sumar_cartas(cartas_jugador)) :
        
        cartas_tallador = repartir(cartas_tallador, baraja)
        
        if sumar_cartas(cartas_tallador) > 21:
            break
        print("\n" + "Tallador: " + str(mostrar(tallador)))
        
    return cartas_tallador

#La función ganador decide quién fue el ganador de la partida. Haciendo uso de las anteriores funciones para decidir el ganador.
def ganador(jugador, tallador):
    if mostrar(cartas_jugador) == "Has perdido" :
        return "El tallador gana"
    elif sumar_cartas(jugador) > sumar_cartas(tallador):
        return "El jugador gana"
    elif sumar_cartas(jugador) == 21 :
        return "El jugador gana"
    elif sumar_cartas(tallador) == 21 :
        return "El tallador gana"
    elif sumar_cartas(tallador) > 21 :
        return "El jugador gana"
    elif sumar_cartas(jugador) < sumar_cartas(tallador) :
        return "El tallador gana"

#La función new_partida crea una nueva partida si el jugador elige continuar jugando. Utiliza un ciclo while para jugar tantas partidas como el jugador quiera.
def new_partida(part):
    cartas_jugador = []
    cartas_tallador = []
    ganadas = ganada
    perdidas = perdida
    partidas_jugadas = 1
    while part == "YES" :
        ponderado = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "J": 10, "Q": 10, "K": 10}
        simbolos = ["C", "D", "T", "P"]
        baraja = combinar(ponderado, simbolos)
        baraja = revolver(baraja)
        cartas_jugador = repartir(cartas_jugador, baraja)
        cartas_tallador = repartir(cartas_tallador, baraja)
        
        cartas_jugador = tomar_cartas_jugador(cartas_jugador)
        cartas_tallador = tomar_cartas_tallador(cartas_tallador)
        
        winner = ganador(cartas_jugador,cartas_tallador)
        print(ganador(cartas_jugador,cartas_tallador))
        partidas_jugadas += 1
        if winner == "El jugador gana":
            ganadas += 1
        else:
            perdidas += 1
            
        part = input("¿Quiere jugar otra partida? ")
        
    print("Jugaste " + str(partidas_jugadas) + " de las cuales ganaste " + str(ganadas) + " y perdiste " + str(perdidas))
        
        
# -----Principal----- #

# 11
ponderado = {"A": 1,
             "2": 2,
             "3": 3,
             "4": 4,
             "5": 5,
             "6": 6,
             "7": 7,
             "8": 8,
             "9": 9,
             "J": 10,
             "Q": 10,
             "K": 10}

# 12
simbolos = ["C", "D", "T", "P"]

# 13
baraja = combinar(ponderado, simbolos)
#14
baraja = revolver(baraja)


# 15
cartas_jugador = []
cartas_tallador = []

cartas_jugador = repartir(cartas_jugador, baraja)
cartas_tallador = repartir(cartas_tallador, baraja)


cartas_jugador = tomar_cartas_jugador(cartas_jugador)
cartas_tallador = tomar_cartas_tallador(cartas_tallador)
print(cartas_tallador)

winner = print(ganador(cartas_jugador,cartas_tallador))

partidas_jugadas = 1
ganada = 0
perdida = 0
if winner == "El jugador gana":
    ganada += 1
else:
   perdida += 1

game = input("¿Quiere jugar otra partida? ")
if game=="YES":
    new_partida(game)
else:
  print("Jugaste " + str(partidas_jugadas) + " de las cuales ganaste " + str(ganada) + " y perdiste " + str(perdida))