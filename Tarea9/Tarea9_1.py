import random


def millRab(n):
    a = random.randrange(2, n - 1)
    print(f"Testigo a: {a}")
    return btest(a, n)


def millRabRep(n, k):
    for i in range(1, k+1):
        print(f"\nIteración {i}:")
        if (not (millRab(n))):
            print("Se encontró un testigo que indica que el número es compuesto.")
            return False
    print("\nDespués de todas las iteraciones, el número es probablemente primo.")
    return True


def btest(a, n):
    s = 0
    t = n-1

    while (t % 2 == 0):
        s = s+1
        t = t // 2
    print(f"Valores de s: {s}, t: {t}")

    x = pow(a, t, n)
    print(f"Valor inicial de x: {x}")
    if (x == 1 or x == n-1):
        return True

    for i in range(1, s):
        x = pow(x, 2, n)
        print(
            f"Valor de x en la iteración {i} del bucle interno de la función btest: {x}")
        if (x == n-1):
            return True
    return False


print(millRabRep(151019215101921510191, 10))
