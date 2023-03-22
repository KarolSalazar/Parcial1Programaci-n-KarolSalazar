import math
from Punto2 import impares
from Punto1 import Punto1 as p1
"""
Aquí se supone que debemos poner lo que va interamente dentro del punto 3, y sólo definí la función :D
"""

class derivadas:
    def definir_derivadas(n,h,a,b):
        print("INICIO SOLUCIÓN PUNTO 3")
        primera_derivada = (p1.funcion(a+h)-p1.funcion(a-h))/(2*h)
        segunda_derivada = (p1.funcion(a+h)-2*p1.funcion(a)+p1.funcion(a-h))/(h*h)

        print("Primera derivada: " + str(primera_derivada))
        print("Segunda derivada: " + str(segunda_derivada))
        print("FIN SOLUCIÓN PUNTO 3")

