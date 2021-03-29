
class BackGround():

    def __init__(self, sky):
        self.sky = sky
        self.pos1 = (0, 0)

    def update(self, screen):
        screen.blit(self.sky, self.pos1)