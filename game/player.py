import pygame
from glob import glob
import sys
 
 
pygame.init()
screen = pygame.display.set_mode((400, 600))
 
 
class Cat(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Cat, self).__init__()
        self.x = x
        self.y = y
        self.list = [self.convert("C:/Users/oatpt/Desktop/py/game/istockphoto-1297111821-612x612.jpg")]
        self.list_idle = [self.convert("C:/Users/oatpt/Desktop/py/game/istockphoto-1297111821-612x612.jpg")]
        self.counter = 0
        self.image = self.list[0]
        self.w, self.h = self.image.get_size()
        self.rect = self.image.get_rect()
        self.dir = ""
        self.prov = ""
        self.mask = pygame.mask.from_surface(self.image)
 
    def convert(self, f):
        imp=pygame.image.load(f).convert_alpha()
        DEFAULT_IMAGE_SIZE = (100,100 )
        imp = pygame.transform.scale(imp, DEFAULT_IMAGE_SIZE)
        return imp
        
    def update(self):
        self.counter += .1
        if self.counter >= len(self.list):
            self.counter = 0
        if self.dir == "right":
            self.image = self.list[int(self.counter)]
            self.prov = self.dir
        if self.dir == "left":
            self.image = pygame.transform.flip(self.list[int(self.counter)], True, False)
            self.prov = self.dir
        if self.dir == "":
            if self.counter >= len(self.list_idle):
                self.counter = 0
            if self.prov == "right":
                self.image = self.list_idle[int(self.counter)]
            else:
                self.image = pygame.transform.flip(self.list_idle[int(self.counter)], True, False)
 
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        screen.blit(self.image, (self.x, self.y))
 
 
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        super(Sprite, self).__init__()
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = pygame.Surface((self.w, self.h))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
 
    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        screen.blit(self.image, (self.x, self.y))
 
 
cat = Cat(100, 100)
clock = pygame.time.Clock()
floor = Sprite(100, 300, 60, 10)
while True:
    screen.fill((128, 255, 128))
 
 
 
    if pygame.event.get(pygame.QUIT):
        break
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
            if event.key == pygame.K_RIGHT:
                cat.dir = "right"
            if event.key == pygame.K_LEFT:
                cat.dir = "left"
            if event.key == pygame.K_UP:
                cat.dir = "up"
            if event.key == pygame.K_DOWN:
                cat.dir = "down"
        if event.type == pygame.KEYUP:
            # Make the 
            if cat.dir not in "down":
                cat.dir = ""
 
    if cat.dir == "right":
        cat.x += 1
    if cat.dir == "left":
        cat.x -= 1
    if cat.dir == "up":
        cat.y -= 2
 
    if cat.dir == "down":
        cat.dir = ""
 
    if not pygame.sprite.collide_mask(floor, cat):
        cat.y += 1
 
    # if not pygame.sprite.collide_rect(floor, cat):
    #     cat.y += 1
 
    if cat.y > 480:
        cat.y = 0
 
 
    cat.update()
    floor.update()
    pygame.display.update()
    clock.tick(180)
 
pygame.quit()