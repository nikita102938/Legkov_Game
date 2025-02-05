import os
import sys
import random
import pygame
import time
from pygame._sdl2 import Window
from tetris import *

pygame.init()
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()
oblaka = pygame.sprite.Group()
texture = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = pygame.sprite.Group()
nps = pygame.sprite.Group()
yandex = pygame.sprite.Group()
play = pygame.sprite.Group()
f1 = pygame.sprite.Group()
home1 = pygame.sprite.Group()
lst = pygame.sprite.Group()
lstk = pygame.sprite.Group()
armor = pygame.sprite.Group()
sz = (240, 160)
x, y = 18, 8
y_prig = 17
music_volume = 0.5
COINMP3 = pygame.mixer.Sound('data/coin.mp3')
SWORDPLMP3 = pygame.mixer.Sound('data/SWORDPLAYER.mp3')
SKELETMP3 = pygame.mixer.Sound('data/SKELET.mp3')
DMGPLMP3 = pygame.mixer.Sound('data/dmg.mp3')
RUNMP3 = pygame.mixer.Sound('data/RUN.mp3')
HILSTMP3 = pygame.mixer.Sound('data/HILSTATYA.mp3')
KUVALDAMP3 = pygame.mixer.Sound('data/KUVALDA.mp3')
PAYMP3 = pygame.mixer.Sound('data/PAY.mp3')
LISTMP3 = pygame.mixer.Sound('data/LIST.mp3')
LISTMMP3 = pygame.mixer.Sound('data/LIST_MINUS.mp3')
BLUMMP3 = pygame.mixer.Sound('data/blum.mp3')
MMM = pygame.mixer.Sound('data/mmm.mp3')
all_volume = [COINMP3, SWORDPLMP3, SKELETMP3, DMGPLMP3, RUNMP3, HILSTMP3, KUVALDAMP3, PAYMP3, LISTMMP3, LISTMP3,
              BLUMMP3, MMM]
for i in all_volume:
    i.set_volume(music_volume)
st_time = time.time()

buy_cena = [25, 25, 25, 25, 25]


class Play_bt(pygame.sprite.Sprite):
    def __init__(self, p_x, p_y, sz):
        super().__init__(play)
        self.image = load_image('PLAY.png')
        self.image = pygame.transform.scale(self.image, sz)
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y

    def click(self, pos):
        if self.rect.collidepoint(pos):
            return False
        return True


class Exit_bt(pygame.sprite.Sprite):
    def __init__(self, p_x, p_y, sz):
        super().__init__(play)
        self.image = load_image('EXIT.png')
        self.image = pygame.transform.scale(self.image, sz)
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y

    def click(self, pos):
        if self.rect.collidepoint(pos):
            return False
        return True


class Start_bt(pygame.sprite.Sprite):
    def __init__(self, p_x, p_y, sz):
        super().__init__(play)
        self.image = load_image('start_1.png', -1)
        self.image = pygame.transform.scale(self.image, sz)
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y

    def click(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False


def start():
    size = width, height = 512, 512
    screen = pygame.display.set_mode(size)
    running = True
    img = pygame.transform.scale(load_image('fon_2.png'), (512, 512))
    pl_b = Play_bt(150, 200, (72 * 3, 20 * 3))
    ex_b = Exit_bt(200, 280, (38 * 3, 20 * 3))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    running = pl_b.click(event.pos)
                    if not(running):
                        for i in play:
                            i.kill()
                    if not (ex_b.click(event.pos)):
                        exit()
            if event.type == pygame.QUIT:
                exit()
        screen.fill('black')
        screen.blit(img, (0, 0))
        play.draw(screen)
        pygame.display.flip()
    pl_b.kill()


def end():
    screen.fill('white')
    pygame.display.flip()
    pygame.mixer.music.stop()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT, pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
                running = False
    exit()


def pause():
    running = True
    global flmouse
    volume_pos = int(all_volume[0].get_volume() * 250) + 249
    pl_b = Play_bt(240, 280, (72 * 3, 20 * 3))
    ex_b = Exit_bt(291, 350, (38 * 3, 20 * 3))
    p = pygame.transform.scale(load_image('pause.png', -1), (31 * 6, 8 * 6))
    menu = pygame.transform.scale(load_image('ramka.png', -1), (62 * 8, 62 * 8))
    volume = pygame.transform.scale(load_image('volume.png', -1), (50 * 0.8, 50 * 0.8))
    perg = pygame.transform.scale(load_image('parchment_1.png', -1), (860 * 0.8, 951 * 0.7))
    font = pygame.font.Font('data/font_2.ttf', 40)
    txt_1 = font.render(f'Урон: {pl.atk_mobs}', True, (0, 0, 0))
    txt_2 = font.render(f'Здоровье: {hp}', True, (0, 0, 0))
    txt_3 = font.render(f'Скорость бега: {x}', True, (0, 0, 0))
    txt_4 = font.render(f'Прыжок: {y_prig}', True, (0, 0, 0))
    while running:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                running = pl_b.click(event.pos)
                if not (ex_b.click(event.pos)):
                    exit()
                pos = event.pos
                if 250 <= pos[0] <= 500 and 462 <= pos[1] <= 478:
                    volume_pos = pos[0]
                    BLUMMP3.play()
                    for i in all_volume:
                        i.set_volume((pos[0] - 250) / 250)
                    pygame.mixer.music.set_volume((pos[0] - 250) / 250)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    pl_b.kill()
                    ex_b.kill()
            if event.type == pygame.MOUSEMOTION:
                flmouse = event.pos
        screen.fill(pygame.Color(133, 187, 204))
        oblaka.draw(screen)
        f1.draw(screen)
        texture.draw(screen)
        home1.draw(screen)
        nps.draw(screen)
        mobs.draw(screen)
        player.draw(screen)
        yandex.draw(screen)
        pygame.draw.rect(screen, 'red' if pl.dm else 'green', (10, 10, 200 * pl.hp / hp, 20))
        pygame.draw.rect(screen, 'white', (8, 8, 204, 24), 3)
        screen.blit(money, (5, 40))
        text_surface = my_font.render(str(pl.summ), False, 'white')
        screen.blit(text_surface, (35, 38))
        screen.blit(menu, (100, 80))
        screen.blit(p, (255, 150))
        screen.blit(volume, (180, 450))
        pygame.draw.rect(screen, pygame.Color(249, 242, 225), (250, 466, 250, 8))
        pygame.draw.rect(screen, pygame.Color(212, 133, 76), (volume_pos, 462, 5, 16))
        screen.blit(perg, (1200, -10))
        screen.blit(txt_1, (1380 + 10, 100))
        screen.blit(txt_2, (1380 + 10, 150))
        screen.blit(txt_3, (1380 + 10, 200))
        screen.blit(txt_4, (1380 + 10, 250))
        pygame.draw.rect(screen, pygame.Color(212, 133, 76), (volume_pos, 462, 5, 16))
        play.draw(screen)
        if flmouse != 0 and pygame.mouse.get_focused():
            screen.blit(arrow, flmouse)
            pygame.mouse.set_visible(False)
        pygame.display.flip()


def city1():
    Home((2000 - camera.ox, 420), 'house_1.png', (454, 234))
    Home((2500 - camera.ox, 535), 'kolodec.png', (128, 92))
    Home((2640 - camera.ox, 562), 'podsolnuh.png', (88, 64))
    Home((2860 - camera.ox, 515), 'bushes_1.png', (95 * 3, 37 * 3))
    Home((3400 - camera.ox, 562), 'podsolnuh.png', (88, 64))
    Home((3500 - camera.ox, 302), 'house_2.png', (384, 384))
    Home((3870 - camera.ox, 251), 'house_5.png', (384, 384))
    Doska((4300 - camera.ox, 476), 'Doska.png', (68 * 2.5, 61 * 2.5),
          [['Кузнец', 'Помоги построить дом', '100', '0', '0'], ['Ведьма', 'Помоги построить дом', '50', '0', '0'],
           ['Учитель', 'Помоги построить дом', '5', '0', '0'], ['Фермер', 'Помоги построить дом', '120', '0', '0']])
    Angel(4460 - camera.ox, 411, 'statya.png', (64 * 3, 72 * 3), 1000, 100)
    Home((4610 - camera.ox, 251), 'house_4.png', (384, 384))
    Home((4990 - camera.ox, 302), 'house_3.png', (384, 384))
    Home((5540 - camera.ox, 303), 'trees_1.png', (153 * 2, 162 * 2))
    Home((5360 - camera.ox, 325), 'pehc.png', (324 * 0.5, 624 * 0.5))
    Blacksmith(5510 - camera.ox, 470, 'BLACKSMITH', (672 // 7 * 2, 96 * 2))
    Home((5976 - camera.ox, 510), 'phenica.png', (155 * 2, 59 * 2))


def city1_kill():
    global home1
    for i in home1:
        i.kill()


def load_image(name, colorkey=None):
    fullname = os.path.join('../../Game/data', name)
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
    return framer, framel


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, args, hp, kd_atk):
        super().__init__(player, all_sprites)
        self.frame = dict()
        self.frame['run_right'], self.frame['run_left'] = cut_sheet(args[0][0], args[0][1], args[0][2])
        self.frame['run_right_sh'], self.frame['run_left_sh'] = cut_sheet(args[1][0], args[1][1], args[1][2])
        self.frame['jump_right'], self.frame['jump_left'] = cut_sheet(args[2][0], args[2][1], args[2][2])
        self.frame['atk1_right'], self.frame['atk1_left'] = cut_sheet(args[3][0], args[3][1], args[3][2])
        self.frame['atk_right_sh'], self.frame['atk_left_sh'] = cut_sheet(args[4][0], args[4][1], args[4][2])
        self.frame['atk2_right'], self.frame['atk2_left'] = cut_sheet(args[5][0], args[5][1], args[5][2])
        self.frame['death_right'], self.frame['death_left'] = cut_sheet(args[6][0], args[6][1], args[6][2])
        self.cut = 0
        self.cut_l = 'run_right'
        self.image = load_image('_Idle.png', -1).subsurface(pygame.Rect(0, 0, 120, 80))
        self.image = pygame.transform.scale(self.image, sz)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.sh = 0
        self.cut_p = 0
        self.p = 0
        self.fll = 1
        self.atk = 0
        self.hp = hp
        self.summ = 0
        self.kl = -1
        self.dm = 0
        self.timer_atk = 0
        self.kd_atk = kd_atk
        self.kd_dmg = 0
        self.atk_mobs = 10

    def update(self, move_x, move_y, sh=None, prob=None):
        if self.dm:
            self.dm = 0
        global x, y
        if self.kl >= 0:
            if self.kl == 0:
                end()
                self.kill()
                return
            else:
                if self.cut_l == 'run_left':
                    self.image = self.frame['death_left'][10 - self.kl]
                else:
                    self.image = self.frame['death_right'][10 - self.kl]
                self.kl -= 1
                return
        for i in mobs:
            if pygame.sprite.collide_mask(i, self) and i.getName() == 'Coin':
                COINMP3.play()
                i.sobr()
        if move_y != 0:
            self.p = move_y
        if self.atk > 0:
            return
        if self.p != 0:
            y = 0
            if prob == 1:
                self.rect.y -= self.p
                if self.cut_l == 'run_right':
                    self.image = self.frame['jump_right'][self.p % 3]
                else:
                    self.image = self.frame['jump_left'][self.p % 3]
                self.p -= 1
            elif move_x != 0:
                self.rect.x += x * move_x
                if move_x == 1:
                    self.cut_l = 'run_right'
                else:
                    self.cut_l = 'run_left'
        elif move_x == 0 and move_y == 0:
            image = load_image('_Idle.png', -1).subsurface(pygame.Rect(0, 0, 120, 80))
            if sh:
                image = load_image('_Crouch.png', -1)
            fll = self.fll
            self.fll = 1
            self.rect.y += 5
            img = self.image
            self.image = load_image('_Idle.png', -1).subsurface(pygame.Rect(240, 0, 120, 80))
            for i in texture:
                if pygame.sprite.collide_mask(self, i):
                    self.fll = 0
                    y = 0
                    if fll == 1:
                        while pygame.sprite.collide_mask(self, i):
                            self.rect.y -= 1
                        self.rect.y += 11
                        img = load_image('_Idle.png', -1).subsurface(pygame.Rect(240, 0, 120, 80))
                        if self.cut_l == 'run_left':
                            img = pygame.transform.flip(img, 1, 0)
                    break
            self.rect.y -= 5
            self.image = pygame.transform.scale(img, sz)
            if self.fll:
                self.cut_p = (self.cut_p + 1) % 6
                self.rect.y += y
                y += 2
            if self.cut_l == 'run_right' and sh in [0, 1]:
                self.image = pygame.transform.scale(image, sz)
            elif self.cut_l == 'run_left' and sh in [0, 1]:
                self.image = pygame.transform.scale(pygame.transform.flip(image, 1, 0), sz)
        elif sh:
            if move_x == 1:
                self.rect.x += x // 2
                if self.cut_l == 'run_right':
                    self.cut = (self.cut + 1) % len(self.frame['run_right_sh'])
                else:
                    self.cut_l = 'run_right'
                    self.cut = 0
                self.image = self.frame['run_right_sh'][self.cut]
            if move_x == -1:
                self.rect.x -= x // 2
                if self.cut_l == 'run_left':
                    self.cut = (self.cut + 1) % len(self.frame['run_left_sh'])
                else:
                    self.cut_l = 'run_left'
                    self.cut = 0
                self.image = self.frame['run_left_sh'][self.cut]
        else:
            if self.cut == 0:
                RUNMP3.play()
            if move_x == 1:
                self.rect.x += x
                if self.cut_l == 'run_right':
                    self.cut = (self.cut + 1) % len(self.frame['run_right'])
                else:
                    self.cut_l = 'run_right'
                    self.cut = 0
                self.image = self.frame['run_right'][self.cut]
            if move_x == -1:
                self.rect.x -= x
                if self.cut_l == 'run_left':
                    self.cut = (self.cut + 1) % len(self.frame['run_left'])
                else:
                    self.cut_l = 'run_left'
                    self.cut = 0
                self.image = self.frame['run_left'][self.cut]
        if self.fll:
            self.image = pygame.transform.scale(
                load_image('_Fall.png', -1).subsurface(pygame.Rect(self.cut_p // 2 * 120, 0, 120, 80)), sz)
            if self.cut_l == 'run_left':
                self.image = pygame.transform.flip(self.image, 1, 0)
        self.mask = pygame.mask.from_surface(self.image)

    def atkf(self, f=0, sh=0, img=0):
        global y
        if f in [4, 6] and self.atk == 0 and time.time() - self.timer_atk > self.kd_atk and y == 0 and self.p == 0:
            self.atk = f
            self.img = img
            self.timer_atk = time.time()
            """SWORDPLMP3.play()"""
            MMM.play()
        elif self.atk > 0:
            if sh:
                if self.cut_l == 'run_right':
                    self.image = self.frame['atk_right_sh'][4 - self.atk]
                else:
                    self.image = self.frame['atk_left_sh'][4 - self.atk]
            elif self.img == 1:
                if self.cut_l == 'run_right':
                    self.image = self.frame['atk1_right'][4 - self.atk]
                else:
                    self.image = self.frame['atk1_left'][4 - self.atk]
            else:
                if self.cut_l == 'run_right':
                    self.image = self.frame['atk2_right'][6 - self.atk]
                else:
                    self.image = self.frame['atk2_left'][6 - self.atk]
            self.atk -= 1
            self.mask = pygame.mask.from_surface(self.image)
            for i in mobs:
                if pygame.sprite.collide_mask(self, i):
                    i.update(hp=self.atk_mobs)

    def mask_peres(self):
        for i in texture:
            if pygame.sprite.collide_mask(self, i):
                return 1
        return 0

    def dmg(self, hp):
        if time.time() - self.kd_dmg > 0.3:
            DMGPLMP3.play()
            self.kd_dmg = time.time()
        self.hp -= hp
        self.dm = 1
        if self.hp <= 0 and self.kl == -1:
            self.kl = 10


class ObjT(pygame.sprite.Sprite):
    def __init__(self, pos, name):
        super().__init__(texture, all_sprites)
        self.image = load_image(name)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Fon1(pygame.sprite.Sprite):
    def __init__(self, pos, img, s, f=0):
        if f:
            super().__init__(texture, all_sprites)
        else:
            super().__init__(f1, all_sprites)
        self.image = load_image(img)
        self.image = pygame.transform.scale(self.image, s)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def getName(self):
        return self.__class__.__name__


class Home(pygame.sprite.Sprite):
    def __init__(self, pos, img, s):
        super().__init__(home1, all_sprites)
        self.image = load_image(img)
        self.image = pygame.transform.scale(self.image, s)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]


class Skelet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, args, pl, hp, atk, s):
        super().__init__(mobs, all_sprites)
        self.frame = dict()
        self.frame['run_right'], self.frame['run_left'] = cut_sheet(args[0][0], args[0][1], args[0][2], sz=(180, 120))
        self.frame['atk_right'], self.frame['atk_left'] = cut_sheet(args[1][0], args[1][1], args[1][2], sz=(180, 120))
        self.frame['die_right'], self.frame['die_left'] = cut_sheet(args[2][0], args[2][1], args[2][2], sz=(180, 120))
        self.frame['dmg_right'], self.frame['dmg_left'] = cut_sheet(args[3][0], args[3][1], args[3][2], sz=(180, 120))
        self.image = self.frame['run_left'][0]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.hp = hp
        self.kl = -1
        self.fldmg = -1
        self.pl = pl
        self.cut_l = 'left'
        self.cut = 0
        self.atk = 0
        self.dlatk = atk
        self.s = s
        self.nopl = 0

    def update(self, hp=0):
        self.image = self.frame['run_left'][0]
        if self.kl == 0:
            Coin(self.rect.x + 80, self.rect.y + 50, self.s)
            self.kill()
        elif self.kl > 0:
            self.image = self.frame['die_left' if self.cut_l == 'left' else 'die_right'][13 - self.kl]
            self.kl -= 1
        else:
            if hp > 0:
                SKELETMP3.play()
                self.hp -= hp
                self.fldmg = 0
            if self.atk > 0:
                self.image = self.frame['atk_left'][self.dlatk - self.atk] if self.cut_l == 'left' else \
                    self.frame['atk_right'][
                        self.dlatk - self.atk]
                self.mask = pygame.mask.from_surface(self.image)
                if pygame.sprite.collide_mask(self, self.pl):
                    self.pl.dmg(10)
                self.atk -= 1
                if self.atk == 0:
                    pygame.time.set_timer(MOB, 50)
            elif self.fldmg > -1:
                self.image = self.frame['dmg_left'][self.fldmg] if self.cut_l == 'left' else self.frame['dmg_right'][
                    self.fldmg]
                self.fldmg += 1
                if self.fldmg == 5:
                    self.fldmg = -1
            else:
                if abs(self.rect.x - self.pl.rect.x) <= 600:
                    if self.pl.rect.x < self.rect.x:
                        self.cut_l = 'left'
                    else:
                        self.cut_l = 'right'
                if abs(self.rect.x - self.pl.rect.x) > 600:
                    if random.randint(1, 10) == 1:
                        self.nopl = random.randint(1, 5)
                    nopl = self.nopl
                else:
                    nopl = -1
                if (self.pl.rect.x + 100 < self.rect.x and abs(self.rect.x - self.pl.rect.x) <= 600) or nopl == 1:
                    self.rect.x -= 3
                    if self.cut_l == 'left':
                        self.cut = (self.cut + 1) % 10
                    else:
                        self.cut, self.cut_l = 0, 'left'
                    self.image = self.frame['run_left'][self.cut]
                elif (self.pl.rect.x - 60 > self.rect.x and abs(self.rect.x - self.pl.rect.x) <= 600) or nopl == 2:
                    self.rect.x += 3
                    if self.cut_l == 'right':
                        self.cut = (self.cut + 1) % 10
                    else:
                        self.cut, self.cut_l = 0, 'right'
                    self.image = self.frame['run_right'][self.cut]
                else:
                    if (self.rect.x - 100 <= pl.rect.x <= self.rect.x + 10 and
                            self.atk == 0 or self.rect.x + 60 >= pl.rect.x >= self.rect.x):
                        self.atk = self.dlatk
                        pygame.time.set_timer(MOB, 80)
                    self.image = self.frame['atk_left'][0] if self.cut_l == 'left' else self.frame['atk_right'][0]
            self.mask = pygame.mask.from_surface(self.image)

            if self.hp <= 0:
                self.kl = 13

    def getName(self):
        return self.__class__.__name__


class Coin(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, summ):
        super().__init__(mobs, all_sprites)
        self.frame = cut_sheet('coin', 14, 1, (32, 32))[0]
        self.image = self.frame[0]
        self.rect = self.image.get_rect()
        self.cut = 0
        self.rect.x, self.rect.y = pos_x, pos_y
        self.nominal = summ
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, hp=0):
        self.cut = (self.cut + 1) % 14
        self.image = self.frame[self.cut]
        self.mask = pygame.mask.from_surface(self.image)

    def sobr(self):
        global pl
        pl.summ += self.nominal
        self.kill()

    def getName(self):
        return self.__class__.__name__


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.ox = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        try:
            if obj.getName() == 'Fon1':
                if obj.rect.x < -300:
                    obj.rect.x += 2200
                elif obj.rect.x > 1900:
                    obj.rect.x -= 2200
        except Exception:
            pass

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.ox -= self.dx


class Clouds(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(oblaka)
        self.spd = random.randint(1, 3)
        sz = random.randint(1, 5)
        self.image = pygame.transform.scale(load_image('cloud.png'), (71, 80))
        self.image = pygame.transform.scale(self.image, (71 * sz, 80 * sz))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = random.randint(-300, 2300)
        self.rect.y = random.randint(0, 100)
        fl = 1
        while fl:
            fl = 0
            self.rect.x = random.randint(-2000, 3000)
            self.rect.y = random.randint(-200, 30)
            for i in oblaka:
                if self != i:
                    if pygame.sprite.collide_mask(self, i) and self != i:
                        fl = 1
                        break

    def update(self):
        self.rect.x -= self.spd
        if self.rect.x < -300:
            self.rect.x += 2300
        """for i in yandex:
            if pygame.sprite.collide_rect(self, i):
                self.rect.x = 3000
                break"""


class Angel(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, img, sz, hp, t):
        super().__init__(nps, all_sprites)
        self.image = pygame.transform.scale(load_image(img), sz)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.hp = hp
        self.timeogid = t
        self.timee = 0

    def update(self, pl, hp):
        HILSTMP3.play()
        pl.hp = min(pl.hp + min(self.hp, (time.time() - self.timee) * self.hp / self.timeogid), hp)
        self.timee = time.time()

    def getName(self):
        return self.__class__.__name__


class Armor(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, img, img2, sz, price, inf):
        super().__init__(armor, all_sprites)
        self.image = pygame.transform.scale(load_image(img, -1), sz)
        self.img_pasiv = pygame.transform.scale(load_image(img, -1), sz)
        self.img_aktiv = pygame.transform.scale(load_image(img2, -1), sz)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x, self.rect.y = pos_x, pos_y
        self.inf = inf
        self.price = price

    def update(self, fl):
        if fl:
            self.image = self.img_aktiv
        else:
            self.image = self.img_pasiv

    def click(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False


class Blacksmith(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, img, sz):
        super().__init__(nps, home1, all_sprites)
        self.frame = cut_sheet(img, 7, 1, sz)[0]
        self.cut = 0
        self.image = self.frame[self.cut]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self, fl=0):
        if fl:
            pygame.mixer.music.pause()
            running = True
            Armor(1380, 80, 'helmet.png', 'helmet_s.png', (32 * 3, 36 * 3), buy_cena[0], [])
            Armor(1338, 195, 'breastplate.png', 'breastplate_s.png', (60 * 3, 50 * 3), buy_cena[1], [])
            Armor(1368, 350, 'pants.png', 'pants_s.png', (40 * 3, 38 * 3), buy_cena[2], [])
            Armor(1620, 160, 'sword_k.png', 'sword_k_s.png', (12 * 6, 54 * 6), buy_cena[3], [])
            Armor(1342, 480, 'bb.png', 'bb_s.png', (174, 112), buy_cena[4], [])
            global flmouse
            buy = []
            rmk = pygame.transform.scale(load_image('ramka_2.png', -1), (62 * 10.2, 62 * 10.2))
            rmk_buy = pygame.transform.scale(load_image('ramka_buy.png', -1), (62 * 3, 62 * 3))
            while running:
                for event in pygame.event.get():
                    if event.type in [pygame.QUIT]:
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            running = False
                            k = 0
                            for i in armor:
                                buy_cena[k] = i.price
                                k += 1
                                i.kill()
                            pygame.mixer.music.unpause()
                    if event.type == pygame.MOUSEMOTION:
                        flmouse = event.pos
                        fl_m = 1
                        for i in armor:
                            i.update(i.click(event.pos))
                            if i.click(event.pos):
                                buy = ['1']
                                fl_m = 0
                        if fl_m:
                            buy = []
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0]:
                            for i in armor:
                                if i.click(event.pos):
                                    if i.price <= pl.summ:
                                        pl.summ -= i.price
                                        i.price *= 2
                                        PAYMP3.play()
                screen.fill(pygame.Color(133, 187, 204))
                oblaka.draw(screen)
                f1.draw(screen)
                texture.draw(screen)
                home1.draw(screen)
                nps.draw(screen)
                mobs.draw(screen)
                player.draw(screen)
                yandex.draw(screen)
                pygame.draw.rect(screen, 'red' if pl.dm else 'green', (10, 10, 200 * pl.hp / hp, 20))
                pygame.draw.rect(screen, 'white', (8, 8, 204, 24), 3)
                screen.blit(money, (5, 40))
                text_surface = my_font.render(str(pl.summ), False, 'white')
                screen.blit(text_surface, (35, 38))
                screen.blit(rmk, (1200, 10))
                armor.draw(screen)
                if len(buy) > 0:
                    screen.blit(rmk_buy, (1008, 10))
                if flmouse != 0 and pygame.mouse.get_focused():
                    screen.blit(arrow, flmouse)
                    pygame.mouse.set_visible(False)
                pygame.display.flip()
        else:
            self.cut = (self.cut + 1) % 7
            if self.cut == 1 and 300 < self.rect.x < 1500:
                KUVALDAMP3.play()
            if self.cut == 6:
                pygame.time.set_timer(BLACKSMITH, 1000)
            elif self.cut == 0:
                pygame.time.set_timer(BLACKSMITH, 100)
            self.image = self.frame[self.cut]

    def getName(self):
        return self.__class__.__name__


class List_Kvest(pygame.sprite.Sprite):
    def __init__(self, img, sz, inf):
        super().__init__(lst, all_sprites)
        self.image = pygame.transform.scale(load_image(img), sz)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.y = random.randint(110, 388)
        self.rect.x = random.randint(170, 700)
        self.inf = inf
        fll = 1
        while fll:
            fll = 0
            for i in lst:
                if i != self:
                    if pygame.sprite.collide_mask(i, self):
                        self.rect.y = random.randint(110, 388)
                        self.rect.x = random.randint(170, 650)
                        fll = 1
                        break

    def click(self, pos):
        if self.rect.collidepoint(pos):
            return True
        return False


class Kvest(pygame.sprite.Sprite):
    def __init__(self, inf):
        super().__init__(lstk, all_sprites)
        self.image = pygame.transform.scale(load_image('list_3.png'), (474 * 1, 700 * 0.8))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 1300
        self.rect.y = 50
        self.txt, self.cena, self.rep, self.rep_f = inf[0], inf[1], inf[2], inf[3]
        font = pygame.font.Font('data/font_1.ttf', 50)
        self.cena_k = font.render(inf[2], True, (0, 0, 0))
        self.txt_k = font.render(inf[0], True, (0, 0, 0))
        self.rep_k = font.render(inf[3], True, (0, 0, 0))
        self.rep_f_k = font.render(inf[4], True, (0, 0, 0))
        font = pygame.font.Font('data/font_1.ttf', 25)
        self.op_k = font.render(inf[1], True, (0, 0, 0))


class Doska(pygame.sprite.Sprite):
    def __init__(self, pos, img, sz, args):
        super().__init__(nps, all_sprites)
        self.image = pygame.transform.scale(load_image(img), sz)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.spisok_kvestov = args
        self.pers_gr = load_image('pers_gr.png', -1)
        self.pers_rd = load_image('pers_rd.png', -1)
        self.start = load_image('start_1.png', -1)
        self.i = 0

    def update(self):
        pygame.mixer.music.pause()
        running = True
        global flmouse, screen
        for _ in self.spisok_kvestov:
            List_Kvest('list_2.png', (11 * 10, 15 * 10), _)
        dsk = pygame.transform.scale(load_image('dsk.png', -1), (609 * 1.3, 448 * 1.3))
        while running:
            for event in pygame.event.get():
                if event.type in [pygame.QUIT]:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        pygame.mixer.music.unpause()
                        for i in lst:
                            i.kill()
                        for i in lstk:
                            i.kill()
                        for i in play:
                            i.kill()
                if event.type == pygame.MOUSEMOTION:
                    flmouse = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        for i in play:
                            if i.click(event.pos):
                                for j in range(len(self.spisok_kvestov)):
                                    if self.spisok_kvestov[j] == self.i.inf:
                                        del self.spisok_kvestov[j]
                                        tetris()
                                        screen = pygame.display.set_mode(size)
                                        window.position = (0, 0)
                                        LISTMMP3.play()
                                        break
                                self.i.kill()
                                for j in lstk:
                                    j.kill()
                                for j in play:
                                    j.kill()
                                self.i = 0
                        for i in lst:
                            if i.click(event.pos):
                                LISTMP3.play()
                                for j in lstk:
                                    j.kill()
                                for j in play:
                                    j.kill()
                                self.i = i
                                kv = Kvest(i.inf)
                                Start_bt(1425, 490, (226, 116))
            screen.fill(pygame.Color(133, 187, 204))
            oblaka.draw(screen)
            f1.draw(screen)
            texture.draw(screen)
            home1.draw(screen)
            nps.draw(screen)
            mobs.draw(screen)
            player.draw(screen)
            yandex.draw(screen)
            pygame.draw.rect(screen, 'red' if pl.dm else 'green', (10, 10, 200 * pl.hp / hp, 20))
            pygame.draw.rect(screen, 'white', (8, 8, 204, 24), 3)
            screen.blit(money, (5, 40))
            text_surface = my_font.render(str(pl.summ), False, 'white')
            screen.blit(text_surface, (35, 38))
            screen.blit(dsk, (100, 40))
            lst.draw(screen)
            lstk.draw(screen)
            if self.i != 0:
                screen.blit(kv.txt_k, (1350, 100))
                screen.blit(kv.op_k, (1350, 190))
                screen.blit(pygame.transform.scale(money, (32 * 2, 32 * 2)), (1350, 400))
                screen.blit(kv.cena_k, (1423, 412))
                screen.blit(self.pers_gr, (1350, 450))
                screen.blit(kv.rep_k, (1423, 470))
                screen.blit(self.pers_rd, (1550, 450))
                screen.blit(kv.rep_f_k, (1623, 470))
            play.draw(screen)
            if flmouse != 0 and pygame.mouse.get_focused():
                screen.blit(arrow, flmouse)
                pygame.mouse.set_visible(False)
            pygame.display.flip()

    def getName(self):
        return self.__class__.__name__


class Yandex(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, img, sz):
        super().__init__(yandex, all_sprites)
        self.image = pygame.transform.scale(load_image(img), sz)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = pos_x
        self.rect.y = pos_y


if __name__ == '__main__':
    pygame.init()
    start()
    clock = pygame.time.Clock()
    pygame.display.set_caption('Тут пусто')
    size = width, height = 2000, 650
    screen = pygame.display.set_mode(size)
    window = Window.from_display_module()
    window.position = (0, 0)
    running = True
    pygame.mixer.music.load('data/LES.mp3')
    pygame.mixer.music.play(-1)
    HODR = pygame.USEREVENT + 1
    HODL = pygame.USEREVENT + 2
    HODSTOP = pygame.USEREVENT + 3
    HODPROB = pygame.USEREVENT + 4
    HODATK = pygame.USEREVENT + 5
    MOB = pygame.USEREVENT + 6
    OBLAKA = pygame.USEREVENT + 7
    BLACKSMITH = pygame.USEREVENT + 8
    pygame.time.set_timer(BLACKSMITH, 100)
    pygame.time.set_timer(OBLAKA, 100)
    pygame.time.set_timer(MOB, 55)
    pygame.time.set_timer(HODATK, 0)
    pygame.time.set_timer(HODL, 0)
    pygame.time.set_timer(HODR, 0)
    pygame.time.set_timer(HODPROB, 0)
    pygame.time.set_timer(HODSTOP, 50)
    sh = 0
    atk = 0
    hp = 1000
    atkfl = 0
    jump = 17
    flmouse = 0
    kd_atk = 1
    camera = Camera()
    e = pygame.transform.scale(load_image('e.png'), (32 * 2, 32 * 2))
    sword_kd = pygame.transform.scale(load_image('Sword4.png', -1), (200, 40))
    sword_kdno = pygame.transform.scale(load_image('Sword2.png', -1), (200, 40))
    for i in range(15):
        Clouds()
    pl = Player(800, 300,
                [['_Run', 10, 1], ['_CrouchWalk', 8, 1], ['_Jump', 3, 1], ['_Attack', 4, 1],
                 ['_CrouchAttack', 4, 1], ['_Attack2', 6, 1], ['_Death', 10, 1]], 1000, kd_atk)
    for i in range(-1, 6):
        Yandex(-500, 100 * i, 'yandex.png', (200, 150))
    for i in range(-1, 7):
        Fon1((i * 300, 470), 'Ground.png', (353, 180), f=1)
    for i in range(2, 10):
        if i % 3 != 0:
            i = (1000 * i, 507)
            Skelet(i[0], i[1],
                   [['Skeleton_01_White_Walk', 10, 1], ['Skeleton_01_White_Attack2', 9, 1],
                    ['Skeleton_01_White_Die', 13, 1],
                    ['Skeleton_01_White_Hurt', 5, 1]], pl, 100, 9, 5)
    for i in range(1, 6):
        i = (3000 * i, 507)
        Skelet(i[0], i[1],
               [['Skeleton_01_Yellow_Walk', 10, 1], ['Skeleton_01_Yellow_Attack1', 10, 1],
                ['Skeleton_01_Yellow_Die', 13, 1],
                ['Skeleton_01_Yellow_Hurt', 5, 1]], pl, 300, 10, 10)
    for i in range(8):
        Angel(10000 * i, 556 - 144, 'statya.png', (64 * 3, 72 * 3), 1000, 100)
    money = pygame.transform.scale(load_image('coin.png', -1).subsurface(pygame.Rect(0, 0, 16, 16)), (32, 32))
    my_font = pygame.font.SysFont('Comic Sans MS', 24)
    arrow = load_image('01.png', -1)
    for i in range(20):
        Fon1((i * 37 * 3 - 79, 147 if i % 2 == 0 else 187), 'Pine Tree - GREEN  - 0000.png', (53 * 5, 96 * 5))
    for i in range(10):
        Fon1((i * 74 * 3 - 100, 260), 'Large Spruce Tree - GREEN_TEAL - 0000.png', (74 * 3, 128 * 3))
    for i in range(10):
        Fon1((i * 74 * 3 + 37 * 3 - 118.5, 196), 'Large Spruce Tree - NIGHT - 0000.png', (74 * 3 + 37, 128 * 3 + 64))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    pygame.time.set_timer(HODR, 50)
                    pygame.time.set_timer(HODL, 0)
                if event.key == pygame.K_a:
                    pygame.time.set_timer(HODL, 50)
                    pygame.time.set_timer(HODR, 0)
                if event.key == pygame.K_LSHIFT:
                    sh = 1
                    player.update(0, 0, sh)
                if event.key == pygame.K_SPACE:
                    if pl.mask_peres():
                        player.update(0, y_prig)
                        jump = 0
                        pygame.time.set_timer(HODPROB, 30)
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.pause()
                    pygame.time.set_timer(HODL, 0)
                    pygame.time.set_timer(HODR, 0)
                    pause()
                    pl.update(0, 0, sh)
                    pygame.mixer.music.unpause()
                if event.key == pygame.K_e:
                    for i in nps:
                        if pygame.sprite.collide_mask(pl, i):
                            n = i.getName()
                            if n == 'Angel':
                                i.update(pl, hp)
                            elif n == 'Doska':
                                i.update()
                                pygame.time.set_timer(HODL, 0)
                                pygame.time.set_timer(HODR, 0)
                                pl.update(0, 0, sh)
                            elif n == 'Blacksmith':
                                i.update(1)
                                pygame.time.set_timer(HODL, 0)
                                pygame.time.set_timer(HODR, 0)
                                pl.update(0, 0, sh)
                            break
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    pygame.time.set_timer(HODR, 0)
                    player.update(0, 0, sh)
                if event.key == pygame.K_a:
                    pygame.time.set_timer(HODL, 0)
                    player.update(0, 0, sh)
                if event.key == pygame.K_LSHIFT:
                    sh = 0
                    player.update(0, 0, sh)
            if event.type == HODR:
                f = 1
                for i in home1:
                    f -= 1
                    break
                if 0 <= camera.ox <= 6500 and f:
                    city1()
                elif camera.ox > 6500 or camera.ox < 0:
                    city1_kill()
                player.update(1, 0, sh)
            if event.type == HODL:
                fly = 1
                f = 1
                for i in home1:
                    f -= 1
                    break
                if 0 <= camera.ox <= 6500 and f:
                    city1()
                elif camera.ox > 6500 or camera.ox < 0:
                    city1_kill()
                for i in yandex:
                    if pygame.sprite.collide_rect(pl, i):
                        fly = 0
                        pygame.time.set_timer(HODL, 0)
                        player.update(0, 0, sh)
                        break
                if fly:
                    player.update(-1, 0, sh)
            if event.type == HODSTOP:
                player.update(0, 0)
            if event.type == HODPROB:
                if atk == 0:
                    player.update(0, 0, prob=1)
                    jump += 1
                    if jump == y_prig:
                        pygame.time.set_timer(HODPROB, 0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if atk == 0:
                    if pygame.mouse.get_pressed()[0] or sh:
                        pl.atkf(4, img=1)
                        atk = pl.atk
                    elif pygame.mouse.get_pressed()[2]:
                        pl.atkf(6, img=2)
                        atk = pl.atk
                    pygame.time.set_timer(HODATK, 80)
            if event.type == HODATK:
                if atk > 0:
                    atk -= 1
                    pl.atkf(sh=sh)
                else:
                    player.update(0, 0, sh)
                    pygame.time.set_timer(HODATK, 0)
            if event.type == BLACKSMITH:
                for i in nps:
                    if i.getName() == 'Blacksmith':
                        i.update()
            if event.type == MOB:
                mobs.update()
            if event.type == pygame.MOUSEMOTION:
                flmouse = event.pos
            if event.type == OBLAKA:
                oblaka.update()
        camera.update(pl)
        for sprite in all_sprites:
            camera.apply(sprite)
        fle = 0
        for i in nps:
            if pygame.sprite.collide_mask(pl, i):
                fle = 1
                break
        screen.fill(pygame.Color(133, 187, 204))
        oblaka.draw(screen)
        f1.draw(screen)
        texture.draw(screen)
        home1.draw(screen)
        nps.draw(screen)
        mobs.draw(screen)
        player.draw(screen)
        yandex.draw(screen)
        pygame.draw.rect(screen, 'red' if pl.dm else 'green', (10, 10, 200 * pl.hp / hp, 20))
        pygame.draw.rect(screen, 'white', (8, 8, 204, 24), 3)
        screen.blit(money, (5, 40))
        text_surface = my_font.render(str(pl.summ), False, 'white')
        screen.blit(text_surface, (35, 38))
        if time.time() - pl.timer_atk > kd_atk:
            screen.blit(sword_kdno, (5, 75))
        else:
            screen.blit(sword_kd, (5, 75))
            pygame.draw.rect(screen, pygame.Color(221, 180, 100),
                             (4, 93, min(int((time.time() - pl.timer_atk) / kd_atk * 200), 200), 5))
        if fle:
            screen.blit(e, (250, 10))
        if flmouse != 0 and pygame.mouse.get_focused():
            screen.blit(arrow, flmouse)
            pygame.mouse.set_visible(False)
        pygame.display.flip()
    pygame.quit()
