import pygame
import constant as c
from balls import Ball, CueBall
from collision import wall_collision, collision
from vector import Vector

class Scene():
    def __init__(self):
        self.border_width = 20
        self.cue = CueBall((300,500), c.white)
        # self.balls = [self.cue, Ball((300,200),c.ball_color[0],),
        #       Ball((277, 160), c.ball_color[1]), 
        #       Ball((323, 160), c.ball_color[2]), 
        #       Ball((254, 120), c.ball_color[3]), 
        #       Ball((300, 120), c.ball_color[4]),
        #       Ball((346, 120), c.ball_color[5])
        #      ]
        self.balls = [self.cue, Ball((300,200),c.ball_color[0],),
              Ball((284, 168), c.ball_color[1]), 
              Ball((316, 168), c.ball_color[2]), 
              Ball((268, 136), c.ball_color[3]), 
              Ball((300, 136), c.ball_color[4]),
              Ball((332, 136), c.ball_color[5])
             ]
        
    def display(self, screen):
        
        for ball in self.balls:
            ball.display(screen)
    
        pygame.draw.rect(screen, c.dark_brown, (0,0, 600, self.border_width))
        pygame.draw.rect(screen, c.dark_brown, (0, self.border_width, self.border_width, 600-self.border_width))
        pygame.draw.rect(screen, c.dark_brown, (600-self.border_width,self.border_width, self.border_width, 600-self.border_width))
        pygame.draw.rect(screen, c.dark_brown, (self.border_width, 600- self.border_width, 600 - 2*self.border_width, self.border_width))

    def update(self, dt):
        for ball in self.balls:
            wall_collision(ball, self.border_width)
        for i in range(7):
            for j in range(7):
                if j <= i:
                    pass
                else:
                    collision (self.balls[i], self.balls[j])
                # if i != j:
                #     collision(self.balls[i], self.balls[j])

        # for i in range(len(self.balls)):
        #     for j in range(i + 1, len(self.balls)):  # Check each pair only once
        #         collision(self.balls[i], self.balls[j])

            
        for ball in self.balls:
            ball.velocity *= (1-ball.friction)
            if abs(ball.velocity.x) < c.minimum_velocity and abs(ball.velocity.y) < c.minimum_velocity:
                ball.velocity = Vector(0, 0)
            ball.update_position(dt)
       