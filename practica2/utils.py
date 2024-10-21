import numpy as np
import random
import sys

def leer_grafo(archivo: str):
    """
    Lee la matriz de adyacencia de un archivo .txt y la devuelve como un numpy array.
    El archivo tiene la primera línea que indica el tamaño del grafo (n), 
    seguido de n líneas que contienen la matriz de adyacencia.
    
    Params:
        archivo: ruta del archivo de entrada
        
    Returns:
        np.array: matriz de adyacencia del grafo
    """
    with open(archivo, 'r') as f:
        lines = f.readlines()
        
        # Leer la primera línea que contiene el tamaño del grafo (n)
        n = int(lines[0].strip())
        
        # Crear la matriz de adyacencia a partir de las siguientes n líneas
        matriz = []
        for i in range(1, n + 1):
            matriz.append([int(x) for x in lines[i].strip().split()])

    return np.array(matriz)

def leer_certificado(archivo_certificado: str) -> list:
    """
    Lee el certificado (secuencia de vértices) desde un archivo.
    
    Params:
        archivo_certificado: ruta al archivo que contiene la secuencia de vértices
    
    Returns:
        Una lista de enteros que representa la secuencia de vértices.
    """
    with open(archivo_certificado, 'r') as f:
        certificado = [int(v) for v in f.readline().strip().split(',')]
    
    return certificado


def verificar_certificado(matriz: np.array, certificado: list):
    """
    Verifica si el certificado proporcionado forma una ruta hamiltoniana válida en el grafo.
    Se revisa si cada par consecutivo de vértices en el certificado está conectado por una arista en la matriz.
    
    Params:
        matriz: matriz de adyacencia del grafo
        certificado: lista de vértices que representan el certificado a verificar
        
    Returns:
        bool: True si el certificado es una ruta hamiltoniana válida, False en caso contrario
    """
    n = len(certificado)
    
    # Verificar que todos los vértices sean únicos (es decir, que se visiten exactamente una vez)
    if len(set(certificado)) != len(matriz):
        return False
    
    # Verificar que cada par consecutivo de vértices en el certificado esté conectado
    for i in range(n - 1):
        if matriz[certificado[i]][certificado[i + 1]] == 0:
            return False
    
    # Verificar que el último vértice esté conectado al primero si es un ciclo hamiltoniano
    if matriz[certificado[-1]][certificado[0]] == 0:
        return False
    
    return True

def generar_certificado_aleatorio(n: int):
    """
    Genera un certificado aleatorio, que es una permutación de los vértices del grafo.
    Se genera una lista de vértices desde 0 hasta n-1 y se mezcla aleatoriamente.
    
    Params:
        n: número de vértices en el grafo
        
    Returns:
        list: una secuencia aleatoria de vértices que representa el certificado
    """
    # Generar una secuencia de vértices [0, 1, 2, ..., n-1]
    vertices = list(range(0, n))
    
    # Mezclar aleatoriamente los vértices para crear un certificado
    random.shuffle(vertices)
    
    return vertices

def guardar_certificado(archivo_salida: str, certificado: list):
    """
    Guarda un certificado generado en un archivo de salida.
    
    Params:
        archivo_salida: ruta del archivo de salida donde se guardará el certificado
        certificado: lista de vértices que representan el certificado
    """
    with open(archivo_salida, 'w') as f:
        # Escribir el certificado como una lista de vértices separados por comas
        f.write(','.join(map(str, certificado)))

if __name__ == "__main__":
    # Leer los argumentos de la línea de comandos
    archivo_entrada = sys.argv[1]  # Nombre del archivo de entrada con la matriz de adyacencia
    archivo_salida = sys.argv[2]   # Nombre del archivo de salida donde se guardará el certificado

    # Leer el grafo desde el archivo
    matriz = leer_grafo(archivo_entrada)

    # Generar un certificado aleatorio y guardarlo en el archivo de salida
    n = len(matriz)  # Número de vértices en el grafo
    certificado_aleatorio = generar_certificado_aleatorio(n)
    guardar_certificado(archivo_salida, certificado_aleatorio)
    print(f"Certificado aleatorio guardado en {archivo_salida}")

    # Verificar si el certificado generado es válido
    if verificar_certificado(matriz, certificado_aleatorio):
        print("El certificado generado es válido.")
    else:
        print("El certificado generado no es válido.")
