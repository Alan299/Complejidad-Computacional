def grafo_a_binario(grafo:dict, longitud_numero=8):
    """
    Codifica un grafo como una cadena binaria con listas de adyacencia.

    Args:
        grafo (dict): Un diccionario que representa el grafo.
        longitud_numero (int): La longitud en bits de cada número.

    Returns:
        str: La cadena binaria que representa el grafo.
    """
    nodo_max = max( list(grafo.keys()))
    binario = ""
    for nodo, adyacentes in grafo.items():
        for adyacente in adyacentes:
            binario += format(adyacente, f'0{longitud_numero}b')
        if not nodo ==nodo_max :
            binario += format(0, f'0{longitud_numero}b')  # Separador

    return binario

def binario_a_grafo(cadena_binaria, longitud_numero=8):
    """
    Decodifica una cadena binaria a un grafo.

    Args:
        cadena_binaria (str): La cadena binaria que representa el grafo.
        longitud_numero (int): La longitud en bits de cada número.

    Returns:
        dict: Un diccionario que representa el grafo.
    """
    grafo = {}
    nodo = 1 # La numeraciòn de los nodos empiza en 1
    grafo[nodo] = []
    for i in range(0, len(cadena_binaria), longitud_numero):
        nodo_nuevo = cadena_binaria[i:i+longitud_numero]

        # si el numero leido es 0, entonces empezamos una nueva lista de adyacencias para el siguiente nodo
        if nodo_nuevo == "0" * longitud_numero:
            nodo += 1 
            grafo[nodo] = []
            
        else:
            adyacente = int(nodo_nuevo, 2)
            grafo[nodo].append(adyacente)
            
            
    return grafo


def binario_a_matriz(cadena_binaria, longitud_numero=8):
    """
    Convierte una cadena binaria que representa un grafo en una matriz de adyacencia.

    Args:
        cadena_binaria (str): La cadena binaria del grafo.
        longitud_numero (int): Longitud en bits de cada número (nodo o conexión).

    Returns:
        list: Matriz de adyacencia.
    """
    num_nodos = 0
    # contamos el numero de nodos 
    for i in range(0, len(cadena_binaria), longitud_numero):
            numero = cadena_binaria[i:i+longitud_numero]

            # Si el número es cero, pasamos al siguiente nodo
            if numero == "0" * longitud_numero:
                num_nodos+= 1
    num_nodos+= 1  
    print("Numero de nodos: ", num_nodos)

    
    matriz = [[0] * num_nodos for _ in range(num_nodos)]  # Inicializa la matriz

    nodo_actual = 1
    for i in range(0, len(cadena_binaria), longitud_numero):
        numero = cadena_binaria[i:i+longitud_numero]

        # Si el número es cero, pasamos al siguiente nodo
        if numero == "0" * longitud_numero:
            nodo_actual += 1
            continue  # Salta al siguiente número

        # Convertimos el número a entero y lo agregamos a la matriz
        adyacente = int(numero, 2)
        matriz[nodo_actual - 1][adyacente - 1] = 1
        # Para grafos no dirigidos:
        matriz[adyacente - 1][nodo_actual - 1] = 1

    return matriz