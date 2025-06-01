
# Algoritmo de ordenamiento Quick Sort aplicado a productos de un e-commerce

import pandas as pd
import time

# Función Quick Sort para ordenar productos por precio
def quick_sort_example(lista):
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista)// 2]['precio']
    parte_iz = [x for x in lista if x['precio']< pivote]
    igual = [x for x in lista if x['precio']==pivote]
    parte_der = [x for x in lista if x['precio'] > pivote]

    return quick_sort_example(parte_iz) +igual + quick_sort_example(parte_der)

# Cargar CSV y convertir a lista de diccionarios
lista_productos = pd.read_csv("productos_deportivos.csv").to_dict(orient="records")


# Aplicar ordenamiento y medición de ordenacmiento

inicio_quick = time.time()
productos_ordenados_con_quick_sort = quick_sort_example(lista_productos)
fin_quick = time.time()

print(f"Tiempo de ejecución Quick Sort: {fin_quick - inicio_quick:.6f} segundos")

'''
# Mostrar los 10 productos más baratos
print("Top 10 productos más baratos:")
for productos_baratos in productos_ordenados_con_quick_sort[:10]:
    print(productos_baratos)

# Mostrar los 10 productos más caros
print("\nTop 10 productos más caros:")
for producto_costos in productos_ordenados_con_quick_sort[-10:]:
    print(producto_costos)
'''

