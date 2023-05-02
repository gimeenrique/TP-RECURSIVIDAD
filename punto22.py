def usar_la_fuerza(mochila, indice=0, objetos_sacados=0):
    """
    Función recursiva que busca un sable de luz en la mochila.
    Devuelve el número de objetos que se sacaron para encontrar el sable o -1 si no se encontró.
    """
    if indice >= len(mochila):
        # Caso base: no hay más objetos en la mochila
        return -1
    elif mochila[indice] == 'sable de luz':
        # Caso base: se encontró el sable de luz
        return objetos_sacados + 1
    else:
        # Caso recursivo: se saca un objeto y se continúa buscando
        return usar_la_fuerza(mochila, indice + 1, objetos_sacados + 1)

# Ejemplo de uso
mochila = ['botas', 'comida', 'agua', 'sable de luz', 'medicina']
objetos_sacados = usar_la_fuerza(mochila)
if objetos_sacados == -1:
    print("No se encontró el sable de luz en la mochila.")
else:
    print("Se sacaron", objetos_sacados, "objetos para encontrar el sable de luz.")