from GameObject import GameObject


class Enemy(GameObject):

    def __init__(self, image, coords, speed):
        GameObject.__init__(self, image, coords, speed)

    def update(self):
        self.pos = (self.pos[0] + self.speed, self.pos[1])
        self.rect = self.img.get_rect(topleft=self.pos)
