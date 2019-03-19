
import math
from sympy import *



def velocidad_descompuesta(v_0, B,):

    a = math.radians(B)

    v_0x = v_0 * math.cos(a)
    v_0y = v_0 * math.sin(a)

    lista = [v_0x, v_0y]

    return lista



v_0 = float(input("Introducir velocidad inical >>"))
B = float(input("Introduce el angulo de tiro >>"))

velocidad_descompuesta(v_0,B)

v_x = velocidad_descompuesta(v_0, B,)[0]
v_y = velocidad_descompuesta(v_0, B,)[1]

print(v_x)
print(v_y)
