
from sympy import *
import math



def calculadora_segundo_grado(a, b, c):

    raiz = math.sqrt(b**2 - (4 * a * c))
    x = (-b + raiz) / (2 * a)
    y = (-b - raiz) / (2 * a)

    print("Solucion 1: {}".format(x))
    print("Solucion 2: {}".format(y))


def menu():

    print("Seleccion una opcion >>")
    print("\t 1) Incognita del espacio (x)")
    print("\t 2) Incognita del tiempo (x)")
    print("\t 3) Incognita del aceleracion (x)")
    print("\t 4) Tiro parabolico")


menu()

eleccion = int(input("Introduce una opcion >>"))

lista = [1, 2, 3, 4]

while eleccion in lista:

    if eleccion == 1:

        tiempo = float(input("Introduce el tiempo (s) >>"))
        espacio_incial = float(input("Introduce el espacio inicia l>>"))
        velocidad_incial = float(input("Introduce la velocidad inicial >>"))
        aceleracion =float(input("Introduce la aceleracion >>"))

        espacio = espacio_incial + (velocidad_incial * tiempo) - ((aceleracion * (tiempo**2)) / 2)

        print("Solucion: {}".format(tiempo))

    elif eleccion == 2:

        espacio_final = float(input("Introduce el espacio final (x) >>"))
        espacio_incial = float(input("Introduce el espacio inicia l>>"))
        velocidad_incial = float(input("Introduce la velocidad inicial >>"))
        aceleracion = float(input("Introduce la aceleracion >>"))

        a = aceleracion
        b = velocidad_incial
        c = espacio_incial - espacio_final

        calculadora_segundo_grado(a, b, c)


    elif eleccion == 3:

        espacio_final = float(input("Introduce el espacio final (x) >>"))
        tiempo = float(input("Introduce el tiempo (s) >>"))
        espacio_incial = float(input("Introduce el espacio inicia l>>"))
        velocidad_incial = float(input("Introduce la velocidad inicial >>"))
        celeracion = ((espacio_final - espacio_incial) - (velocidad_incial * tiempo) / (1/2 * (tiempo**2)))

        print("Solucion:")


    elif eleccion == 4:

        def menu_parabolico():

            print("Seleccion una opcion >>")
            print("\t 1) Dadas la velocidad inical y el angulo calcular valores basicos")
            print("\t 2) Introduciendo el tiempo calcular la altura en ese instante")
            print("\t 3) Introduciendo la altura calcular el insatnte de tiempo")
            print("\t 4) Salir")


        def velocidad_descompuesta(v_0, B,):

            a = math.radians(B)

            v_0x = v_0 * math.cos(a)
            v_0y = v_0 * math.sin(a)

            lista = [v_0x, v_0y]

            return lista

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


        def alcance_tiempo(y_0,v_y,t):

            y = y_0 + v_y * t- 4.8 * t ** 2

            return y




        menu_parabolico()

        eleccion_4 = int(input("Introduce una opcion >>"))

        if eleccion_4 == 1:

            v_0 = float(input("Introducir velocidad inicial >>"))
            B = float(input("Introduce el angulo de tiro >>"))
            y_0 = float(input("Introduce la altura inicial (0) >>"))



            velocidad_descompuesta(v_0,B)

            v_x = velocidad_descompuesta(v_0, B,)[0]
            v_y = velocidad_descompuesta(v_0, B,)[1]


            alcance_max(y_0,v_y,v_0)

            t_xmax = alcance_max(y_0,v_y,v_0)[0]
            x_xmax = alcance_max(y_0,v_y,v_0)[1]



            print("--------------------------------------------------------\n")
            print("\n El tiempo transcurrido es {} segundos\n".format(t_xmax))
            print("\n La distancia recorrida es {} metros\n".format(x_xmax))
            print("\n La altura maxima es {} metros\n".format(altura_max(y_0,v_y)))
            print("--------------------------------------------------------")

        elif eleccion_4 == 2:

                v_0 = float(input("Introducir velocidad inicial >>"))
                B = float(input("Introduce el angulo de tiro >>"))
                y_0 = float(input("Introduce la altura inicial (0) >>"))
                t = float(input("Introduce el tiempo >>"))


                velocidad_descompuesta(v_0,B)

                v_x = velocidad_descompuesta(v_0, B,)[0]
                v_y = velocidad_descompuesta(v_0, B,)[1]

                print("La altura en el instante {}s es de {} metros".format(t,alcance_tiempo(y_0,v_y,t)))


        end;
print("\n>>>>> ERROR <<<<<")
print("\nSelecciona ua opcion correcta")
