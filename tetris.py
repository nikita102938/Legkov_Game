import pygame
from pygame._sdl2 import Window
import random


class Block_Tetris(pygame.sprite.Sprite):
    pass


def cut_sheet(sheet, columns, rows, sz=(240, 160)):
    sprite = pygame.image.load("data\{0}.png".format(sheet)).convert_alpha()
    framer = []
    framel = []
    width, height = sprite.get_size()
    w, h = width / columns, height / rows
    z = 0
    for j in range(rows):
        for i in range(columns):
            framer.append(pygame.transform.scale(sprite.subsurface(pygame.Rect(i * w, z, w, h)), sz))
        z += 1
    sprite = pygame.image.load("data\{0}.png".format(sheet)).convert_alpha()
    sprite = pygame.transform.flip(sprite, 1, 0)
    z = 0
    for j in range(rows):
        for i in range(columns):
            framel = [pygame.transform.scale(sprite.subsurface(pygame.Rect(i * w, z, w, h)), sz)] + framel
        z += 1
    return [framer, framel]



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
    cut1 = 0 #81
    cut2 = 0 #34
    cut3 = 0 #12
    img1 = cut_sheet('Spellsword sprite sheet sumon', 81, 1, sz=(108 * 4, 93 * 4))
    img2 = cut_sheet('Spellsword sprite sheet death', 34, 1, sz=(108 * 4, 93 * 4))
    img3 = cut_sheet('Spellsword sprite sheet walk', 12, 1, sz=(108 * 4, 93 * 4))
    ass = pygame.USEREVENT + 1
    pygame.time.set_timer(ass, 100)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0
            if event.type == ass:
                cut3 += 1
                cut3 %= 12
        screen.fill('black')
        screen.blit(img3[1][cut3], (70, 100))
        pygame.draw.rect(screen, 'white', (50, 25, 300, 600), 3)
        """for i in range(1, 20):
            pygame.draw.line(screen, 'white', (50, 25 + 30 * i), (349, 25 + 30 * i), 1)
        for i in range(1 , 10):
            pygame.draw.line(screen, 'white', (50 + 30 * i, 25), (50 + 30 * i, 624), 1)"""

        pygame.display.flip()
    pygame.quit()

tetris()