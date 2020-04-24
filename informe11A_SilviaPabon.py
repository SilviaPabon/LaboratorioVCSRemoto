# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 10:24:43 2020

@author: --
"""

# -------- Paquetes y librerías -------- #

import numpy as np

#  ------------- Funciones ------------- #

#                Puntos 1-7

# Se crea un una función llamada generador que por medio de dos ciclos for retorna un arreglo bidimensional con numeros psuedoaleatorios
def generador(min, max):
    arreglo = np.random.randint(min, max, size=(4, 12))
    return arreglo

#La función imprimir, imprime un arreglo bidimensional en forma de una tabla con ciudades y meses. Utiliza ciclo for y condicionales para crear los espacios entre los datos
def imprimir(array):
    ciudades = np.array(["Bucaramanga  ", "Floridablanca", "Giron        ", "Piedecuesta  "])
    print("Las dimensiones del arreglo son: " + str(array.shape))
    print('              Ene Feb Mar Abr May Jun Jul Ago Sep Oct Nov Dic')
    
    for i in range(0,4):
        print(str(ciudades[i]) + str(array[i]))
        
#La función restador resta dos arreglos bidimensionales
def restador(arrayA, arrayB): 
    arrayR = arrayA - arrayB
    return arrayR


#La función mejor_ciudad calcula la ciudad que obtuvo las mejores ganancias, usando un ciclo for para sumar las ganancias de cada ciudad y luego se comparan con un condicional.
def mejor_ciudad(ganancias):
    ciudades = np.array(['Bucaramanga', 'Floridablanca', 'Girón', 'Piedecuesta'])
    mejorGan = 0
    for i in range(0,4):
        ganCiudad = 0
        for x in range(0,12):
            ganCiudad += ganancias[i,x]
        if ganCiudad > mejorGan :
            mejorGan = ganCiudad
            ciudad = i
    print("La mejor ciudad es " + ciudades[ciudad])

#La función peor_ciudad calcula la ciudad que obtuvo las peores ganancias, usando un ciclo for para sumar las ganancias de cada ciudad y luego se comparan con un condicional.
#Se crea una variable llamado peorGan que será un valor imposible para el arreglo y de esta manera lograr obtener el numero más bajo de ganancias. 
def peor_ciudad(ganancias):
    
    ciudades = np.array(['Bucaramanga', 'Floridablanca', 'Girón', 'Piedecuesta'])
    peorGan = 9999999999999
    for i in range(0,4):
        ganCiudad = 0
        for x in range(0,12):
            ganCiudad += ganancias[i,x]
        if ganCiudad < peorGan :
            peorGan = ganCiudad
            ciudad = i
    print("La peor ciudad es " + ciudades[ciudad])

#La función mejor_mes calcula el mes en que se obtuvieron las mejores ganancias para cada ciudad.
#Se utiliza un ciclo for con condicional para comparar las ganacias de cada ciudad para obtener el mes con mayores ganancias.
def mejor_mes(ganancias):
    meses = np.array(['enero', 'febreo', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 
                      'octubre', 'noviembre', 'diciciembre']) 
    for i in range(0,4):
        mejorMes = ganancias[i,0]
        for x in range(0,12):
           if i==0 :
                if (mejorMes < ganancias[i,x]) :
                    mejorMes = ganancias[i,x]
                    mejorMesBuc = x
                if mejorMes == ganancias[i,0]:
                    mejorMesBuc = 0
           elif i==1 :
                if (mejorMes < ganancias[i,x]) :
                    mejorMes = ganancias[i,x]
                    mejorMesFlo = x   
                if mejorMes == ganancias[i,0]:
                    mejorMesFlo = 0
           elif i==2 :
                if (mejorMes < ganancias[i,x]) :
                    mejorMes = ganancias[i,x]
                    mejorMesGir = x
                if mejorMes == ganancias[i,0]:
                    mejorMesGir = 0
           else :
                if (mejorMes < ganancias[i,x]) :
                    mejorMes = ganancias[i,x]
                    mejorMesPie = x
                if mejorMes == ganancias[i,0]:
                    mejorMesPie = 0
    
    print("El mejor mes de bucaramanga es: " + str(meses[mejorMesBuc]))
    print("El mejor mes de Floridablanca es: " + str(meses[mejorMesFlo]))    
    print("El mejor mes de Girón es: " + str(meses[mejorMesGir])) 
    print("El mejor mes de Piedecuesta es: " + str(meses[mejorMesPie]))

#La función peor_mes calcula el mes en que se obtuvieron las peores ganancias. Utilizando un ciclo for con condicionales para este fin.
def peor_mes(ganancias):
    meses = np.array(['enero', 'febreo', 'marzo', 'abril', 'mayo', 'junio', 'julio', 
                      'agosto', 'septiembre', 'octtubre', 'noviembre', 'diciciembre']) 
    for i in range(0,4):
        peorMes = ganancias[i,0]
        for x in range(0,12):
           if i==0 :
                if (peorMes > ganancias[i,x]) :
                    peorMes = ganancias[i,x]
                    peorMesBuc = x
                if peorMes == ganancias[i,0]:
                    peorMesBuc = 0
           elif i==1 :
                if (peorMes > ganancias[i,x]) :
                    peorMes = ganancias[i,x]
                    peorMesFlo = x
                if peorMes == ganancias[i,0]:
                    peorMesFlo = 0
           elif i==2 :
                if (peorMes > ganancias[i,x]) :
                    peorMes = ganancias[i,x]
                    peorMesGir = x
                if peorMes == ganancias[i,0]:
                    peorMesGir = 0
           else :
                if (peorMes > ganancias[i,x]) :
                    peorMes = ganancias[i,x]
                    peorMesPie = x
                if peorMes == ganancias[i,0]:
                    peorMesPie = 0
    
    print("El peor mes de bucaramanga es: " + str(meses[peorMesBuc]))
    print("El peor mes de Floridablanca es: " + str(meses[peorMesFlo]))    
    print("El peor mes de Girón es: " + str(meses[peorMesGir])) 
    print("El peor mes de Piedecuesta es: " + str(meses[peorMesPie]))        
    
#La función imprimir_persolizado imprimime una tabla con los meses que se requira saber
def imprimir_personalizado(arr, inicio, fin):
    meses = np.array(['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'])
    ciudad = np.array(['  Bucaramanga', 'Floridablanca', '        Girón', '  Piedecuesta'])
    mes = ""
    for i in range(inicio-1, fin):
        mes += meses[i] + "   "
         
    print("\n" + str(arr.shape)  + "        " + mes,"\n")

    for i in range(0,4):
        espaciado = ""
        
        for j in range(inicio-1,fin):
            espaciado += str(int(arr[i,j]))
            
            if (arr[i,j] >= 100) or (arr[i,j] <= -10) :
                espaciado += "   "
            elif (arr[i,j] >= 10) or ((arr[i,j] >= -10) and (arr[i,j] < 0)) :
                espaciado += "    "
            else :
                espaciado += "     "    
                
        print(ciudad[i] + "  " + espaciado)
        
    print("\n")
#La función promedio calcula el promedio de ingresos, egresos y ganancias que se obtuvo en cada ciudad. 
#Se hace uso de ciclos y condicionales para este fin.
def promedio(ingresos, egresos, ganancias):
    for i in range(0,4):
        sumaIngresos,sumaEgresos,sumaGanacias = 0, 0, 0
        for x in range(0,12):
            sumaIngresos += ingresos[i,x]
            sumaEgresos += egresos[i,x]
            sumaGanacias += ganancias[i,x]
        if i == 0 :
            ingBuc, egrBuc, ganBuc = sumaIngresos, sumaEgresos, sumaGanacias
        elif i == 1:
            ingFlo, egrFlo, ganFlo = sumaIngresos, sumaEgresos, sumaGanacias
        elif i == 2:
            ingGir, egrGir, ganGir = sumaIngresos, sumaEgresos, sumaGanacias
        else :
            ingPie, egrPie, ganPie = sumaIngresos, sumaEgresos, sumaGanacias
        
    for i in range(0,4):
        if i == 0 :
            promIngr = ingBuc/len(ingresos[i])
            promEgre = egrBuc/len(egresos[i])
            promGan = ganBuc/len(ganancias[i])
            print("El promedio de ganancias de Bucaramanga es " + str(round(promIngr,2)) + ", el de egresos es " 
                  + str(round(promEgre,2)) + " y el de ganancias es " + str(round(promGan,2)))
        elif i == 1:
            promIngr = ingFlo/len(ingresos[i])
            promEgre = egrFlo/len(egresos[i])
            promGan = ganFlo/len(ganancias[i])
            print("El promedio de ganancias de Floridablanca es " + str(round(promIngr,2)) + ", el de egresos es " 
                  + str(round(promEgre,2)) + " y el de ganancias es " + str(round(promGan,2)))
        elif i == 2:
            promIngr = ingGir/len(ingresos[i])
            promEgre = egrGir/len(egresos[i])
            promGan = ganGir/len(ganancias[i])
            print("El promedio de ganancias de Girón es " + str(round(promIngr,2)) + ", el de egresos es "
                  + str(round(promEgre,2)) + " y el de ganancias es " + str(round(promGan,2)))
        else :
            promIngr = ingPie/len(ingresos[i])
            promEgre = egrPie/len(egresos[i])
            promGan = ganPie/len(ganancias[i])
            print("El promedio de ganancias de Piedecuesta es " + str(round(promIngr,2)) + ", el de egresos es " 
                  + str(round(promEgre,2)) + " y el de ganancias es " + str(round(promGan,2)))

#La funcipon promedio_2 calcula el promedio de ingresos, egresos y ganancias de cada ciudad con la expceción del valor más alto y más bajo
#Se utiliza ciclos y condcionales para calcular el valor mas alto y mas bajo, así como el promedio.
def promedio_2(ingresos, egresos, ganancias):
    print("\n")
    for i in range(4):
        mayoringb, mayoringf, mayoringg, mayoringp = ingresos [0,0], ingresos [1,0], ingresos [2,0], ingresos [3,0]    
        mayoregreb, mayoregref, mayoregreg, mayoregrep = egresos [0,0], egresos [1,0], egresos [2,0], egresos [3,0] 
        mayorgananb, mayorgananf, mayorganang, mayorgananp = ganancias[0,0], ganancias[1,0], ganancias[2,0], ganancias[3,0]   
        menoringb, menoringf, menoringg, menoringp = ingresos [0,0], ingresos [1,0], ingresos [2,0], ingresos [3,0]    
        menoregreb, menoregref, menoregreg, menoregrep = egresos [0,0], egresos [1,0], egresos [2,0], egresos [3,0] 
        menorgananb, menorgananf, menorganang, menorgananp = ganancias[0,0], ganancias[1,0], ganancias[2,0], ganancias[3,0]  
        for i in range(4):
            sumIngre, sumEgre, sumGanan = 0, 0, 0
            for x in range(12):
                sumIngre += ingresos[i, x]
                sumEgre += egresos[i, x]
                sumGanan += ganancias[i, x]
                if i == 0 :
                    if ((ingresos [0,x]) > mayoringb):
                        mayoringb = ingresos [0,x]
                    if egresos [0,x] > mayoregreb:
                        mayoregreb = egresos [0,x]
                    if ganancias [0,x] > mayorgananb:
                        mayorgananb = ganancias [0,x]
                    if ((ingresos [0,x]) < menoringb):
                        menoringb = ingresos [0,x]
                    if egresos [0,x] < menoregreb:
                        menoregreb = egresos [0,x]
                    if ganancias [0,x] < menorgananb:
                        menorgananb = ganancias [0,x]
                    ingBuc, egrBuc, ganBuc = sumIngre, sumEgre, sumGanan                     
                elif i == 1 :
                    if ((ingresos [1,x]) > mayoringf):
                        mayoringf = ingresos [1,x]
                    if egresos [1,x] > mayoregref:
                        mayoregref = egresos [1,x]
                    if ganancias [1,x] > mayorgananf:
                        mayorgananf = ganancias [1,x]
                    if ((ingresos [1,x]) < menoringf):
                        menoringf = ingresos [1,x]
                    if egresos [1,x] < menoregref:
                        menoregref = egresos [1,x]
                    if ganancias [1,x] < menorgananf:
                        menorgananf = ganancias [1,x]
                    ingFlo, egrFlo, ganFlo = sumIngre, sumEgre, sumGanan
                elif i == 2 :
                    if ((ingresos [2,x]) > mayoringg):
                        mayoringg = ingresos [2,x]
                    if egresos [2,x] > mayoregreg:
                        mayoregreg = egresos [2,x]
                    if ganancias [2,x] > mayorganang:
                        mayorganang = ganancias [2,x]
                    if ((ingresos [2,x]) < menoringg):
                        menoringg = ingresos [2,x]
                    if egresos [2,x] < menoregreg:
                        menoregreg = egresos [2,x]
                    if ganancias [2,x] < menorganang:
                        menorganang = ganancias [2,x]   
                    ingGir, egrGir, ganGir = sumIngre, sumEgre, sumGanan  
                else:
                    if ((ingresos [3,x]) > mayoringp):
                        mayoringp = ingresos [3,x]
                    if egresos [3,x] > mayoregrep:
                        mayoregrep = egresos [3,x]
                    if ganancias [3,x] > mayorgananp:
                        mayorgananp = ganancias [3,x]
                    if ((ingresos [3,x]) < menoringp):
                        menoringp = ingresos [3,x]
                    if egresos [3,x] < menoregrep:
                        menoregrep = egresos [3,x]
                    if ganancias [3,x] < menorgananp:
                        menorgananp = ganancias [3,x]
                    ingPie, egrPie, ganPie = sumIngre, sumEgre, sumGanan  
                       
    for i in range(0, 4):
        if i == 0 :
            promIngre = int(ingBuc-mayoringb-menoringb)/((len(ingresos[i]))-2)
            promEgre = (egrBuc-mayoregreb-menoregreb)/((len(ingresos[i]))-2)
            promGanan = (ganBuc-mayorgananb-menorgananb)/((len(ingresos[i]))-2)
            print("El promedio de ganancias de Bucaramanga es " + str(round(promIngre, 2)) + ", el de egresos es "
                  + str(round(promEgre, 2)) + " y el de ganancias es " + str(round(promGanan, 2)))
        elif i == 1 :
            promIngre = (ingFlo-mayoringf-menoringf)/((len(ingresos[i]))-2)
            promEgre = (egrFlo-mayoregref-menoregref)/((len(ingresos[i]))-2)
            promGanan = (ganFlo-mayorgananf-menorgananf)/((len(ingresos[i]))-2)
            print("El promedio de ganancias de Floridablanca es " + str(round(promIngre, 2)) + ", el de egresos es "
                  + str(round(promEgre, 2)) + " y el de ganancias es " + str(round(promGanan, 2)))
        
        elif i == 2 :
            promIngre = (ingGir-mayoringg-menoringg)/((len(ingresos[i]))-2)
            promEgre = (egrGir-mayoregreg-menoregreg)/((len(ingresos[i]))-2)
            promGanan = (ganGir-mayorganang-menorganang)/((len(ingresos[i]))-2)
            print("El promedio de ganancias de Girón es " + str(round(promIngre, 2)) + ", el de egresos es "
                  + str(round(promEgre, 2)) + " y el de ganancias es " + str(round(promGanan, 2)))
        else:
            promIngre = (ingPie-mayoringp-menoringp)/((len(ingresos[i]))-2)
            promEgre = (egrPie-mayoregrep-menoregrep)/((len(ingresos[i]))-2)
            promGanan = (ganPie-mayorgananp-menorgananp)/((len(ingresos[i]))-2)
            print("El promedio de ganancias de Piedecuesta es " + str(round(promIngre, 2)) + ", el de egresos es "
                  + str(round(promEgre, 2)) + " y el de ganancias es " + str(round(promGanan, 2)))

#La función extraer_proporciones calcula el porcentaje de los meses en donde hubo ganancias y el porcentaje de meses donde hubo perdidas para cada ciudad. Se utilizan ciclos y condicionales para calcular los porcentajes

def extraer_proporciones(ganancias):
    for i in range(0,4):
        ganNeg = 0
        gan = 0
        for x in range(0,12):
            if ganancias[i,x] > 0 :
                gan += 1
            else:
                ganNeg += 1
        gan = (gan*100)/len(ganancias[i])
        ganNeg = (ganNeg*100)/len(ganancias[i])
        if i == 0 :
            print("El porcentaje de ganancias de los meses en Bucaramanga es: " + str(round(gan,2)) + "%" +" y el de pérdidas es " + str(round(ganNeg,2)) + "%")
        elif i == 1:
            print("El porcentaje de ganancias de los meses en Floridablanca es: " + str(round(gan,2)) + "%" +" y el de pérdidas es " + str(round(ganNeg,2)) + "%")
        elif i== 2 :
            print("El porcentaje de ganancias de los meses en Girón es: " + str(round(gan,2)) + "%" +" y el de pérdidas es " + str(round(ganNeg,2)) + "%")
        else: 
            print("El porcentaje de ganancias de los meses en Piedecuesta es: " + str(round(gan,2)) + "%" +" y el de pérdidas es " + str(round(ganNeg,2)) + "%")

#La función generador3D retorna dos arreglos tridimensionales teniendo como entrada dos arreglos bidimensionales. Se utiliza ciclos para obtener los arreglos tridimensionales. 
def generador3D(ingresos,egresos):
    
    ingresos3D = np.zeros([5,4,12])
    ingresos3D[0] = ingresos
    egresos3D = np.zeros([5,4,12])
    egresos3D[0] = egresos
    for i in range(1,5):
        for x in range(0,4):
            for j in range(0,12):
                ingresos3D[i,x,j] = ((ingresos[x,j])/1.095)//1
                ingresos[x,j] = ingresos3D[i,x,j]
                egresos3D[i,x,j] = ((egresos[x,j])/1.056)//1
                egresos[x,j] = egresos3D[i,x,j]
        
    return (ingresos3D, egresos3D)

#La función Imprimir3D imprime un arreglo tridimensional en formato de tabla para hacerlo más comprensible al usuario     
def imprimir3D(arr):
    meses = np.array(['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'])
    ciudad = np.array(['  Bucaramanga', 'Floridablanca', '        Girón', '  Piedecuesta'])
    mes = ""
    años = np.array(['2019', '2018', '2017', '2016', '2015'])
    for i in range(0,12):
        mes += meses[i] + "   "

    mes2 = np.array([mes, mes, mes, mes, mes])

    for x in range(0,5):
        print("\n" + str(arr.shape) +"                                   Año " + str(años[x]), "\n" 
              +"               "+str(mes2[x]))
        for i in range(0,4):
            espaciado = ""
            
            for j in range(0,12):
                mes += meses[i] + "   "
                espaciado += str(int(arr[x,i,j]))
                
                
                if (arr[x,i,j] >= 100) or (arr[x,i,j] <= -10) :
                    espaciado += "   "
                elif (arr[x,i,j] >= 10) or ((arr[x,i,j] >= -10) and (arr[x,i,j] < 0)) :
                    espaciado += "    "
                else :
                    espaciado += "     "    
        
            print(ciudad[i] + "  " + espaciado)
    print("\n")    

#La función calcular_ganancias3D calcula la resta de dos arreglos tridimensionales, obteniendo un arreglo tridimensional de salida. 
def calcular_ganancias3D(ingresos3D, egresos3D):
    ganancias3D = ingresos3D - egresos3D
    return ganancias3D


#----------------------------Principal------------------------------------------#
#Punto 2
ingresos = generador(100,180) 
egresos = generador(60,130)
#Punto 6
ganancias = restador(ingresos,egresos)
#Puntos 3 y 7 
imprimir(ingresos)
imprimir(egresos)
imprimir(ganancias)

#Puntos 8.1, 8.2
mejor_ciudad(ganancias)
peor_ciudad(ganancias)

#Puntos 8.3, 8.4
mejor_mes(ganancias)
peor_mes(ganancias)

#Punto 8.5
imprimir_personalizado(ingresos, 3, 6)

#Punto 8.6, 8.7
promedio(ingresos, egresos, ganancias)
promedio_2(ingresos,egresos, ganancias)

#Punto 8.8
extraer_proporciones(ganancias)

#Punto 9
arr3D = generador3D(ingresos,egresos)
ingresos3D = arr3D[0]
egresos3D = arr3D[1]
#Punto 12
ganancias3D = calcular_ganancias3D(ingresos3D, egresos3D)

#Punto 11
imprimir3D(ingresos3D)
imprimir3D(egresos3D)

#Punto 13
imprimir3D(ganancias3D)