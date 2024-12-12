import pygame
from vector import Vector
import constant as c 

class Ball():
    def __init__(self, center, color, friction = 0.02, bounce = 0.7, mass = 1):
        self.center = Vector (center[0], center[1])
        self.color = color
        self.radius = 20
        self.velocity = Vector (0,0)
        self.friction = friction
        self.bounce = bounce
        self.mass = mass

    def display(self, screen):
        pygame.draw.circle(screen, self.color, (self.center.x, self.center.y), self.radius) 

    def update_position(self,dt):
        self.center += self.velocity *dt
      
class CueBall(Ball):
    def __init__(self, center, color):
        super().__init__(center, color)
        self.cue_pos = Vector(self.center.x , self.center.y + self.radius)

    def display(self, screen):
        super().display(screen)
        if self.velocity == Vector(0,0):
            pygame.draw.circle(screen, c.red, (self.cue_pos.x, self.cue_pos.y), 5)

    def move_cue(self, angle):
        distance = self.cue_pos - self.center
        rotated = distance.rotation(angle)
        self.cue_pos = self.center + rotated

    def shoot (self, speed):
        direction = (self.center - self.cue_pos).normalize()
        self.velocity = direction * speed

    def update_position(self,dt):
        super().update_position(dt)
        if self.velocity != Vector(0,0):
            self.cue_pos = Vector(self.center.x , self.center.y + self.radius)

        


