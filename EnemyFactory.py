from GameObject import GameObject
import pygame as pygame
from GC import *

class EnemyFactor(GameObject):

    def __init__(self, image, coords, speed, ground, screen):
        GameObject.__init__(self, image, coords, speed)
        self.ground = ground
        self.screen = screen
        