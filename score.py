from GameObject import GameObject
import pygame as pygame
from GC import *


class Score(GameObject):

    def __init__(self, image, coords, speed, ground):
        GameObject.__init__(self, image, coords, speed)
        self.points = 0
        self.ground = ground
        self.font = pygame.font.Font(pygame.font.match_font("impact"), score_font_size)

    def update(self):
        self.points -= self.ground.speed * .1
        self.img = self.font.render(str(int(self.points)).encode("utf-8"), True, (0, 128, 0))
        self.rect = self.img.get_rect()
        self.rect.midtop = (score_pos)
        self.pos = self.rect.midtop


