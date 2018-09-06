from GameObject import GameObject
import random
from Powerup import Powerup
from Enemy import Enemy
from GC import *


class EntityFactory(GameObject):

    def __init__(self, image, coords, speed, ground, screen):
        GameObject.__init__(self, image, coords, speed)
        self.ground = ground
        self.screen = screen
        self.entities = []
        self.cooldown = ef_cooldown

    def make_entity(self):
        choice = random.randint(1, 100)
        if choice <= 3:
            self.entities.append(Powerup(p_up_path, (e1_init_x, e_PU_init_y), self.ground.speed))
        elif choice <= 70:
            self.entities.append(Enemy(enemy_RS_path, (e2_init_x, e_RS_init_y), self.ground.speed))
        self.entities.append(Enemy(enemy_RS_path, (e1_init_x, e_RS_init_y), self.ground.speed))

    def update(self):
        self.cooldown -= 1
        if self.cooldown <= 0:
            self.make_entity()
            self.cooldown = ef_cooldown

        for entity in self.entities:
            entity.update()
            self.screen.blit(entity.img, entity.pos)
            if entity.pos[0] <= -200:
                self.entities.remove(entity)
