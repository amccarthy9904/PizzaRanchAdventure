import pygame


class GameObject:

    def __init__(self, image, coords, speed):
        if image is not None:
            self.img = pygame.image.load(image)
            self.rect = self.img.get_rect(center=coords)
        self.pos = coords
        self.speed = speed

    def update(self):
        pass
