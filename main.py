import pygame
import sys 
import math
from vector import Vector
from balls import CueBall, Ball

import constant as c
from scene import Scene

WIDTH, HEIGHT = 600, 600
FPS = 60
dt = 1/FPS

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Physics Engine")

scene = Scene()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if scene.cue.velocity == Vector(0,0):
                    scene.cue.shoot(2000)
            elif event.key == pygame.K_LEFT:
                scene.cue.move_cue(0.5)
            elif event.key == pygame.K_RIGHT:
                scene.cue.move_cue(-0.5)

    screen.fill(c.green)
    scene.update(dt)
    scene.display(screen)
    pygame.display.flip()

    pygame.time.Clock().tick(FPS)