from GameObject import GameObject
from timeit import default_timer as timer
from GC import *


class Ground(GameObject):

    def __init__(self, image, coords, speed):
        GameObject.__init__(self, image, coords, speed)
        self.start = timer()

    def update(self):
        self.pos = (self.pos[0] + self.speed, self.pos[1])
        end = timer()

        if end - self.start > 15:
            self.start = end
            self.speed += self.speed * .15

        if -self.pos[0] > .65 * ground_len:
            self.pos = (0, ground_y)