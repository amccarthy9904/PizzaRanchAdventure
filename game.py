import pygame
from BOI import BOI
from ground import Ground
from Score import Score
from GC import *
from EnemyFactory import EnemyFactory
from Text import Text
from background import BackGround


pygame.init()
screen = pygame.display.set_mode((display_width,display_height))

bottom = Ground(ground_path, (0, ground_y), ground_start_speed)
#sky = BackGround(pygame.image.load("mountains2.png"), pygame.image.load("sky.jpg"))
boi = BOI(player_path, (0,boi_start_y), boi_start_speed)
enemy_fact = EnemyFactory(ef_path, ef_init_pos, None, bottom, screen)
score = Score(None, score_pos, 0, bottom, score_font_size)
objs = [enemy_fact, boi, bottom, score]


def message_to_screen(msg, color):
    objs.append(Text(None, text_pos, 0, "collision", 50))


def game_loop():

    running = True
    while running:

        screen.fill((0,0,0))
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            boi.jump()
        if keys[pygame.K_s]:
            boi.fall()
        if keys[pygame.K_a]:
            boi.move_left()
        if keys[pygame.K_d]:
            boi.move_right()

        #sky.update(screen)
        for obj in objs:
            obj.update()
            screen.blit(obj.img, obj.pos)
        pygame.display.update()

        for enemy in enemy_fact.enemies:
            if enemy.rect.collidepoint(boi.rect.center):
                message_to_screen("COLLISION", (255, 128, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == "__main__":
    game_loop()
