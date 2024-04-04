def calcular_decomp(N):
    # Inicializamos un arreglo para contar las combinaciones de ab + cd = X
    contador = [0] * (N + 1)

    # Calculamos la cantidad de formas de descomponer cada número en dos factores
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            contador[j] += 1

    # Aplicamos la Criba de Eratóstenes modificada para calcular la suma de divisores
    suma_divisores = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            suma_divisores[j] += i

    # Calculamos decomp(X) para cada X y encontramos el máximo valor
    max_decomp = 0
    for X in range(1, N + 1):
        # Verificamos que el índice esté dentro del rango antes de acceder a la lista
        if suma_divisores[X] <= N:
            # La cantidad de combinaciones es el producto de los contadores de divisores de los sumandos
            decomp_X = contador[suma_divisores[X]] * \
                contador[X - suma_divisores[X]]
            max_decomp = max(max_decomp, decomp_X)

    return max_decomp


# Ejemplo de uso
N = 10  # Reemplazar con el valor deseado de N
print(calcular_decomp(N))
