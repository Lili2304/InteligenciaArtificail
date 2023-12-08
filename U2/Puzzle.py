import random

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(map(str, fila)))

def encontrar_espacio_blanco(tablero):
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == 0:
                return i, j

def mover(tablero, direccion):
    i, j = encontrar_espacio_blanco(tablero)
    if direccion == 'izquierda' and j > 0:
        tablero[i][j], tablero[i][j - 1] = tablero[i][j - 1], tablero[i][j]
    elif direccion == 'derecha' and j < 2:
        tablero[i][j], tablero[i][j + 1] = tablero[i][j + 1], tablero[i][j]
    elif direccion == 'arriba' and i > 0:
        tablero[i][j], tablero[i - 1][j] = tablero[i - 1][j], tablero[i][j]
    elif direccion == 'abajo' and i < 2:
        tablero[i][j], tablero[i + 1][j] = tablero[i + 1][j], tablero[i][j]

def mezclar(tablero, movimientos=100):
    direcciones = ['izquierda', 'derecha', 'arriba', 'abajo']
    for _ in range(movimientos):
        direccion = random.choice(direcciones)
        mover(tablero, direccion)

def es_ganador(tablero):
    objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return tablero == objetivo

def main():
    tablero = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    mezclar(tablero)
    
    movimientos = 0  
    
    while not es_ganador(tablero):
        imprimir_tablero(tablero)
        direccion = input("Mueve la pieza en blanco (izquierda, derecha, arriba, abajo): ").lower()
        if direccion in ['izquierda', 'derecha', 'arriba', 'abajo']:
            mover(tablero, direccion)
            movimientos += 1  
        else:
            print("Movimiento no válido. Inténtalo de nuevo.")
    
    imprimir_tablero(tablero)
    print("¡Felicidades, has resuelto el rompecabezas en", movimientos, "movimientos!")

if __name__ == "__main__":
    main()

