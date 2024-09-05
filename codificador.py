def grafo_a_binario(grafo:dict, longitud_numero=8):
    """
    Codifica un grafo como una cadena binaria con listas de adyacencia.

    Args:
        grafo (dict): Un diccionario que representa el grafo.
        longitud_numero (int): La longitud en bits de cada número.

    Returns:
        str: La cadena binaria que representa el grafo.
    """
    binario = ""
    for nodo, adyacentes in grafo.items():
        for adyacente in adyacentes:
            binario += format(adyacente, f'0{longitud_numero}b')
        if not nodo ==max( list(grafo.keys())):
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