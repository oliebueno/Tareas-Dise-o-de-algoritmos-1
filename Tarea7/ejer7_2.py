import math

# Función para determinar la orientación de tres puntos. Devuelve 0 si los puntos son colineales, 1 si va a la derecha y -1 si va a la izquierda


def orientacion(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1

# Función para encontrar el punto con la coordenada más baja y más a la derecha en caso de empate


def punto_inicio(P):
    punto_inicial = min(P, key=lambda p: (p[1], -p[0]))
    return punto_inicial

# Función para encontrar el Convex Hull de un conjunto de puntos


def convex_hull(P):
    n = len(P)
    if n < 3:
        return P

    # Encontramos el punto con la coordenada y más baja (y más a la izquierda en caso de empate)
    punto_inicial = punto_inicio(P)

    # Ordenamos los puntos según su ángulo polar respecto al punto inicial
    P.sort(key=lambda p: (
        math.atan2(p[1] - punto_inicial[1], p[0] - punto_inicial[0]), p))

    # Creamos una pila para almacenar los puntos del Convex Hull
    stack = [punto_inicial]
    stack.append(P[1])

    for i in range(2, n):
        while len(stack) > 1 and orientacion(stack[-2], stack[-1], P[i]) != -1:
            stack.pop()
        stack.append(P[i])

    return stack

# Función para contar las capas de un conjunto de puntos


def contar_capas(P):
    num_capas = 0
    while P:
        convex_hull_points = convex_hull(P)
        num_capas += 1
        # Eliminamos los puntos extremos del Convex Hull
        for p in convex_hull_points:
            print(num_capas)
            P.remove(p)

    return num_capas
