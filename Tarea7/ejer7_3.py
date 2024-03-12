def encontrar_subcadena_maxima(S):
    # Crear la tabla de saltos utilizando el algoritmo de KMP
    b = [0] * len(S)
    j = 0
    for i in range(1, len(S)):
        while j > 0 and S[i] != S[j]:
            j = b[j-1]
            print(j)

        # Condición por caracter repetidos
        if S[i] == S[j]:
            j += 1
        b[i] = j

    print(b)

    # El último valor de la tabla de saltos nos da la longitud de la subcadena más grande
    longitud = b[-1]

    # Retornar la subcadena más grande o "λ" si no hay ninguna
    if longitud == 0:
        return "λ"
    else:
        return S[:longitud]
