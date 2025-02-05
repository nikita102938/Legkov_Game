import pygame
from pygame._sdl2 import Window
import random


class Block_Tetris(pygame.sprite.Sprite):
    pass


def tetris():
    pygame.init()
    pygame.display.set_caption('квадрат')
    size = width, height = 650, 650
    screen = pygame.display.set_mode(size)
    fps = 50  # количество кадров в секунду
    clock = pygame.time.Clock()
    window = Window.from_display_module()
    window.position = (675, 0)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0
        screen.fill('black')
        pygame.draw.rect(screen, 'white', (50, 25, 300, 600), 3)
        """for i in range(1, 20):
            pygame.draw.line(screen, 'white', (50, 25 + 30 * i), (349, 25 + 30 * i), 1)
        for i in range(1 , 10):
            pygame.draw.line(screen, 'white', (50 + 30 * i, 25), (50 + 30 * i, 624), 1)"""

        pygame.display.flip()
    pygame.quit()