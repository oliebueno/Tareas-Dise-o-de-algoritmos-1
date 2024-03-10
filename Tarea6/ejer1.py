import random

# Clase que implementa un nodo de un treap implicito


class Node:
    # Constructor
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None

    # Método que retorna la representación en string del nodo
    def __str__(self):
        return str(self.key) + " " + str(self.priority)

# Clase que implementa un treap implicito


class ImplicitTreap:
    # Constructor
    def __init__(self):
        self.root = None

    # Metodo split
    def split(self, root, key):
        if root == None:
            return (None, None)
        if key <= root.key:
            left, right = self.split(root.left, key)
            root.left = right
            right = root
        else:
            left, right = self.split(root.right, key)
            root.right = left
            left = root
        return (left, right)

    # Metodo merge
    def merge(self, left, right):
        if left == None:
            return right
        if right == None:
            return left
        if left.priority > right.priority:
            left.right = self.merge(left.right, right)
            return left
        else:
            right.left = self.merge(left, right.left)
            return right

    # Metodo insert
    def insert(self, key, priority):
        if self.root == None:
            self.root = Node(key, priority)
        else:
            left, right = self.split(self.root, key)
            self.root = self.merge(self.merge(
                left, Node(key, priority)), right)

    # Metodo multiswap
    def multiswap(self, a, b, N):
        if a == None or b == None:
            return

        tam = min(b-a, N-b+1)
        T1, T2 = self.split(self.root, a)
        T2, T3 = self.split(T2, b)
        T2, T2r = self.split(T2, a+tam)
        T3, T3r = self.split(T3, b+tam)
        T1 = self.merge(T1, T3)
        T1 = self.merge(T1, T2r)
        T1 = self.merge(T1, T2)
        T1 = self.merge(T1, T3r)
        return (T1)

    # Metodo inorder
    def inorder(self, node):
        if node != None:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)


# Programa principal
def main():
    # Creamos un treap implicito
    treap = ImplicitTreap()
    # pedimos al usuario que ingrese el tamaño del treap implicito
    print("Ingrese el tamaño del arreglo: ")
    N = int(input())
    print("Ingrese el rango de los elementos. ")
    print("Ingrese el rango inferior: ")
    a = int(input())
    print("Ingrese el rango superior: ")
    b = int(input())
    # Insertamos elementos aleatorios en el treap implicito
    for i in range(1, N+1):
        treap.insert(i, random.randint(1, 1000000000))
    # Imprimimos el treap implicito
    print("Arreglo original:")
    treap.inorder(treap.root)
    print()
    # Realizamos un multiswap
    treap.root = treap.multiswap(a, b, N)
    # Imprimimos el treap implicito
    treap.inorder(treap.root)
    print()


# Llamamos al programa principal
__init__ = main()
