from turtle import distance
import pygame
from pygame.locals import *
from settings import *
from line import Line
from math import sqrt, cos, sin
import numpy as np
from numpy.linalg import norm
from walls import WALL_DOWN, WALLS
from colors import *

class Laser(Line):
    def __init__(self, p1 = [WIDTH/2, HEIGHT/2], p2 = [WIDTH, HEIGHT*0.6], name = "laser", setDirectionBy = "mouse"):
        super().__init__(p1, p2, name)
        self.setDirectionBy = setDirectionBy
        
        self.crossPoints = []
        self.obsticle = False
        self.reflected = False
        self.intensity = 1
        self.color = RED
        
    
    def shoot(self):
        # If not reflected, set direction by mouse
        # Else the direction remains the same
        if (self.setDirectionBy=="mouse") and (not self.reflected):
            self.setDirectionByMouse()
        
        elif self.setDirectionBy=="angle":
            self.setDirectionByAngle(1)
            
        # The laser's length begins from at least the maximum length
        # it can reach. Not the best solution..
        shoot_length = sqrt(WIDTH**2 + HEIGHT**2)
        shoot_length *= 1.01 

        # set new end point of the laser
        new_endPoint = shoot_length*self.direction + np.array(self.p1)
        self.setEndpoint( list(new_endPoint) )
    
    def setDirectionByMouse(self) -> None:
        mouse_vec = np.array(pygame.mouse.get_pos())
        moused_rel_vec = mouse_vec - np.array(self.p1)
        mouse_rel_direction = moused_rel_vec/norm(moused_rel_vec) 
        self.direction = mouse_rel_direction

    def setDirectionByAngle(self, angle) -> None:
        new_endPoint = [self.p1[0] + cos(angle), self.p1[1] + sin(angle)]
        self.setEndpoint(new_endPoint)

    def findEndpoint(self):     
        self.shoot()        
        self.checkBorders()
    
    def updateIntensity(self, intensity):
        self.intensity = intensity
        # update alpha of the color
        self.color[3] *= self.intensity

class Spotlight(Line):
    pass


def test():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    laser = Laser()

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (pygame.key.get_pressed()[pygame.K_x]):
                pygame.quit()
                sys.exit()
        
        rel_mouse = pygame.mouse.get_rel()

        if (rel_mouse[0] != 0) and (rel_mouse[1] != 0):
            laser.findEndpoint()

        # Draw on screen
        screen.fill('black')
        pygame.draw.line(screen, 'red', laser.p1, laser.p2, 5)
        pygame.display.flip()
        clock.tick(FPS)


if __name__ == '__main__':
    import sys
    test()