
class BackGround():

    def __init__(self, img1, img2):
        self.layer1 = img1
        self.layer2 = img2
        self.pos1 = (700, 0)
        self.pos2 = (500, 0)

    def update(self, screen):
        screen.blit(self.layer2, self.pos2)
        screen.blit(self.layer1, self.pos1)