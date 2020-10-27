import pygame
import numpy as np
import time


pygame.init()
# Ancho de la Pantalla. Screen Width
width , heigth = 1000 , 1000
# Creación de la Pantalla.
screen = pygame.display.set_mode((heigth , width))

# Color de Fondo. Background color 
bg = 25, 25, 25
# Pintar el fondo con el color elegido.
screen.fill(bg)

# Numero de Celdas. Number of Cells
nxC, nyC = 50, 50
# Dimensiones de la Celda. Cell Dimensions
dimCW = width  / nxC
dimCH = heigth / nyC

# Estado de Celdas. Vivas = 1; Muertas = 0;
# Cell Status. Alive = 1; Dead = 0;
gameState = np.zeros((nxC, nyC))

# Automata #2.
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

#Control de Ejecucion. Execution Control
pauseExect = False

# Bucle de Ejecución. Execution Loop
while True:
# A current copy of the game is required for each iteration
# En cada Iteracion se necesita una copia actual del juego
    newGameState = np.copy(gameState)
     # Limpia la pantalla. Clean the screen
    screen.fill(bg)
    #para que se tome un repiro. so that you can take a break
    time.sleep(0.1)
    #Record keyboard and mouse events
    #Registrar eventos del teclado y del mouse
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect

# Ciclo que Recorre las celadas Y , X
# Cycle that runs through the Y, X traps
    for y in range(0, nxC):
        for x in range(0, nyC):
            if not pauseExect:
            # Calcular Cuantos vecinos cercanos. Calculate how many close neighbors.
                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x) % nxC, (y - 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x - 1) % nxC, (y) % nyC] + \
                      gameState[(x + 1) % nxC, (y) % nyC] + \
                      gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                      gameState[(x) % nxC, (y + 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y + 1) % nyC] 
            # Rule # 1: A dead Cell with exactly 3 neighbors, "Revive" 
            # Regla #1 : Una Celula muerta con exactamente 3 vecinas, " Revive".
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1
            # Rule # 2: A Living Cell with less than 2 or more than 3 living neighbors, "Die".
            # Regla #2 : Una Célula Viva con menos de 2 o más de 3 vecinas vivas, "Muere".
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh >3):
                newGameState[x, y] = 0               
            # Creation of the Polygon of each cell to draw.          
            # Creacion del Polígono de cada celda a dibujar. 
            poly = [((x) * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x) * dimCW, (y+1) * dimCH)]
            # We draw the Cell for each pair of X and Y.
            # Dibujamos la Celula para cada par de X e Y.
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
# We update the State of the Game.
# Actualizamos el Estado del Juego.
gameState = np.copy(newGameState)   
# Display function to show the frame in each iteration
# Funcion display para mostrar el fotograma en cada iteracion. 
pygame.display.flip()
