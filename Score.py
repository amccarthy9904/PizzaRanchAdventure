from GameObject import GameObject
from Message import Message
from GC import *


class Score(Message):

    def __init__(self, image, coords, speed, ground, text_size):
        Message.__init__(self, image, coords, speed, text_size)
        self.points = 0
        self.ground = ground

    def update(self):
        self.points -= self.ground.speed * .1
        self.img = self.font.render(str(int(self.points)).encode("utf-8"), True, (0, 5, 0))



