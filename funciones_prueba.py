
import math
from sympy import *
"""
x = Symbol('x')

y = solve(x**2 + 4*x -17)

print(y)
"""

v_0 = float(input("Introducir velocidad inical >>"))
a = float(input("INtroduce el angulo de tiro >>"))

def velocidad_descompuesta(v_0,a):

    v_0x = v_0 * math.cos(a)
    v_0y = v_0 * math.sin(a)

    return v_0x
    return v_0y


"""
Calcular primero el punto mas alto
"""

velocidad_descompuesta(v_0,a)

v_0x = velocidad_descompuesta(v_0)

print(v_0x)
