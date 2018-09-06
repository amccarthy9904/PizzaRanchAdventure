import pygame
from BOI import BOI
from ground import Ground
from Score import Score
from GC import *
from EntityFactory import EntityFactory
from Text import Text
from random import randint
from background import BackGround


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((display_width,display_height))


bottom = Ground(ground_path, (0, ground_y), ground_start_speed)
#sky = BackGround(pygame.image.load("mountains2.png"), pygame.image.load("sky.jpg"))
boi = BOI(player_path, (0,boi_start_y), boi_start_speed)
entity_fact = EntityFactory(ef_path, fact_init_pos, None, bottom, screen)
score = Score(None, score_pos, 0, bottom, score_font_size)
objs = [entity_fact, boi, bottom, score]


def message_to_screen(msg, color):
    objs.append(Text(None, text_pos, 0, msg, 50))

def new_track():
    pygame.mixer.music.load(music[randint(0,4)])
    pygame.mixer.music.play()

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

        for entity in entity_fact.entities:
            if entity.rect.collidepoint(boi.rect.center):
                message_to_screen("COLLISION", (255, 128, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not pygame.mixer.music.get_busy():
            new_track()

if __name__ == "__main__":
    game_loop()
