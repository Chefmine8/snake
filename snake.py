import pygame
import random

class snake:
    def __init__(self, x, y):
        self.image = pygame.image.load("./image/corpsnack.png")
        self.rect = self.image.get_rect(x=x, y=y)
        self.distance = 10
        self.speed = 0.04
        self.x = random.randrange(30, 1240, 10)
        self.y = random.randrange(30, 680, 10)
        self.position_tete_x = []
        self.position_tete_y = []

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
