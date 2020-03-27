# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:45:33 2020

@author: --
"""


#%%
#Ejercicio 19 hoja de modelado
# x1, y1, x2, y2 se refiere a las coordenadas
print("Ingrese los dos valores de la primera coordenada")
x1 = int(input ("Ingrese el valor de X1: "))
y1 = int(input ("Ingrese el valor de Y1: "))
print("Ingrese los dos valores de la segunda coordenada")
x2 = int(input ("Ingrese el valor de X2: "))
y2 = int(input ("Ingrese el valor de Y2: "))

#Aquí se realiza el cálculo de la distancia euclidiana con su fórmula
print("La distancia euclidiana es: " + str((((x2-x1)**2)+((y2-y1)**2))**(1/2)))

#%%
#Ejercicio 30 hoja de modelado

# n1,n2,n3,n4,n5 se refiere a la entrada de las 5 notas del estudiante
n1 = float(input ("Ingrese el valor de la primera nota: "))
n2 = float(input ("Ingrese el valor de la segunda nota: "))
n3 = float(input ("Ingrese el valor de la tercera nota: "))
n4 = float(input ("Ingrese el valor de la cuarta nota: "))
n5 = float(input ("Ingrese el valor de la quinta nota: "))

#Aquí se realiza el cálculo de la nota final teniendo en cuenta su valor porcentual
nf = ((n1*0.15)+(n2*0.20)+(n3*0.15)+(n4*0.30)+(n5*0.20))

#Aquí se realizan
if nf<2:
    print("La nota final es: " + str(nf))
    print("No podrá habilitar")
elif ((nf>=2.0) and (nf<3.0)):
    print("La nota final es: " + str(nf))
    print("Ha reprobado")
elif ((nf>=3.0) and (nf<=4.5)):
    print("La nota final es: " + str(nf))
    print("Ha aprobado")
elif nf>4.5:
    print("La nota final es: " + str(nf))
    print("Felicitaciones, aprobó")

#%%
#Ejercicio número 6 del preinforme, definición de funciones
#Ejemplo 6.1
def launch_missiles():
    print("Missiles launched!")
    
launch_missiles()

#%%
#Ejemplo 6.2
def square (x):
    x_squared = x**2
    return x_squared
number=2
number_squared=square (number)
print(number, "al cuadrado es", number_squared)

#%%
#Ejemplo 6.3
def even_or_odd(n):
    if n % 2 == 0:
        print("even")
        return
    print("odd")
even_or_odd(4)

even_or_odd(5)

#%% Punto 7

 

#Ejemplos de los tipos de funciones en Python

 

#Función Aritmética

 

n=int(input("Ingrese un numero: "))
va=abs(n)
print(va)

 

#funcion de cadena

 

c=input("Ingrese una frase: ")

 

Lista = c.split()

 

print (Lista)

 

#Función importada

 

from math import pi
x=pi
print(x)

 

#Función definida por uno
n=int(input("Ingrese un numero: "))
a=int(input("Ingrese un numero: "))
def suma(n,a):
    print(n + a)
suma(n,a)



