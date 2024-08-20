import pygame
import numpy as np


def draw_cells(screen, gameState, dimCW, dimCH, bg):
    screen.fill(bg)
    for y in range(gameState.shape[1]):
        for x in range(gameState.shape[0]):
            poly = [((x) * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x) * dimCW, (y+1) * dimCH)]
            if gameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)


def update_game_state(gameState, nxC, nyC):
    newGameState = np.copy(gameState)
    for y in range(nyC):
        for x in range(nxC):
            n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                gameState[(x) % nxC, (y - 1) % nyC] + \
                gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                gameState[(x - 1) % nxC, (y) % nyC] + \
                gameState[(x + 1) % nxC, (y) % nyC] + \
                gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                gameState[(x) % nxC, (y + 1) % nyC] + \
                gameState[(x + 1) % nxC, (y + 1) % nyC]
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0
    return newGameState


def draw_text(screen, text, position, size=30, color=(255, 255, 255), font_name=None, bold=False, italic=False):
    # Cargar la fuente, si se proporciona un nombre, usa esa fuente
    font = pygame.font.Font(font_name, size)

    # Aplicar estilos si es necesario
    font.set_bold(bold)
    font.set_italic(italic)

    # Renderizar el texto
    text_surface = font.render(text, True, color)

    # Obtener el rectángulo del texto y centrarlo en la posición proporcionada
    rect = text_surface.get_rect(center=position)

    # Dibujar el texto en la pantalla
    screen.blit(text_surface, rect)
