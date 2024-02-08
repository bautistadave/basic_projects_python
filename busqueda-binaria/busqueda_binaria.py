"""
Proyecto Básico de Python (Búsqueda Binaria). 
"""
import random
import time


def busqueda_ingenua(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# ejemplo para extraer logica
# [1, 3, 5, 10, 12]
#  0  1  2   3   4
# punto_medio = (0 + 4) // 2 = 2


mi_lista = [1, 5, 6, 9, 10, 7, 0]
print(busqueda_ingenua(mi_lista, 5)) #imprime la posicion

def busqueda_binaria(lista, objetivo, límite_inferior=None, límite_superior=None):
    if límite_inferior is None:
        límite_inferior = 0 # Inicio de la lista
    if límite_superior is None:
        límite_superior = len(lista) - 1 # Final de la lista

    if límite_superior < límite_inferior:
        return -1

    punto_medio = (límite_inferior + límite_superior) // 2  # divide y convierte en entero

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, límite_inferior, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio+1, límite_superior)


if __name__=='__main__':
    # Crear una lista ordenada con 10000 números aleatorios.
    tamaño = 10000
    conjunto_inicial = set()

    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño, 3*tamaño))

    lista_ordenada = sorted(list(conjunto_inicial))

    # Medir el tiempo de búsqueda ingenua.
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_ingenua(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda ingenua: {fin - inicio} segundos.")

    # Medir el tiempo de busqueda binaria.
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda binaria: {fin - inicio} segundos.")
