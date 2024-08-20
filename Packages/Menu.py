# import pygame
# import pygame_menu


# def main_menu(screen, width, height):
#     # Cargar la imagen de fondo
# background_image = pygame.image.load('imgs\banner-bg.png')
# background_image = pygame.transform.scale(
#     background_image, (width, height))

#     # Crear el menú usando pygame_menu
#     menu = pygame_menu.Menu('Juego de la Vida', width, height,
#                             theme=pygame_menu.themes.THEME_DARK)

#     # Agregar botones al menú
#     menu.add_button('Comenzar Juego', start_game)
#     menu.add_button('Instrucciones', show_instructions)
#     menu.add_button('Salir', pygame_menu.events.EXIT)

#     # Ejecutar el menú
#     menu.mainloop(screen, bgfun=lambda: screen.blit(background_image, (0, 0)))


# def start_game():
#     return 'start'


# def show_instructions():
#     return 'instructions'


# def instructions(screen, width, height):
#     showing_instructions = True

#     # Cargar la imagen de fondo

# background_image = pygame.image.load('imgs\color-sharp.png')
# background_image = pygame.transform.scale(
#     background_image, (width, height))

#     while showing_instructions:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 return False
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_ESCAPE:
#                     return True

#         screen.blit(background_image, (0, 0))

#         draw_text(screen, "Instrucciones:", (width // 2,
#                   height // 4), size=40, color=(255, 255, 0))
#         draw_text(screen, "1. Presiona 'Espacio' para Pausar/Reanudar",
#                   (width // 5, height // 2), size=30, color=(255, 255, 255))
#         draw_text(screen, "2. Usa el Mouse para activar/desactivar células",
#                   (width // 5, height // 1.5), size=30, color=(255, 255, 255))
#         draw_text(screen, "3. Presiona 'Esc' para Volver al Menú",
#                   (width // 5, height // 1.2), size=30, color=(255, 255, 255))
#         pygame.display.flip()


# def draw_text(screen, text, position, size=50, color=(255, 255, 255)):
#     font = pygame.font.Font(None, size)
#     text_surface = font.render(text, True, color)
#     rect = text_surface.get_rect(center=position)
#     screen.blit(text_surface, rect)


# def main():
#     width, height = 1000, 1000
#     screen = init_pygame(width, height)

#     while True:
#         menu_selection = main_menu(screen, width, height)
#         if menu_selection == 'instructions':
#             if not instructions(screen, width, height):
#                 break
#         elif menu_selection == 'start':
#             # Aquí iría la lógica para iniciar el juego
#             pass


# def init_pygame(width, height):
#     pygame.init()
#     screen = pygame.display.set_mode((width, height))
#     pygame.display.set_caption("Juego de la Vida")
#     return screen


# if __name__ == "__main__":
#     main()

from Packages.Menu import *
from Packages.Game import *
import numpy as np
import pygame


def main_menu(screen, width, height):
    menu = True
    background_image = pygame.image.load('./imgs/banner-bg.png')
    background_image = pygame.transform.scale(
        background_image, (width, height))
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_i:
                    return 'instructions'
                if event.key == pygame.K_s:
                    return 'start'

        screen.blit(background_image, (0, 0))

        draw_text(screen, "Juego de la Vida", (width // 2, height //
                  4), size=70, color=(255, 215, 0), bold=True)

        # Dibujar las opciones del menú
        draw_text(screen, "Presiona 'S' para Comenzar",
                  (width // 2, height // 2), size=40, color=(255, 255, 255))
        draw_text(screen, "Presiona 'I' para ver Instrucciones",
                  (width // 2, height // 1.5), size=40, color=(255, 255, 255))

        pygame.display.flip()


def instructions(screen, width, height):
    showing_instructions = True

    background_image = pygame.image.load('./imgs/color-sharp.png')
    background_image = pygame.transform.scale(
        background_image, (width, height))

    while showing_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True

        screen.blit(background_image, (0, 0))

        draw_text(screen, "Instrucciones", (width // 2, height //
                  5), size=70, color=(255, 215, 0), bold=True)

        # Dibujar las opciones del menú

        draw_text(screen, "1. Presiona 'Espacio' para Pausar/Reanudar",
                  (width // 2, height // 3.5), size=30, color=(255, 255, 255))
        draw_text(screen, "2. Usa el Mouse para activar/desactivar células",
                  (width // 2, height // 2), size=30, color=(255, 255, 255))
        draw_text(screen, "3. Presiona 'Esc' para Volver al Menú",
                  (width // 2, height // 1.5), size=30, color=(255, 255, 255))

        pygame.display.flip()
