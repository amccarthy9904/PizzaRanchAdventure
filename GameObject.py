import pygame
class GameObject:

    def __init__(self, image, coords, speed):
        if image is not None:
            self.img = pygame.image.load(image)
        self.pos = coords
        self.speed = speed

    def update(self):
        pass
