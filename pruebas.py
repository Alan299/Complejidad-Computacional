from codificador import grafo_a_binario
from codificador import binario_a_grafo
from codificador import binario_a_matriz
from utils import print_broken_string

# Pruebas
def probar_codificacion_decodificacion(grafo:dict):
    cadena_binaria = grafo_a_binario(grafo)

    print("cadena binaria")
    print_broken_string(cadena_binaria)
    print()

    grafo_recuperado = binario_a_grafo(cadena_binaria)
    print("Grafo recuperado")
    print(grafo_recuperado)
    assert grafo == grafo_recuperado, f"Error en la codificación/decodificación del grafo"
    print(f"La codificación y decodificación del grafo es correcta.")



if __name__ == "__main__":
    # La numeraciòn de los nodos empieza en 1 NO en 0.
    g1 = {
        1: [2, 3, 4, 5, 6],
        2: [1, 3, 4, 5, 6],
        3: [1, 2, 4, 5, 6],
        4: [1, 2, 3, 5, 6],
        5: [1, 2, 3, 4, 6],
        6: [1, 2, 3, 4, 5]
    }


    g2 = {
        1: [2, 3, 4, 5, 6],
        2: [1],
        3: [1],
        4: [1],
        5: [1],
        6: [1]
    }


    g3 = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3, 5, 6],
        5: [4],
        6: [4]
    }

    # Ejecutar las pruebas
    probar_codificacion_decodificacion(g1 )
    probar_codificacion_decodificacion(g2)
    probar_codificacion_decodificacion(g3)

    print("Pruebas de Binario a Matriz")


    cadena_binaria = grafo_a_binario(g1)
    matriz = binario_a_matriz(cadena_binaria)

    print("matriz de adyacencias")
    print(matriz)
    print()
