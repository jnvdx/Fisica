

import math
from sympy import *



def velocidad_descompuesta(v_0, B,):

    a = math.radians(B)

    v_0x = v_0 * math.cos(a)
    v_0y = v_0 * math.sin(a)

    lista = [v_0x, v_0y]

    return lista



v_0 = float(input("Introducir velocidad inicial >>"))
B = float(input("Introduce el angulo de tiro >>"))
y_0 = float(input("Introduce la altura inicial (0) >>"))


velocidad_descompuesta(v_0,B)

v_x = velocidad_descompuesta(v_0, B,)[0]
v_y = velocidad_descompuesta(v_0, B,)[1]



def altura_max(y_0,v_y):

    t_ymax = v_y / 9.8

    y_max = y_0 + v_y * t_ymax - 4.8 * t_ymax ** 2


    return y_max

def alcance_max(y_0,v_y,v_0):

    v_0f = v_0

    t_xmax = 2 * (v_y / 9.8)

    x_max = v_0f * t_xmax

    lista = [t_xmax, x_max]

    return lista

alcance_max(y_0,v_y,v_0)

t_xmax = alcance_max(y_0,v_y,v_0)[0]
x_xmax = alcance_max(y_0,v_y,v_0)[1]






print("--------------------------------------------------------\n")
print("\n El tiempo transcurrido es {} segundos\n".format(t_xmax))
print("\n La distancia recorrida es {} metros\n".format(x_xmax))
print("\n La altura maxima es {} metros\n".format(altura_max(y_0,v_y)))
print("--------------------------------------------------------")
