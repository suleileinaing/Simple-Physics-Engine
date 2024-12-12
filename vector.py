import pygame
import sys
import constant as c
import math

#reference : Lecture Week 12 practice code 

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normalize (self):
        magnitude = math.sqrt(self.x**2 + self.y**2)
        if magnitude == 0:
            return Vector(0,0)
        return Vector(self.x/magnitude, self.y/ magnitude)
    
    def dot (self, other):
        return self.x * other.x + self.y * other.y
    
    def cross(self, other):
        return self.x * other.y - self.y * other.x
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x , self.y+ other.y)
        elif isinstance(other, tuple) or isinstance(other, list):
            return Vector(self.x + other[0], self.y + other[1])
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x + other, self.y + other)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Vector' and '{}'".format(type(other).__name__))
        
    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x , self.y - other.y)
        elif isinstance(other, tuple) or isinstance(other, list):
            return Vector(self.x - other[0], self.y - other[1])
        elif isinstance(other, int) or isinstance(other, float):
            return Vector(self.x - other, self.y - other)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Vector' and '{}'".format(type(other).__name__))
        
    def __mul__ (self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector' and '{}'".format(type(other).__name__))
    
    def __truediv__ (self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(self.x / other, self.y / other)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Vector' and '{}'".format(type(other).__name__))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other):
        return not self == other
    
    def distance_to (self, other): 
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def rotation (self, angle):
        sin = math.sin(angle)
        cos = math.cos(angle)

        return Vector (self.x * cos - self.y* sin , self.x * sin + self.y * cos)

        