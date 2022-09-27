import pygame
import random

class snake:
    def __init__(self, x, y):
        self.image = pygame.image.load("./image/corpsnack.png")
        self.rect = self.image.get_rect(x=x, y=y)
        self.distance = 30
        self.speed = 0.09
        self.x = random.randrange(30, 1240, 30)
        self.y = random.randrange(30, 680, 30)
        self.position_tete_x = []
        self.position_tete_y = []

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
