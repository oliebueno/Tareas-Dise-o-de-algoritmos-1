def calcular_lejania(puntos):
    # Ordenamos los puntos por su coordenada x; en caso de empate, por y
    puntos_ordenados_x = sorted(puntos, key=lambda punto: (punto[0], punto[1]))

    # Precalculamos los máximos de x e y para cada posible partición
    max_x_derecha = [0] * len(puntos)
    max_y_derecha = [0] * len(puntos)
    max_x_actual = max_y_actual = 0

    for i in range(len(puntos) - 1, -1, -1):
        punto = puntos_ordenados_x[i]
        max_x_actual = max(max_x_actual, abs(punto[0]))
        max_y_actual = max(max_y_actual, abs(punto[1]))
        max_x_derecha[i] = max_x_actual
        max_y_derecha[i] = max_y_actual

    # Inicializamos la lejanía mínima a un valor alto
    lejania_minima = float('inf')
    particion_optima = []
    max_x_izquierda = max_y_izquierda = 0

    # Exploramos las particiones posibles
    for i in range(1, len(puntos)):
        punto = puntos_ordenados_x[i - 1]
        max_x_izquierda = max(max_x_izquierda, abs(punto[0]))
        max_y_izquierda = max(max_y_izquierda, abs(punto[1]))

        # Calculamos la lejanía de cada subconjunto utilizando los valores precalculados
        lejania_C1 = max_x_izquierda * max_y_izquierda
        lejania_C2 = max_x_derecha[i] * max_y_derecha[i]

        # Actualizamos la lejanía mínima y la partición óptima si es necesario
        lejania_actual = lejania_C1 + lejania_C2
        if lejania_actual < lejania_minima:
            lejania_minima = lejania_actual
            particion_optima = [puntos_ordenados_x[:i], puntos_ordenados_x[i:]]

    return particion_optima, lejania_minima

# Función para calcular la lejanía de un conjunto de puntos


def lejania(conjunto):
    max_x = max(conjunto, key=lambda punto: punto[0])[0]
    max_y = max(conjunto, key=lambda punto: punto[1])[1]
    return abs(max_x) * abs(max_y)


# Ejemplo de uso
puntos = [(8, 3), (2, 5), (3, 7), (5, 11), (1, 13)]
particion, lejania = calcular_lejania(puntos)
print("Partición óptima:", particion)
print("Lejanía mínima:", lejania)
