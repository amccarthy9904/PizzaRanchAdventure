import pygame
from BOI import BOI
from ground import Ground
from score import Score
from GC import *
from background import BackGround

def main():
    pygame.init()
    screen = pygame.display.set_mode((1440,900))

    running = True
    bottom = Ground(pygame.image.load(ground_path), (0, ground_y), ground_start_speed)
    #sky = BackGround(pygame.image.load("mountains2.png"), pygame.image.load("sky.jpg"))
    boi = BOI(pygame.image.load(player_path), (0,boi_start_y), boi_start_speed, bottom)
    score = Score(None, score_pos, 0, bottom)
    objs = [boi, bottom, score]

    while running:

        screen.fill((0,0,0))
        keys = pygame.key.get_pressed()

        if(keys[pygame.K_w]):
            boi.jump()
        if(keys[pygame.K_s]):
            boi.fall()
        if(keys[pygame.K_a]):
            boi.move_left()
        if(keys[pygame.K_d]):
            boi.move_right()

        #sky.update(screen)
        for obj in objs:
            obj.update()
            screen.blit(obj.img, obj.pos)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()