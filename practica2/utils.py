
import numpy as np
import random
import sys

def leer_grafo_y_certificado(archivo:str):
    """
    Params:
        archivo: ruta del archivo
    Regresa una tupa (grafo, certificado)
    """
    with open(archivo, 'r') as f:
        lines = f.readlines()
        
        # Leer la matriz de adyacencia
        n = int(lines[0].strip())  # Primer línea es el tamaño del grafo
        matriz = []
        for i in range(1, n + 1):
            matriz.append([int(x) for x in lines[i].strip().split()])

        # Leer el certificado
        certificado = [int(x) for x in lines[n + 1].strip().split(',')]
    
    return np.array(matriz), certificado

def verificar_certificado(matriz:np.array, certificado:list):
    n = len(certificado)
    
    # Verificar si todos los vértices son visitados
    if len(set(certificado)) != len(matriz):
        return False
    
    # Verificar si todas las aristas del certificado están presentes en la gráfica
    for i in range(n - 1):
        if matriz[certificado[i] ][certificado[i + 1] ] == 0:
            return False
    
    # Si es un ciclo, verificar la última arista
    if matriz[certificado[-1] ][certificado[0] ] == 0:
        return False
    
    return True

def generar_certificado_aleatorio(n:int):


    # Generar una secuencia aleatoria de los vértices
    vertices = list(range(0, n ))
    random.shuffle(vertices)
    
    return vertices

def guardar_certificado(archivo_salida, certificado):
    with open(archivo_salida, 'w') as f:
        f.write(','.join(map(str, certificado)))

if __name__ == "__main__":
    # Leer los argumentos de la línea de comandos
    archivo_entrada = sys.argv[1]  # nombre del archivo de entrada
    archivo_salida = sys.argv[2]   # nombre del archivo de salida

    # Leer el grafo y el certificado
    matriz, certificado = leer_grafo_y_certificado(archivo_entrada)

    # Verificar si el certificado es válido
    if verificar_certificado(matriz, certificado):
        print("El certificado es válido")
    else:
        print("El certificado no es válido")
    
    # Generar un certificado aleatorio y guardarlo
    n = len(matriz)
    certificado_aleatorio = generar_certificado_aleatorio(n)
    guardar_certificado(archivo_salida, certificado_aleatorio)
    print(f"Certificado aleatorio guardado en {archivo_salida}")



