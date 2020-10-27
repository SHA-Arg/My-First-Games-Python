import pygame
import numpy as np
import time


pygame.init()
# Ancho de la Pantalla.
width , heigth = 1000 , 1000
# Creación de la Pantalla.
screen = pygame.display.set_mode((heigth , width))

# Color de Fondo. 
bg = 25, 25, 25
# Pintar el fondo con el color elegido.
screen.fill(bg)

# Numero de Celdas.
nxC, nyC = 50, 50
# Dimensiones de la Celda.
dimCW = width  / nxC
dimCH = heigth / nyC

# Estado de Celdas. Vivas = 1; Muertas = 0;
gameState = np.zeros((nxC, nyC))



# Automata #2.
gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1


#Control de Ejecucion
pauseExect = False


# Bucle de Ejecución.
while True:

# En cada Iteracion se necesita una copia actual del juego
    newGameState = np.copy(gameState)
     # Limpia la pantalla
    screen.fill(bg)
    #para que se tome un repiro todo
    time.sleep(0.1)

    #Registrar eventos del teclado y del maouse
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.KEYDOWN:
            pauseExect = not pauseExect


# Ciclo que Recorre las celadas Y , X
    for y in range(0, nxC):
        for x in range(0, nyC):

            if not pauseExect:
            # Calcular Cuantos vecinos cercanos.
                n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x) % nxC, (y - 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                      gameState[(x - 1) % nxC, (y) % nyC] + \
                      gameState[(x + 1) % nxC, (y) % nyC] + \
                      gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                      gameState[(x) % nxC, (y + 1) % nyC] + \
                      gameState[(x + 1) % nxC, (y + 1) % nyC] 

            # Regla #1 : Una Celula muerta con exactamente 3 vecinas, " Revive".
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1

            # Regla #2 : Una Célula Viva con menos de 2 o más de 3 vecinas vivas, "Muere".
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh >3):
                newGameState[x, y] = 0               

            # Creacion del Polígono de cada celda a dibujar. 
            poly = [((x) * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x) * dimCW, (y+1) * dimCH)]


            # Dibujamos la Celula para cada par de x e y.
            if newGameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)




# Actualizamos el Estado del Juego.
gameState = np.copy(newGameState)                  

# Funcion display para mostrar el fotograma en cada iteracion del 
pygame.display.flip()