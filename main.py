import math


def calculadora_segundo_grado(a,b,c):

    raiz =  math.sqrt( b**2 - (4 * a * c))
    x = (-b + raiz ) / (2 * a)
    y = (-b - raiz ) / (2 * a)

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
        aceleracion =float(input("Introduce la aceleracion >>"))

        a = aceleracion
        b = velocidad_incial
        c = espacio_incial - espacio_final

        calculadora_segundo_grado(a,b,c)


    elif eleccion == 3:

        espacio_final = float(input("Introduce el espacio final (x) >>"))
        tiempo = float(input("Introduce el tiempo (s) >>"))
        espacio_incial = float(input("Introduce el espacio inicia l>>"))
        velocidad_incial = float(input("Introduce la velocidad inicial >>"))

        aceleracion = (espacio_final - espacio_incial - (velocidad_incial * tiempo)) / (1/2 * (tiempo**2)

        print("Solucion: {}".format(aceleracion))


    elif eleccion == 4:

            












print(">>>>> ERROR <<<<<")
