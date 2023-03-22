import math
from Punto1 import Punto1 as p1
from Punto2 import impares
from Punto3 import derivadas

class definicion_numeros:
    def definir_n():
        try:
            n = int(input("Por favor ingrese el valor de n (debe ser impar): "))
            if n<=0:
                print("n debe ser mayor de 0")
                return definicion_numeros.definir_n()
            elif n%2==0:
                print("n debe ser impar")
                return definicion_numeros.definir_n()
            else:
                return n
        except:
            print("Debe ingresar un número")
            return definicion_numeros.definir_n()
        
    def definir_intervalo(n):
        try:
            a = int(input("Por favor ingrese el valor de a (límite inferior): "))
            b = int(input("Por favor ingrese el valor de b (límite superior): "))
            if b<=a:
                return definicion_numeros.definir_intervalo(n)
            else:
                h = (b-a)/n
                return h,a,b
        except:
            print("Debe ingresar un número")
            return definicion_numeros.definir_intervalo(n)

p1.ejecutar()
n = definicion_numeros.definir_n()
h,a,b = definicion_numeros.definir_intervalo(n)
impares.espacio_intervalo(n,h,a,b)
derivadas.definir_derivadas(n,h,a,b)