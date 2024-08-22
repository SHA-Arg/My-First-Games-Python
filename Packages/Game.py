import pygame
import numpy as np


def draw_cells(screen, gameState, dimCW, dimCH, bg):
    '''
    Esta función se encarga de dibujar las celdas en la pantalla. Recibe la pantalla, el estado del juego, las dimensiones de las celdas y el color de fondo.

    Args:
    screen (pygame.Surface): La pantalla del juego.
    gameState (numpy.ndarray): El estado del juego.
    dimCW (int): La dimensión de las celdas en anchura.
    dimCH (int): La dimensión de las celdas en altura.
    bg (tuple): El color de fondo.

    '''

    # Rellenar el fondo
    screen.fill(bg)
    # Dibujar las celdas
    for y in range(gameState.shape[1]):
        # Dibujar una línea horizontal
        for x in range(gameState.shape[0]):
            # Calcular los vértices del polígono
            poly = [((x) * dimCW, y * dimCH),
                    ((x+1) * dimCW, y * dimCH),
                    ((x+1) * dimCW, (y+1) * dimCH),
                    ((x) * dimCW, (y+1) * dimCH)]
            # Dibujar el polígono
            if gameState[x, y] == 0:
                # Dibujar el borde de la celda
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                # Dibujar la celda viva
                pygame.draw.polygon(screen, (255, 255, 255), poly, 0)


def update_game_state(gameState, nxC, nyC):
    '''
    Esta función se encarga de actualizar el estado del juego. Recibe el estado actual del juego, el número de celdas en anchura y altura. Devuelve el nuevo estado del juego.

    Args:
    gameState (numpy.ndarray): El estado actual del juego.
    nxC (int): El número de celdas en anchura.
    nyC (int): El número de celdas en altura.

    Returns:
    numpy.ndarray: El nuevo estado del juego.

    '''
    # Crear un nuevo array para el nuevo estado del juego y copiar el estado actual.
    newGameState = np.copy(gameState)
    # Iterar sobre cada celda
    for y in range(nyC):
        # Iterar sobre cada columna
        for x in range(nxC):
            # Calcular el número de vecinos
            n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
                gameState[(x) % nxC, (y - 1) % nyC] + \
                gameState[(x + 1) % nxC, (y - 1) % nyC] + \
                gameState[(x - 1) % nxC, (y) % nyC] + \
                gameState[(x + 1) % nxC, (y) % nyC] + \
                gameState[(x - 1) % nxC, (y + 1) % nyC] + \
                gameState[(x) % nxC, (y + 1) % nyC] + \
                gameState[(x + 1) % nxC, (y + 1) % nyC]
            # Aplicar las reglas del juego de la vida.
            # Si la celda está muerta y tiene 3 vecinos vivos, nace.
            if gameState[x, y] == 0 and n_neigh == 3:
                newGameState[x, y] = 1
                # Si la celda está viva y tiene menos de 2 o más de 3 vecinos vivos, muere.
            elif gameState[x, y] == 1 and (n_neigh < 2 or n_neigh > 3):
                newGameState[x, y] = 0
    # Devolver el nuevo estado del juego.
    return newGameState


def draw_text(screen, text, position, size=30, color=(255, 255, 255), font_name=None, bold=False, italic=False):
    '''
    Esta función se encarga de dibujar texto en la pantalla. Recibe la pantalla, el texto, la posición, el tamaño, el color, la fuente, si es negrita y si es cursiva. 

    Args:
    screen (pygame.Surface): La pantalla del juego.
    text (str): El texto a dibujar.
    position (tuple): La posición del texto.
    size (int): El tamaño del texto.
    color (tuple): El color del texto.
    font_name (str): El nombre de la fuente.
    bold (bool): Si el texto es negrita.
    italic (bool): Si el texto es cursiva.

    '''

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
