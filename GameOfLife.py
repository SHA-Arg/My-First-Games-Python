import pygame
import numpy as np
import time
from Packages.Menu import *
from Packages.Game import *


def init_pygame(width, height):
    '''
    Esta función inicializa pygame y crea una ventana con el tamaño especificado.

    Parámetros:
    width -- Ancho de la ventana.
    height -- Alto de la ventana.

    Retorna:
    screen -- La ventana de pygame.

    '''
    # Inicializar pygame
    pygame.init()
    # Crear la ventana
    screen = pygame.display.set_mode((width, height))
    # Establecer el título de la ventana
    pygame.display.set_caption("Juego de la Vida")
    return screen


def main():
    '''
    Esta función es la encargada de ejecutar el juego. Inicializa pygame, crea la ventana y ejecuta el juego.

    '''
    # Inicializar pygame y crear la ventana
    width, height = 600, 600
    # Inicializar pygame y crear la ventana
    screen = init_pygame(width, height)

    # Definir el color de fondo
    bg = 25, 25, 25
    # Definir el número de celdas en anchura y altura
    nxC, nyC = 50, 50
    # Definir las dimensiones de las celdas en anchura y altura
    dimCW = width / nxC
    dimCH = height / nyC
    # Crear el estado del juego inicial
    gameState = np.zeros((nxC, nyC))
    # Crear un patrón inicial
    gameState[21, 21] = 1
    gameState[22, 22] = 1
    gameState[22, 23] = 1
    gameState[21, 23] = 1
    gameState[20, 23] = 1

    pauseExect = False

    # Bucle principal del juego
    while True:
        # Mostrar el menú principal
        menu_selection = main_menu(screen, width, height)
        # Si el usuario cierra la ventana, salir del juego
        if menu_selection == 'instructions':
            if not instructions(screen, width, height):
                break
        elif menu_selection == 'start':
            while True:
                newGameState = np.copy(gameState)
                ev = pygame.event.get()

                for event in ev:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            pauseExect = not pauseExect
                        if event.key == pygame.K_ESCAPE:
                            gameState = np.zeros((nxC, nyC))
                            break
                    if pygame.mouse.get_pressed()[0]:
                        posX, posY = pygame.mouse.get_pos()
                        celX, celY = int(posX / dimCW), int(posY / dimCH)
                        newGameState[celX, celY] = not newGameState[celX, celY]

                if not pauseExect:
                    newGameState = update_game_state(gameState, nxC, nyC)

                draw_cells(screen, newGameState, dimCW, dimCH, bg)
                gameState = newGameState
                pygame.display.flip()
                time.sleep(0.1)


if __name__ == "__main__":
    main()
