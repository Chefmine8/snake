import pygame

class golden:
    def __init__(self, x, y):
        self.image = pygame.image.load("./image/goldapp.png")
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 1
        self.x = 0
        self.y = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
