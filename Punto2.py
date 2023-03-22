import math


"""
Aquí se supone que debemos poner lo que va interamente dentro del punto 2, y sólo definí la función :D
"""

class impares:
    def definir_n():
        try:
            n = int(input("Por favor ingrese el valor de n (debe ser impar): "))
            if n<=0:
                print("n debe ser mayor de 0")
                return impares.definir_n()
            elif n%2==0:
                print("n debe ser impar")
                return impares.definir_n()
            else:
                return n
        except:
            print("Debe ingresar un número")
            return impares.definir_n()
        
    def definir_intervalo(n):
        try:
            a = int(input("Por favor ingrese el valor de a (límite inferior): "))
            b = int(input("Por favor ingrese el valor de b (límite superior): "))
            if b<=a:
                return impares.definir_intervalo()
            else:
                h = (b-a)/n
                return h,a,b
        except:
            print("Debe ingresar un número")
            return impares.definir_intervalo()
        
    def espacio_intervalo():
        n = impares.definir_n()
        h,a,b = impares.definir_intervalo(n)
        lista_intervalos = []
        x=[a]

        for i in range(1,n+1):
            x.append(a+i*h)

        I=0

        for i in range(1,(n-1)/2+1):
            I+=math.sin(x[2*i])