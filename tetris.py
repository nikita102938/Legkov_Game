import pygame
from pygame._sdl2 import Window
import os
import sys

boss = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


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


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


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
    time_font = pygame.font.SysFont('timer', 60)
    time_text = time_font.render('SOMING SOON', False, 'white')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0
        screen.fill('black')
        boss.draw(screen)
        screen.blit(time_text, (170, 270))
        pygame.display.flip()
    pygame.quit()
