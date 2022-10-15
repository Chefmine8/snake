import pygame
import random

class snake:
    def __init__(self, x, y):
        self.image = pygame.image.load("./image/corpsnack.png")
        self.angle = pygame.transform.rotate(self.image, 0)
        self.rect = self.image.get_rect(x=x, y=y)
        self.distance = 30
        self.speed_start = 0.09
        self.speed = self.speed_start
        self.x = random.randrange(30, 1240, 30)
        self.y = random.randrange(30, 680, 30)
        self.position_tete_x = []
        self.position_tete_y = []

    def draw(self, screen):
        screen.blit(self.angle, (self.x, self.y))
