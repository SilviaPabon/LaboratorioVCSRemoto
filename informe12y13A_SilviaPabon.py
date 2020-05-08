# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:59:47 2020

@author: --
"""
# ------------------Importe librerías---------------------#

import random as rd

#--------------------Funciones---------------------------------#

#La función imprimir imprime los elementos de una lista y la cantidad de elementos que esta contiene 
def imprimir(lista):
    print("La lista contiene: " + str(len(lista)) + " elementos")
    print("Los elementos de la lista son: " + str(lista) + "\n")

#La función generador recibe como parámetros de entrada una lista A y un valor N para retornar una nueva lista con N elementos de la lista A seleccionados aleatoriamente y sin repeticiones.  
#Para ello, utiliza un ciclo while que agrega los N número de elementos establecidos. Se hace uso de la librería de random, con choice, para escoger los elementos aleatoriamente. Por último se utiliza un condicional para asegurarse que no se repitan elementos.
def generador(A, N):
  R =[]
  num = 0
  while num < N:
      Carta = rd.choice(A)
      if not Carta in R:
          R.append(Carta)
          num +=1
  return R

#La función combinador recibe como parámetros de entrada dos listas A y B, retornando una lista R con los elementos de A y B mezclados. 
#Para ello, se suman los elementos A y B en una lista n y se hace uso de la librería random, con sample, para organizarlos de forma aleatoria. 
def combinador(A, B):
    n = A + B
    R = rd.sample(n,len(n))
    return R

# la función lotería, que recibe como parámetros, la lista paquete y la lista premium. 
#En primer lugar, verifica si paquete tiene objetos repetidos, por medio de un for y una nueva lista, sumando cada vez que se cumpla la condición de que ya está en la lista el elemento. 
#Luego verifica si en paquete hay cartas premium repetidas. Finalmente se verifica que la cantidad de elementos repetidos en paquete sea mayor o igual a uno y que las cartas premium no estén repetidas más de una vez. Si la anterior condición se cumple se genera la probabilidad de un 10% de que se anexe una carta premium adicional que no esté en paquete. 
#Si no se cumple, se informa que no se cumplió la condición. 
def loteria(paquete, premium):
   
    repetidas = 0
    prueba = []
    for cartas in paquete:
        if cartas not in prueba:
            prueba.append(cartas)
        else:
            repetidas += 1
    print(repetidas)
    
    repetidasP = 0
    for cartas in paquete:
        if cartas in paquete == "AIVLIS":
            repetidasP += 1
        if cartas in paquete == "lEIRBAG":
            repetidasP += 1
        if cartas in paquete == "NAILUJ":
            repetidasP += 1
        if cartas in paquete == "SOLRAC":
            repetidasP += 1
        if cartas in paquete == "ANAID":
            repetidasP += 1
    print(repetidasP)
  
    if repetidas >= 1 and repetidasP <= 1:
       probabilidad = rd.randint(0,10)
       print (probabilidad)
       if probabilidad == 5:
           cartaP = rd.choice(premium)
           print ("hola", cartaP)
           condicion=0
           while condicion == 0:
               cartaP = rd.choice(premium)
               if cartaP not in paquete:
                   paquete.append(cartaP)
                   condicion=1
              
    else:
        print("usted no cumplio las condiciones para entregarle la carta")
    return(paquete)

#La función cartasPremium identifica cuántas y cuáles fueron las cartas premium obtenidas.
# Para la cual se hace uso de list comprehension para crear una lista con las cartas premium obtenidas. Después se hace uso de condicionales para imprimir el número de premium que tuvo y cuales fueron. En caso de no haber premium se imprime que no hubo cartas premium. 
def cartasPremium(jugador):
    prem = [cartas for cartas in jugador for cartPremium in premium if cartas==cartPremium]
    num = 0
    for i in range(len(prem)):
        num += 1
    if num != 1 and num != 0:
        print("Hubo " + str(num) + " cartas premium que fueron " +str(prem) + "\n")
    elif num==1:
        print("Hubo " + str(num) + " carta premium que fue " +str(prem) + "\n")
    else:
        print("No hubo cartas premium" + "\n")

#La función cartasRepetidas cuenta cuántas cartas se repitieron. 
#Para esto hace uso de un ciclo for con condicionales que va almacenando las cartas únicas en una lista y para aquellas que se repiten se van sumando para obtener el total de repetidas. Retorna la cantidad de cartas repetidas. 
def cartasRepetidas(jugador):
    repetidas = 0
    jugador_sin_repetidas = []
    for cartas in jugador:
        if cartas not  in jugador_sin_repetidas:
            jugador_sin_repetidas.append(cartas)
        else:
            repetidas += 1
    return repetidas

#La función cantidadCartas recibe como parámetros la lista jugador y mazo (suma de cartas y cartas premium), la función cuenta la cantidad de veces que aparece cada carta de mazo en la lista del jugador, por medio de dos ciclos for y un condicional. 

def cantidadCartas(jugador, mazo):
    cantidadC = []
    cartas
    suma = 0
    for element in mazo:
        almacenador=[]
        suma = 0
        for carta in jugador:
            if carta == element:
                suma += 1
        almacenador.append(suma)
        cantidadC.append([element,almacenador])
    return cantidadC

#La función cartasAlfabeto toma como parámetro las cartas del jugador y retorna una lista con las letras del abecedario inglés y las cartas que empiezan por dichas letras. 
#Para esto se hace uso de un ciclo que compara la letra con la que inicia cada carta y la va agregando a lista junto a su letra del alfabeto con la que inicia. 
def cartasAlfabeto(jugador):
    cartasAlf = []
    abecedario = ["A", "B", "C", "D", "E", "F" , "G", "H", "I" , "J", "K", "L", 
                  "M", "N", "O", "P", "Q", "R", "S", "T" , "U", "V", "W", "X", "Y", "Z"]
    for letras in abecedario:
        almacenador=[]
        for carta in jugador:
            if carta[0]== letras:
                almacenador.append(carta)
        cartasAlf.append([letras,almacenador])
    return cartasAlf

#La función cartaLong tiene como parámetro de entrada las cartas del jugador y retorna una impresión con la carta de mayor y menor longitud. 
#Para esto se utiliza un for que recorre elemento por elemento hasta hallar el que tiene mayor y menor longitud. Por último, se imprimen los resultados obtenidos.  
def cartaLong(jugador):
    mayor, cartaMayor = len(jugador[0]), jugador[0]
    menor, cartaMenor = len(jugador[0]), jugador[0]
    for carta in jugador:
        if mayor < len(carta) :
            mayor = len(carta)
            cartaMayor = carta
            
        if menor > len(carta):
            menor = len(carta)
            cartaMenor = carta
            
    print("La carta de mayor longitud fue " + cartaMayor + " con una longitud de " + str(mayor) + 
          "; la carta de menor longitud fue " + cartaMenor + " con una longitud de " + str(menor) + "\n")

#La función iniCartPrem tiene como parámetro de entrada las cartas del jugador y retorna una impresión con las cartas que terminan con la(s) carta(s) premium encontradas en las cartas del jugador. 
#Para lo cual, se utiliza list comprehension para almacenar las cartas premium obtenidas de las cartas del jugador y después se crea un condicional para determinar si hubo premium o no. 
#En caso de habaer premium se utiliza un ciclo for con condicional para comprar la letra final de cada carta con la inicial de la premium, en caso de que ninguna coincida se imprimirá No hubo ninguna carta que terminará con la letra que inicia la premium. 
#Si no existe ninguna carta premium en las cartas del jugador entonces se imprimir No hubo premium. 
def iniCartPrem(jugador):
    prem = [cartas for cartas in jugador for cartPremium in premium if cartas==cartPremium]
    if len(prem) != 0:    
        prem_sin_repetidas = []
        for carta in prem:
            if carta not in prem_sin_repetidas:
                prem_sin_repetidas.append(carta.lower())
        carta_termina_premium = [carta for prem in prem_sin_repetidas for carta in jugador if carta[-1]==prem[0]]
        if len(carta_termina_premium) == 0 :
            print("No hubo ninguna carta que terminará con la letra que inicia la premium" + "\n")
        else: 
            print("Las cartas que terminan con la letra que empiezan la(s) premium: " + str(carta_termina_premium)+ "\n")
            
    else:
        print("No hubo premium"+ "\n")

#La función consecutivas recibe como parámetros la lista de jugador y retorna una impresión con las letras repetidas y las cartas a las que corresponden. 
#Para ello, utiliza un ciclo for que recorre carta por carta, luego otro ciclo for para recorrer letra por letra de la carta y para finalizar un condicional para verificar que la letra actual y la que le sigue son las mismas, es decir, consecutivas. 
#Por último, se realiza la impresión con los datos recolectados.  
def consecutivas(jugador):
    letrasConsecutivas = []
    cartasConsetuvias = []
    for carta in jugador:
        for i in range(len(carta)-1):
            if carta[i] == carta[i+1]:
                letrasConsecutivas.append(carta[i])
                cartasConsetuvias.append(carta)
    print("Las letras consecutivas son: " + str(letrasConsecutivas) + " en las cartas " + str(cartasConsetuvias))
    
#La función numero_letras recibe como parámetro la lista jugador, y crea una lista de listas con las letras del abecedario y la sumatoria total de la cantidad de veces que aparece cada letra del abecedario en los nombres de las cartas de la lista final de la lista jugador, por medio de ciclos y list comprehension. 
def numero_letras(jugador):
    player_copy = jugador.copy()
    abecedario = ["a", "b", "c", "d", "e", "f" , "g", "h", "i" , "j", "k", "l",
                  "m", "n", "o", "p", "q", "r", "s", "t" , "u", "v", "w", "x", "y", "z"]
    player_copy_minusculas = [ element.lower() for element in player_copy]
   
   
    numletras = []
    for i in range(0, len(abecedario)):
        suma = 0
        for element in player_copy_minusculas:
            for caracter in element:
                if caracter == abecedario[i]:
                    suma += 1
       
        numletras.append(suma)
   
    letras_con_numero = [[abecedario[i], numletras[i]] for i in range(0, len(abecedario)) ]
   
    return letras_con_numero

cartas = ["Payne" , "Hendrix", "Stone" , "Coffey" , "Whitaker" , "Pope" ,
          "Bleach" , "Arc" , "Fleming" , "Hardin" , "Robiar" , "Mccullough" ,
          "Mooney" , "Reynolds" , "Short" , "Stanton" , "Deadman" ,
          "Stonehammer" , "Smith" , "Patrick" , "Crane" , "Cargane" , "Powers"
          , "Wade" , "Joseph" , "Savage" , "Houston" , "Merritt" , "Nuke" ,
          "Barnett" , "Acosta" , "Duke" , "Sellers" , "Blake" , "Schneider" ,
          "Stone" , "Cannon" , "Garrison" , "Randall" , "Leon" , "Buck" ,
          "Shannon" , "Delaney" , "Mckinney" , "Dodademocles" , "Flowers" ,
          "Whitehead" , "Kirby" , "Park" , "Shannon" , "Vlad" , "Pepin" ,
          "Mcguire" , "Murray" , "Rush" , "Aramis" , "Fletcher", "Mcfadden" ,
          "Deleon" , "Luke" , "Lindsay" , "Payne" , "Gerbvo" , "Hubbard" ,
          "Burnett" , "Bryan" , "Ratliff" , "Carlson" , "Parsons" , "Deadmeat"
          , "Crimson" , "Wilson" , "Terry" , "Hancock" , "Hightower" , "Burns"
          , "Austin" , "Nightwalker" , "Thetis" , "Owen" , "Tate" , "Simmons"
          , "Grant" , "Barber" , "Talos" , "Ashes" , "Alston" , "Clayton" ,
          "Mcbride" , "Huffman" , "Lightbringer" , "Blankenship" , "Higgins" ,
          "Saint" , "Graham" , "Hodor" , "Ellison" , "Roberts" , "Odom" ,
          "Mann" ]

premium = ["AIVLIS", "LEIRBAG", "NAILUJ", "SOLRAC", "ANAID"]

imprimir(cartas)
imprimir(premium)

jugador = generador(cartas, 10)
juego = combinador(cartas, premium)

sobre_uno = generador(juego, 5)
sobre_dos = generador(juego, 5)
sobre_tres = generador(juego, 5)


paquete = combinador(sobre_uno, (sobre_dos + sobre_tres))


jugador = jugador + paquete
mazo = cartas + premium
cartasPremium(jugador)
print("Las cartas repetidas fueron: " + str(cartasRepetidas(jugador)) + "\n")
print("Carta y número de veces que aparece en cartas del jugador S(respectivamente): ", cantidadCartas(jugador, mazo), "\n")
print(str(cartasAlfabeto(jugador)) + "\n")
cartaLong(jugador)
iniCartPrem(jugador)
consecutivas(jugador)
print("Número de veces que aparece cada letra del alfabeto inglés en los nombres de las cartas de lista jugador: ", numero_letras(jugador))