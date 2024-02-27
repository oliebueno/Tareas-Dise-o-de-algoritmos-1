import matplotlib.pyplot as plt
import math
import networkx as graph

# Función que determina si un número es primo


def es_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# Función que crear un grafo bipartito dirigido


def crear_grafo_bipartito(C):
    G = graph.DiGraph()
    # Agregar nodos
    G.add_nodes_from(C)
    # Agregar aristas
    for x in C:
        for y in C:
            if x % 2 == 0 and es_primo(x + y):
                G.add_edge(x, y)
    return G

# Funcion de máximo emparejamiento usando el algoritmo de Hopcroft-Karp


def max_emparejamiento(G):
    A = {}
    while True:
        # Encontrar un camino aumentante
        P = buscar_camino_en_aumento(G, A)
        if not P:
            break
        for p in P:
            print(p)
            mejorar_emparejamiento(A, p)
    return A


# Función que busca un camino en aumento
# Función que busca un camino en aumento
def buscar_camino_en_aumento(G, A):
    # Inicializar las distancias de los nodos libres a cero
    dist = {}
    for x in G.nodes:
        if x not in A:
            dist[x] = 0
    # Inicializar la cola de la BFS con los nodos libres
    Q = [x for x in G.nodes if x not in A]
    # Inicializar el diccionario de padres para reconstruir los caminos
    parent = {}
    # Inicializar la bandera que indica si se ha encontrado un camino en aumento
    found = False
    # Mientras la cola no esté vacía y no se haya encontrado un camino en aumento
    while Q and not found:
        # Sacar el primer nodo de la cola
        u = Q.pop(0)
        # Para cada vecino de u
        for v in G.neighbors(u):
            # Si v no tiene distancia asignada
            if v not in dist:
                # Asignarle la distancia de u más uno
                dist[v] = dist[u] + 1
                # Asignarle a u como padre
                parent[v] = u
                # Si v está libre
                if v not in A.values():
                    # Marcar que se ha encontrado un camino en aumento
                    found = True
                    # Salir del bucle
                    break
                # Si v está emparejado
                else:
                    # Obtener el nodo con el que está emparejado v
                    w = A[v]
                    # Asignarle la distancia de v más uno
                    dist[w] = dist[v] + 1
                    # Asignarle a v como padre
                    parent[w] = v
                    # Añadir w a la cola
                    Q.append(w)
    # Si se ha encontrado un camino en aumento
    if found:
        # Inicializar la lista de caminos en aumento
        P = []
        # Para cada nodo libre del otro lado del grafo
        for y in [x for x in G.nodes if x not in A.values()]:
            # Si y tiene distancia asignada
            if y in dist:
                # Inicializar el camino en aumento desde y
                p = [y]
                # Mientras y tenga padre
                while y in parent:
                    # Añadir el padre de y al camino
                    p.append(parent[y])
                    # Actualizar y al padre de y
                    y = parent[y]
                # Invertir el orden del camino
                p.reverse()
                # Añadir el camino a la lista de caminos en aumento
                P.append(p)
        # Devolver la lista de caminos en aumento
        return P
    # Si no se ha encontrado ningún camino en aumento
    else:
        # Devolver una lista vacía
        return []


# Función que mejora el emparejamiento


def mejorar_emparejamiento(A, p):
    for i in range(0, len(p), 2):
        v1 = p[i]
        v2 = p[i + 1]
        # Si v1 esta enparejado con v2, se desenparejan
        if v1 in A:
            del A[v1]
        # Se enparejan v1 con v2
        else:
            A[v1] = v2


# Función para resolver el problema planteado


def resolver_problema(C):
    # Creamos el grafo bipartito a partir del conjunto C
    G = crear_grafo_bipartito(C)
    print(G.edges)
    # Encontramos el máximo emparejamiento del grafo
    M = max_emparejamiento(G)
    # Calculamos la cantidad de números que debemos eliminar
    print(M)
    k = len(M)
    # Devolvemos la respuesta
    return k


# Ejemplo de uso
C = [2, 3, 4, 5, 8, 16]
k = resolver_problema(C)
print(f"La menor cantidad de números que debe eliminarse de {C} es {k}")
