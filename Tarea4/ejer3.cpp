#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

// clase que implementa la inicializacion virtual
class InicializacionVirtual
{
public:
    int tamaño;
    int *T;
    int *a;
    int *b;
    int ctr = 0;

    InicializacionVirtual(int n) : tamaño(n), T(new int[n]), a(new int[n]), b(new int[n])
    {
    }

    void asignar(int pos, int val)
    {
        if (pos < 0 || pos >= tamaño)
        {
            printf("Posición fuera de rango\n");
            return;
        }
        T[pos] = val;
        a[ctr] = pos;
        b[pos] = ctr;
        ctr++;
    }

    bool consultar(int pos)
    {
        if (pos < 0 || pos >= tamaño)
        {
            printf("Posición fuera de rango\n");
            return false;
        }

        if (0 <= b[pos] && b[pos] <= ctr)
        {
            if (a[b[pos]] == pos)
            {
                return true;
            }
            else
            {
                return false;
            }
        }
        else
        {
            return false;
        }
    }

    void limpiar()
    {
        ctr = 0;
    }

    void borrar_salir()
    {
        delete[] T;
        delete[] a;
        delete[] b;
    }
};

int main()
{
    printf("Introduzca el tamaño del arreglo: ");
    int n;
    cin >> n;
    cin.ignore();
    InicializacionVirtual ini_vir(n);

    // Menu
    while (true)
    {
        printf("Introduzca un comando: \n");
        printf("ASIGNAR POS VAL\n");
        printf("CONSULTAR POS\n");
        printf("LIMPIAR\n");
        printf("SALIR\n");
        printf("\n");
        printf("Comando: ");

        string comando;
        getline(cin, comando);

        string comando1 = comando.substr(0, comando.find(" "));
        if (comando1 == "ASIGNAR")
        {
            int pos = stoi(comando.substr(comando.find(" ") + 1, comando.rfind(" ")));
            int val = stoi(comando.substr(comando.rfind(" ") + 1, comando.length()));
            ini_vir.asignar(pos, val);
        }
        else if (comando1 == "CONSULTAR")
        {
            int pos = stoi(comando.substr(comando.find(" ") + 1, comando.length()));
            bool result = ini_vir.consultar(pos);
            if (result)
            {
                printf("El valor en la posición %d es %d\n", pos, ini_vir.T[pos]);
            }
            else
            {
                printf("No hay valor en la posición %d\n", pos);
            }
        }
        else if (comando1 == "LIMPIAR")
        {
            ini_vir.limpiar();
        }
        else if (comando1 == "SALIR")
        {
            ini_vir.borrar_salir();
            break;
        }
        else
        {
            printf("Comando no reconocido\n");
        }
        printf("\n");
    }
    return 0;
}
