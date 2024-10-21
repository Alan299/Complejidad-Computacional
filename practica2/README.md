# Practica 2 - Ruta Hamiltoniana



### Instalación de dependencias
Antes de ejecutar el script, asegúrate de tener instaladas las dependencias necesarias. 
Para ello, deberas instalar las dependencias listadas en el archivo `requirements.txt` 

```bash
pip install -r requirements.txt
```


##  Genera Certificado 

Para ejecutar el programa `genera_certificado.py`, debes proporcionar dos argumentos:

- El archivo de entrada que contiene la matriz de adyacencia del grafo.
- El archivo de salida donde se guardará el certificado generado aleatoriamente.

```bash
python genera_certificado.py <archivo_entrada> <archivo_salida>
``` 


### Estructura del archivo de entrada:

El archivo de entrada debe estar en el siguiente formato:


n

fila_1

fila_2

...

fila_n



### Notas:

- El certificado generado será una secuencia de vértices que podría representar una ruta hamiltoniana dentro del grafo.
- El archivo de salida contendrá el certificado como una sequencia de vèrtices

