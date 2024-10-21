import sys
import numpy as np
from utils import leer_grafo,leer_certificado, verificar_certificado

def verificar_ruta_hamiltoniana(archivo_grafo:str, archivo_certificado:str):
    """
    Params:
        archivo_grafo: ruta del archivo al grafo

        archivo_certificado: ruta del certificado (sequencia de vertices)
    """


    # Leer el grafo (matriz de adyacencia) y el certificado desde los archivos
    matriz, certificado = leer_grafo(archivo_grafo),leer_certificado(archivo_certificado)
    
    # Obtener número de vértices y aristas
    n_vertices = len(matriz)
    n_aristas = sum(sum(matriz[i][j] for j in range(n_vertices)) for i in range(n_vertices)) // 2

    # Imprimir información básica del grafo y el certificado
    print(f"Número de vértices: {n_vertices}")
    print(f"Número de aristas: {n_aristas}")
    print(f"Primer vértice de la ruta: {certificado[0]}")
    print(f"Último vértice de la ruta: {certificado[-1]}")
    
    # Verificar si el certificado satisface la condición de ruta Hamiltoniana
    es_valido = verificar_certificado(matriz, certificado)
    
    if es_valido:
        print("El certificado satisface la condición de pertenencia al lenguaje: Es una ruta Hamiltoniana válida.")
    else:
        print("El certificado NO satisface la condición de pertenencia al lenguaje: No es una ruta Hamiltoniana válida.")

if __name__ == "__main__":
    # Leer los argumentos de la línea de comandos
    archivo_grafo = sys.argv[1]      # Nombre del archivo con la matriz de adyacencia (ejemplar)
    archivo_certificado = sys.argv[2]  # Nombre del archivo con el certificado a probar

    # Verificar la ruta hamiltoniana
    verificar_ruta_hamiltoniana(archivo_grafo, archivo_certificado)
