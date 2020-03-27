# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:55:48 2020

@author: --
"""
#%%
#Ejercicio 5
a = float(input("Ingrese el primer número: "))
c = float(input("Ingrese el segundo número: "))

print("El resultado es el siguiente: " + str(a*c))
print("El resultado es el siguiente: " + str(a*2))

#%%
#Modificación de codificación
b = int(input("Ingrese el primer número: "))
print("El resultado del cuadrado del número es: " + str(b**2))

d = float(input("Ingrese el segundo número: "))
print("La raíz cuadrada del número es: " + str(d**(1/2)))

#%%
#Desarrollo de solución simple
a = int(input ("Ingrese el valor de a: "))
b = int(input ("Ingrese el valor de b: "))
c = int(input ("Ingrese el valor de c: "))

d = b**2-4*a*c

if d < 0:
    print("No existe ecuación cuadrática dentro del dominio de los reales")
elif d > 0:
    print("X1 es igual a: "+ str((-b+(d**1/2))/2*a))
    print("X2 es igual a: "+ str((-b-(d**1/2))/2*a))
elif d == 0:
    print("X1 y X2 equivalen a "+ str(-b/2*a))
