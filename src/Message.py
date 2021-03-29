from GameObject import GameObject
import pygame as pygame
from GC import *


class Message(GameObject):

    def __init__(self, image, coords, speed, text_size):
        GameObject.__init__(self, image, coords, speed)
        self.font = pygame.font.Font(pygame.font.match_font("impact"), text_size)

    def update(self):
        pass


