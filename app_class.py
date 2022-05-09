import pygame, sys
from setting import *
from player_class import *
pygame.init()
vec = pygame.math.Vector2


class App:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH , HEIGHT))
        self.clock = pygame.time.Clock()
        self.running  = True
        self.state = 'playing'
        self.cell_width = WIDTH//28
        self.cell_height = HEIGHT//31

        self.player = Player(self, PLAYER_START_POS)
        self.load()
    def run(self):
        while self.running:
            if self. state == 'start':
                self.start_events()
                self.start_update()
                self.start_draw()
            
            elif self.state == 'playing':
                self.playing_events()
                self.playing_update()
                self.playing_draw()
            self.clock.tick(FPS)
        pygame.quit()
        sys.exit()
    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    def start_update(self):
        pass
    def start_draw(self):
        pygame.display.update()

    

############################ Load display################
    def load(self):
        self.background = pygame.image.load('background.png')
        self.background = pygame.transform.scale(self.background, (WIDTH,HEIGHT))

    def draw_grid(self):
        for x in range(WIDTH//self.cell_width):
            pygame.draw.line(self.screen, GREY, (x*self.cell_width,0), (x*self.cell_width,HEIGHT))
        for x in range(HEIGHT//self.cell_height):
            pygame.draw.line(self.screen, GREY, (0,x*self.cell_width), (WIDTH,x*self.cell_height))
############################# playing #############################
    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.move(vec(-1,0))
                if event.key == pygame.K_RIGHT:
                    self.player.move(vec(1,0))
                if event.key == pygame.K_UP:
                    self.player.move(vec(0,-1))
                if event.key == pygame.K_DOWN:
                    self.player.move(vec(0,1))

    
    def playing_update(self):
        self.player.update()
    def playing_draw(self):
        self.screen.blit(self.background,(0,0))
        self.draw_grid()

        self.player.draw()
        pygame.display.update()
    
 

