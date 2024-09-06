"""
Una grafica no dirigida G,
tiene un camino Euleriano si
 bien cada vértice tiene un grado par o exactamente dos vértices tienen un grado impar.
"""
import argparse
import os


def encuentra_vertice_inicial(grafo):
    """Encuentra un vértice inicial válido para el algoritmo de Fleury.
       Necesitamos encontrar un vertice de grado impar.

    Args:
        grafo: La matriz de adyacencia del grafo no dirigido.

    Returns:
        int: El índice del vértice inicial.

    O(n) a lo mas recorre revisa los n nodos
    """
    for i in range(len(grafo)):
        grado = sum(grafo[i])
        if grado % 2 != 0:
            return i
    return 0

def tiene_puente(u, v, grafo):
    """Determina si una arista es un puente.
    Es decir si tiene grado igual a uno, y removemos  la arista (u,v)
    entonces el nodo quedara desconectado formando 2 componentes en el grafo.

    Args:
        u: El primer vértice de la arista.
        v: El segundo vértice de la arista.
        grafo: La matriz de adyacencia del grafo.

    Returns:
        bool: True si la arista es un puente, False en caso contrario.
    O(n) hace la suma de las n entradas de la matriz siempre
    """
    #
    grado = sum(grafo[v])
    if grado > 1:
        return False
    return True

def cuenta_aristas(grafo):
    """Cuenta el número total de aristas en el grafo.

    Args:
        grafo: La matriz de adyacencia del grafo.

    Returns:
        int: El número de aristas.

    O(n^2) suma sobre las columnas*renglones  n*n
    """

    # //2 pues tenemos un grafo dirigido contando 1 arista como 2
    # la arista (u,v) es la misma que (v,u)
    return sum(sum(fila) for fila in grafo) // 2

def algoritmo_fleury(inicio, grafo, camino, circuito_encontrado):
    """Implementa el algoritmo de Fleury para encontrar un camino  Euleriano.

    Args:
        inicio: El vértice inicial.
        grafo: La matriz de adyacencia del grafo.
        camino: La lista para almacenar el camino Euleriano.
        circuito_encontrado: Una lista para indicar si se encontró un circuito.

    O(n^4)
        O(n^2) a lo mas visitamos cada arista (u,v) una vez
        Con la recursion potencialmente corriendo O(n^2) 
    """
    aristas_restantes = cuenta_aristas(grafo)
    for v in range(len(grafo)):
        if grafo[inicio][v]:
            if aristas_restantes <= 1 or not tiene_puente(inicio, v, grafo):
                camino.append((inicio, v))
                grafo[inicio][v] = grafo[v][inicio] = 0
                aristas_restantes -= 1
                algoritmo_fleury(v, grafo, camino, circuito_encontrado)
    if aristas_restantes == 0 and not circuito_encontrado[0]:
        circuito_encontrado[0] = True



def procesa_grafo(ruta_archivo):
    """
    Lee un archivo de texto que contiene la matriz de adyacencia de un grafo y 
    devuelve la matriz de adyacencia en formato de lista de listas.

    Args:
        ruta_archivo (str): La ruta completa al archivo de texto.

    Returns:
        list: La matriz de adyacencia del grafo.
    """

    grafo = []
    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            fila = list(map(int, linea.strip().split()))
            grafo.append(fila)
    return grafo

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Determina si un grafo tiene un camino Euleriano.')
    parser.add_argument('archivo', help='Ruta al archivo que contiene la matriz de adyacencia')
    args = parser.parse_args()

    matriz = procesa_grafo(args.archivo)

    print("matriz")
    print(*matriz, sep = "\n")

    """
    python fleury.py   ejemplos/g1.txt
    """

    inicio = encuentra_vertice_inicial(matriz)
    camino = []
    circuito_encontrado = [False]
    algoritmo_fleury(inicio = inicio, grafo = matriz, camino = camino , circuito_encontrado =circuito_encontrado )

    print(camino)
    print(circuito_encontrado)