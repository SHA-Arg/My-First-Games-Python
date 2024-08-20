import pygame
import numpy as np
from Packages.Game import *
from Packages.Menu import *


def main_menu(screen, width, height):
    menu = True
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

        screen.fill((0, 0, 0))
        draw_text(screen, "Juego de la Vida", (width // 4, height // 4))
        draw_text(screen, "Presiona 'S' para Iniciar",
                  (width // 4, height // 2))
        draw_text(screen, "Presiona 'I' para Instrucciones",
                  (width // 4, height // 1.5))
        pygame.display.flip()


def instructions(screen, width, height):
    showing_instructions = True
    while showing_instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return True

        screen.fill((0, 0, 0))
        draw_text(screen, "Instrucciones:", (width // 4, height // 4))
        draw_text(screen, "1. Presiona 'Espacio' para Pausar/Reanudar",
                  (width // 4, height // 2))
        draw_text(screen, "2. Usa el Mouse para activar/desactivar células",
                  (width // 4, height // 1.5))
        draw_text(screen, "3. Presiona 'Esc' para Volver al Menú",
                  (width // 4, height // 1.2))
        pygame.display.flip()
