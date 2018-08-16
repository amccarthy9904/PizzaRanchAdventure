from GameObject import GameObject
from GC import *

class BOI(GameObject):

    is_jump = 0
    is_fall = 0
    v = boi_v
    m = boi_m

    def __init__(self, image, coords, speed, ground):
        GameObject.__init__(self, image, coords, speed)
        self.ground = ground

    def die(self):
        pass

    def update(self):
        if self.is_jump:
            if self.v > 0:
                F = (.3 * self.m * (self.v*self.v))
            elif self.is_fall:
                F = -(.05 * self.m * (self.v*self.v))
            else:
                F = -(.008 * self.m * (self.v*self.v))

            self.pos = (self.pos[0], self.pos[1] - F)
            self.v = self.v - 1

            if self.pos[1] >= boi_start_y:
                self.pos = (self.pos[0], boi_start_y)
                self.is_jump = 0
                self.is_fall = 0
                self.v = boi_v

    def move_right(self):
        self.pos = (self.pos[0] + self.speed, self.pos[1])

    def move_left(self):
        self.pos = (self.pos[0] - self.speed, self.pos[1])

    def jump(self):
        self.is_jump = 1

    def fall(self):
        self.is_fall = 1


