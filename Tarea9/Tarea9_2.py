import numpy as np


def es_inversa(A, B, e, k):
    n = A.shape[0]
    for _ in range(k):
        # Se genera el vector aleatorio
        x = np.random.rand(n, 1)

        # Se multiplica A por x
        y = np.dot(A, x)

        # Se multiplica B por y
        x_prima = np.dot(B, y)

        # Diferencia entre x_prima y x
        error = np.linalg.norm(x_prima - x)

        if error > e:
            return False

    return True


# Ejemplo de uso

epsilon = 0.00001
k = 100
A = np.array([[1, 0, 3], [0, 5, -1], [0, 0, 3]])
B = np.array([[1, 0, -1], [0, 1/5, 1/15], [0, 0, 1/3]])

if es_inversa(A, B, epsilon, k):
    print("B es la matriz inversa de A.")
else:
    print("B no es la matriz inversa de A.")
