#f(x)=senx

import math
import random

class Punto1:
    def funcion(x):
        f = math.sin(x)
        return f
    
    def generar_random():
        x = random.randint(-999,999)
        #if x==0:
        #    return Punto1.generar_random()
        return x
    
    def ejecutar():
        print("INICIO SOLUCIÓN PUNTO 1")
        x = Punto1.generar_random()
        print("Valor de X: " + str(x))
        f = Punto1.funcion(x)
        print("Valor obtenido en la función: " + str(f))
        print("FIN SOLUCIÓN PUNTO 1")



"""
Se importan math y random, se crea un método función el cuál retorna una función que dependa de x,
se crea una función que genera aleatoriamente un valor de x, se crea la función de ejecutar
"""