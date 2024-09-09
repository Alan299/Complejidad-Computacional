import argparse
import codificador  # Asegúrate de que el archivo coficador.py esté en el mismo directorio



#python obten_matriz.py  ejemplos/g1_bin.txt   g1_bin.txt
def main():
    parser = argparse.ArgumentParser(description='Convierte una representación binaria de un grafo a una matriz de adyacencia.')
    parser.add_argument('archivo_entrada', type=str, help='Nombre del archivo de entrada con la representación binaria.')
    parser.add_argument('archivo_salida', type=str, help='Nombre del archivo de salida para la matriz de adyacencia.')
    args = parser.parse_args()

    # Leer el contenido del archivo de entrada
    with open(args.archivo_entrada, 'r') as f:
        cadena_binaria = f.read().strip()

    # Llamar a la función binario_a_matriz
    matriz_adyacencia = codificador.binario_a_matriz(cadena_binaria)
    

    # Calcular el número de aristas y nodos
    num_nodos = len(matriz_adyacencia)
    num_aristas = sum(sum(fila) for fila in matriz_adyacencia) // 2  # Dividimos por 2 para no contar aristas dos veces en grafos no dirigidos

    # Guardar la matriz en un archivo .txt
    with open(args.archivo_salida, 'w') as f:
        for fila in matriz_adyacencia:
            f.write(' '.join(map(str, fila)) + '\n')

    print(f"Número de nodos: {num_nodos}")
    print(f"Número de aristas: {num_aristas}")

if __name__ == '__main__':
    main()