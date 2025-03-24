from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.x = x 
        self.y = y
        self.radius = radius
    
    def draw(self, surface)
        pygame.draw.circle(surface, (225, 225, 225), (self.x, self.y), self.radius, 2)
        
    
