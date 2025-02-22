import pygame
from pygame._sdl2 import Window
import random
import os
import sys

boss = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


class Boss(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__(boss, all_sprites)
        self.cut = 0
        self.cut_run = 1
        self.run = cut_sheet('Spellsword sprite sheet walk', 12, 1, sz=(108 * 4, 93 * 4))
        self.image = self.run[1][0]
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, x=0, cut_run=-1):
        self.cut = (self.cut + 1) % 12
        if cut_run != -1:
            self.cut_run = cut_run
        self.image = self.run[self.cut_run][self.cut]
        self.mask = pygame.mask.from_surface(self.image)

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
    cut1 = 0  # 81
    cut2 = 0  # 34
    cut_run = 0  # 12
    time_font = pygame.font.SysFont('timer', 60)
    #img1 = cut_sheet('Spellsword sprite sheet sumon', 81, 1, sz=(108 * 4, 93 * 4))
    #img2 = cut_sheet('Spellsword sprite sheet death', 34, 1, sz=(108 * 4, 93 * 4))
    bb = Boss((100, 100))
    run_s = 1
    n1 = pygame.USEREVENT + 10
    pygame.time.set_timer(n1, 70)
    ass = pygame.USEREVENT + 1
    pygame.time.set_timer(ass, 100)
    time_text = time_font.render('SOMING SOON', False, 'white')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return 0
                if event.key == pygame.K_a:
                    bb.update(cut_run=1)
                if event.key == pygame.K_d:
                    bb.update(cut_run=0)
            if event.type == n1:
                bb.update()
        screen.fill('black')
        boss.draw(screen)
        # screen.blit(time_text, (170, 270))
        pygame.display.flip()
    pygame.quit()


