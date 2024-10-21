import sys
from utils import leer_grafo, generar_certificado_aleatorio, guardar_certificado


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

    