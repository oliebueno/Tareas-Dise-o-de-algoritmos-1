def minimax(tablero, jugador_actual, alpha, beta):
    if hay_victoria(tablero):
        return eval(tablero)

    # Asigna + o - infinito para el jugador actual, según el caso
    mejor_puntuacion = float("-inf") if jugador_actual == "-" else float("inf")

    # Encuentra todos los movimientos válidos. Busca los sucesores del estado actual
    for movimiento in movimientos_validos:
        # Aplica el movimiento al tablero
        nuevo_tablero = aplicar_movimiento(tablero, movimiento, jugador_actual)
        # la función minimax se llama recursivamente con el nuevo tablero y el jugador opuesto
        puntuacion = minimax(nuevo_tablero, otro_jugador(jugador_actual))

        if jugador_actual == "-":
            mejor_puntuacion = max(mejor_puntuacion, puntuacion)
            alfa = max(alfa, mejor_puntuacion)
        else:
            mejor_puntuacion = min(mejor_puntuacion, puntuacion)
            beta = min(beta, mejor_puntuacion)

    return mejor_puntuacion
