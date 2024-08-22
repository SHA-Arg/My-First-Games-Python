from Packages.Menu import *
from Packages.Game import *
import numpy as np
import pygame


def main_menu(screen, width, height):
    '''
    Esta función se encarga de mostrar el menú principal del juego. Recibe la pantalla, el ancho y alto de la ventana. Devuelve la opción seleccionada por el usuario. 

    Args:
    screen (pygame.Surface): La pantalla del juego.
    width (int): El ancho de la ventana.
    height (int): El alto de la ventana.

    Returns:
    str: La opción seleccionada por el usuario.

    '''
    # Mostrar el menú principal
    menu = True
    # Cargar la imagen de fondo del menú
    background_image = pygame.image.load('./imgs/banner-bg.png')
    background_image = pygame.transform.scale(
        background_image, (width, height))
    # Bucle principal del menú
    while menu:
        # Obtener los eventos de pygame
        for event in pygame.event.get():
            # Si el usuario cierra la ventana, salir del juego
            if event.type == pygame.QUIT:
                # Salir del juego
                pygame.quit()
                return False
            # Si el usuario presiona una tecla, Si el usuario presiona la tecla 'S', comenzar el juego. Si el usuario presiona la tecla 'I', mostrar las instrucciones.
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    return 'instructions'
                if event.key == pygame.K_s:
                    return 'start'
        # Dibujar la imagen de fondo
        screen.blit(background_image, (0, 0))
        # Dibujar el título del juego
        draw_text(screen, "Juego de la Vida", (width // 2, height //
                  4), size=70, color=(255, 215, 0), bold=True)

        # Dibujar las opciones del menú
        draw_text(screen, "Presiona 'S' para Comenzar",
                  (width // 2, height // 2), size=40, color=(255, 255, 255))
        draw_text(screen, "Presiona 'I' para ver Instrucciones",
                  (width // 2, height // 1.5), size=40, color=(255, 255, 255))
        # Actualizar la pantalla
        pygame.display.flip()


def instructions(screen, width, height):
    ''' 
    Esta función se encarga de mostrar las instrucciones del juego. Recibe la pantalla, el ancho y alto de la ventana. Devuelve True si el usuario presiona la tecla 'Esc' para salir.

    args:
    screen (pygame.Surface): La pantalla del juego.
    width (int): El ancho de la ventana.
    height (int): El alto de la ventana.

    Returns:
    bool: True si el usuario presiona la tecla 'Esc' para salir.

    '''
    # Mostrar las instrucciones
    showing_instructions = True

    # Cargar la imagen de fondo de las instrucciones
    background_image = pygame.image.load('./imgs/color-sharp.png')
    background_image = pygame.transform.scale(
        background_image, (width, height))
    # Bucle principal de las instrucciones
    while showing_instructions:
        # Obtener los eventos de pygame
        for event in pygame.event.get():
            # Si el usuario cierra la ventana, salir del juego
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            # Si el usuario presiona la tecla 'Esc', salir de las instrucciones
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True
        # Dibujar la imagen de fondo
        screen.blit(background_image, (0, 0))
        # Dibujar el título de las instrucciones
        draw_text(screen, "Instrucciones", (width // 2, height //
                  5), size=70, color=(255, 215, 0), bold=True)

        # Dibujar las opciones del menú
        draw_text(screen, "1. Presiona 'Espacio' para Pausar/Reanudar",
                  (width // 2, height // 3.5), size=30, color=(255, 255, 255))
        draw_text(screen, "2. Usa el Mouse para activar/desactivar células",
                  (width // 2, height // 2), size=30, color=(255, 255, 255))
        draw_text(screen, "3. Presiona 'Esc' para Volver al Menú",
                  (width // 2, height // 1.5), size=30, color=(255, 255, 255))
        # Actualizar la pantalla
        pygame.display.flip()
