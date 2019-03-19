
import math
from sympy import *
def velocidad_descompuesta(v_0, B):

    a = math.radians(B)

    v_0x = v_0 * math.cos(a)
    v_0y = v_0 * math.sin(a)

    print(v_0x)
    print(v_0y)


v_0 = float(input("Introducir velocidad inical >>"))
B = float(input("Introduce el angulo de tiro >>"))

velocidad_descompuesta(v_0,B)
