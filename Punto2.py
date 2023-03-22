import math
from Punto1 import Punto1 as p1
"""
Aquí se supone que debemos poner lo que va interamente dentro del punto 2, y sólo definí la función :D
"""

class impares:
        
    def espacio_intervalo(n, h, a, b):
        print("INICIO SOLUCIÓN PUNTO 2")
        x=[a]

        for i in range(1,n+1):
            x.append(a+i*h)

        I=0

        for i in range(1,int((n-1)/2)+1):
            I+=p1.funcion(x[2*i])

        I*=2

        for i in range(1,int((n+1)/2)+1):
            I+=p1.funcion(x[2*i-1])
        
        I*=4

        I+= p1.funcion(b)
        I+= p1.funcion(a)
        I*=(h/3)
        print("La integral aproximada es: " + str(I))
        print("FIN SOLUCIÓN PUNTO 2")

