import pygame
import numpy as np
import time
from Packages.Menu import *
from Packages.Game import *


def init_pygame(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Juego de la Vida")
    return screen


def main():
    width, height = 600, 600
    screen = init_pygame(width, height)

    bg = 25, 25, 25
    nxC, nyC = 50, 50
    dimCW = width / nxC
    dimCH = height / nyC

    gameState = np.zeros((nxC, nyC))
    gameState[21, 21] = 1
    gameState[22, 22] = 1
    gameState[22, 23] = 1
    gameState[21, 23] = 1
    gameState[20, 23] = 1

    pauseExect = False

    while True:
        menu_selection = main_menu(screen, width, height)
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
