# Algoritmo de ordenamiento Merge Sort aplicado a productos de un e-commerce

import pandas as pd
import time

# Función Merge Sort para ordenar productos por precio
def merge_sort_productos(lista):
    if len(lista) <= 1:
        return lista

    medio = len(lista) // 2
    izquierda = merge_sort_productos(lista[:medio])
    derecha = merge_sort_productos(lista[medio:])

    return merge(izquierda, derecha)

# Función para unir listas ordenadas
def merge(izquierda, derecha):
    resultado = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i]['precio'] <= derecha[j]['precio']:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado

# Cargar CSV y convertir a lista de diccionarios
productos = pd.read_csv("productos_deportivos.csv").to_dict(orient="records")

# Aplicar ordenamiento y medición de método
inicio_merge = time.time()
ordenados = merge_sort_productos(productos)
fin_merge = time.time()

print(f"\nTiempo de ejecución Merge Sort: {fin_merge - inicio_merge:.6f} segundos")
'''
# Mostrar los 10 productos más baratos
print("Top 10 productos más baratos:")
for producto in ordenados[:10]:
    print(producto)

# Mostrar los 10 productos más caros
print("\nTop 10 productos más caros:")
for producto in ordenados[-10:]:
    print(producto)
'''
