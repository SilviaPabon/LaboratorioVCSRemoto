# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 09:11:52 2020

@author: --
"""
presion = [110.06, 107.89, 108.45, 108.49, 109.03, 110.11, 109.87,                      
           119.38, 119.35, 116.34, 117.73, 120.01, 118.19, 119.53,
           117.09, 118.03, 118.65, 117.47, 117.49, 109.65, 110.44, 
           110.51, 107.38, 109.26, 106.18, 109.36, 106.61, 105.16, 
           110.11, 105.48, 108.37, 107.59, 108.91, 108.35, 109.57,
           122.56, 124.44, 125.97, 121.03, 121.22, 122.41, 122.15,
           124.52, 123.35, 125.76, 121.08, 122.29, 105.42, 110.67,
           107.73, 105.76, 107.85]

#Función que calcula la diferencia entre el mayor y el menor con la utilización de un for para hallar el valor mayor y menor de la lista
def difMayorMenor(presion):
    mayor = presion[0]
    menor = presion[0]
    for element in presion :
        if mayor < element :
            mayor = element
        if menor > element :
            menor = element
    dif = mayor - menor
    return dif

#La función media calcula el promedio de una lista. Utiliza un for para calcular la sumatoria de los elementos y luego los divide entre la cantidad sumada
def media(presion):
    suma = 0
    for element in presion:
        suma += element
    prom = suma/len(presion)
    return prom

#La función mediana calcula la mediana de una lista. Utiliza un ordenamiento burbuja, con ciclos y condicionales, para ordenar la lista de mayor a menor. 
#Después se identifica el número de elementos que contiene la lista, en caso de que sean par se saca el promedio de la mitad de sus elementos.
#En caso de ser impar, se toma el numero que divide en partes iguales la lista.
def mediana(presion):
    presionCopia = presion.copy()
    for j in range(0,len(presion)):
        for i in range(0,len(presion)-1):
            if presionCopia[i]>presionCopia[i+1]:
                orden=presionCopia[i]
                presionCopia[i]=presionCopia[i+1]
                presionCopia[i+1] = orden
    mitad=int(len(presion)/2)
    if (len(presion))%2==0 :
        mediana=(presionCopia[mitad]+presionCopia[mitad-1])/2
    else:
        mediana=presionCopia[mitad//1]
    return mediana

#La función semanas consecutivas obtiene las semanas consecutivas en que los valores del promedio semanal superaron al promedio anual y las que semanas en donde no lo hicieron.
def semanasconsecutivas(lista):
    prom = media(lista)
    sem = []
    for i in range(0, len(lista)):
        sem.append(i+1)        
    semanas = [ [], []]
    for j in range(0, len(lista)-1):
        
            if lista[j] > prom :
                if lista[j + 1] > prom :
                    semanas[0].append(sem[j])
                    if lista[j+1] == lista[len(lista)-1] :
                        semanas[0].append(sem[len(lista)-1])
                if lista[j + 1] < prom :
                    semanas[0].append(sem[j])
            if lista[j] < prom :
                if lista[j + 1] < prom :
                    semanas[1].append(sem[j])
                    if lista[j+1] == lista[len(lista)-1] :
                        semanas[1].append(sem[len(lista)-1])                            
    return semanas

#La función listadeListas obtiene los valores de las semanas en donde el promedio semanal supero al promedio anual y donde no lo hizo.
def listadeListas(lista):
    sem = semanasconsecutivas(lista)
    ListaMedia = [ [] , []]
    for i in range(0, len(sem[0])):
        valoresMayor = (sem[0][i]) - 1
        ListaMedia[0].append(lista[valoresMayor])
    for i in range(0, len(sem[1])):
        valoresMenor = (sem[1][i]) - 1
        ListaMedia[1].append(lista[valoresMenor])
    return ListaMedia

temperatura = []
for i in presion:
    t = round(((i*510)/(8.314472*17.16)),2)
    temperatura.append(t)

#La función desviación estándar calcula la desviación estándar de una lista, sumando todos los elementos mediante un for, a la par que se restan por el promedio y se potencian al cuadrado
#Una vez hecho lo anterior, se divide la suma obtenida entre la cantidad de numeros sumados y se potencia en 1/2.
def desviacionEstandar(temperatura):
    prom = media(temperatura)
    suma = 0
    for element in temperatura :
        suma += (element-prom)**2
    
    des = (suma/len(temperatura))**(1/2)
    return des

#-----------------------------------Principal---------------------------------#


print("La lista con los datos de presion promedio semanal es: " + str(presion) + "\n") 

print("La diferencia entre el mayor y menor es: " + str(difMayorMenor(presion)) + "\n")

print("La media de las presiones promedio es " + str(media(presion)) + " y la mediana es: " + str(mediana(presion)) + "\n")

SemConsecutivasPresion = semanasconsecutivas(presion)
listaPresionMedia = listadeListas(presion)
print("Las semanas en las que las presiones promedio que superan la media anual son: " + str(SemConsecutivasPresion[0]) + 
      " cuyos valores, respectivamente, son: "+ str(listaPresionMedia[0]) +  " y las semanas que estan por debajo son: " 
      + str(SemConsecutivasPresion[1]) +" cuyos valores, respectivamente, son: " + str(listaPresionMedia[1]) +  "\n")

print("La temperatura promedio semanal es: " + str(media(temperatura)) + "\n")

print("La desviación estándar de la temperatura promedio semanal es: " + str(desviacionEstandar(temperatura)) + "\n")

temperaturamedia = listadeListas(temperatura)
print("Las temperaturas promedio que superan la media anual son: " + str(temperaturamedia[0]) + 
      " y las que estan por debajo son: " + str(temperaturamedia[1]) + "\n")

print("La desviación estándar de las temperaturas superiores a la media es: " + str(desviacionEstandar(temperaturamedia[0])) + 
      " y la desviación de los más bajos de la media es " + str(desviacionEstandar(temperaturamedia[1])) + "\n")

desMayorMenorTemp = [desviacionEstandar(temperaturamedia[0]) , desviacionEstandar(temperaturamedia[1])]
print("La media de la desviación estándar de la temperatura mayor y menor que el promedio es: " + str(media(desMayorMenorTemp)))

