from GameObject import GameObject
import random
from Enemy import Enemy
import pygame as pygame
from GC import *


class EnemyFactory(GameObject):

    def __init__(self, image, coords, speed, ground, screen):
        GameObject.__init__(self, image, coords, speed)
        self.ground = ground
        self.screen = screen
        self.enemies = []
        self.cooldown = 500

    def make_enemy(self):
        choice = random.randint(1,101)
        if choice <= 60:
            self.enemies.append(Enemy(enemy_RS_path, (e1_init_x, e_RS_init_y), self.ground.speed))
            pass
        if choice <=85:
            self.enemies.append(Enemy(enemy_RS_path, (e1_init_x, e_RS_init_y), self.ground.speed))
            self.enemies.append(Enemy(enemy_RS_path, (e2_init_x, e_RS_init_y), self.ground.speed))
            pass
        else:
            self.enemies.append(Enemy(enemy_RS_path, (e1_init_x, e_RS_init_y), self.ground.speed))
            self.enemies.append(Enemy(enemy_RS_path, (e2_init_x, e_RS_init_y), self.ground.speed))
            self.enemies.append(Enemy(enemy_RS_path, (e3_init_x, e_RS_init_y), self.ground.speed))
            pass

    def update(self):
        self.cooldown -= 1
        if self.cooldown <= 0 and random.randint(1,51) > 49:
            self.make_enemy()
            self.cooldown = 500

        for enemy in self.enemies:
            enemy.update()
            self.screen.blit(enemy.img, enemy.pos)
            if enemy.pos[0] <= -200:
                self.enemies.remove(enemy)
