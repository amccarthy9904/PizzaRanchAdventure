from GameObject import GameObject
from Message import Message
import pygame as pygame
from GC import *


class Text(Message):

    def __init__(self, image, coords, speed, text, text_size):
        Message.__init__(self, image, coords, speed, text_size)
        self.text = text
        self.cooldown = text_cooldown
        self.img = self.font.render(self.text.encode("utf-8"), True, (255, 128, 0))

    def update(self):
        self.cooldown -= 1
        if self.cooldown <= 0:
            self.img = self.font.render("".encode("utf-8"), True, (255, 128, 0))
