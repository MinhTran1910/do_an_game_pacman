from pygame.math import Vector2 as vec 
import pygame
from setting import *
class Player:
    def __init__(self, app , pos):
        self.app = app
        self.grid_pos = pos
        self.pix_pos = self.get_pix_pos()
        self.direction = vec(1,0)
    
    def update(self):
        self.pix_pos += self.direction
        self.grid_pos[0] +=(self.pix_pos[0])//self.app.cell_width
    def draw(self):
        pygame.draw.circle(self.app.screen, PLAYER_COLOUR, (int(self.pix_pos.x), int(self.pix_pos.y)),
        self.app.cell_width//2)

    def move(self, direction):
        self.direction = direction 
    def get_pix_pos(self):
        return  vec(((self.grid_pos.x*self.app.cell_width)+ self.app.cell_width//2),
        (self.grid_pos.y*self.app.cell_height) + self.app.cell_height//2)