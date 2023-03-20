#f(x)=senx
#       x

import math
import random

class Punto1:
    def funcion(x):
        f = math.sin(x)/x
        return f
    
    def generar_random():
        x = random.randint(-999,999)
        if x==0:
            return Punto1.generar_random()
        return x
    
    def ejecutar():
        x = Punto1.generar_random()
        print("Valor de X: " + str(x))
        f = Punto1.funcion(x)
        print("Valor obtenido en la función: " + str(f))

Punto1.ejecutar()


"""
Se importan math y random, se crea un método función el cuál retorna una función que dependa de x,
se crea una función que genera aleatoriamente un valor de x, se crea la función de ejecutar
"""