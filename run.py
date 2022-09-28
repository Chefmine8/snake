import pygame
import random
import time
from object import object
from snake import snake

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.pause = False
        self.running = True
        self.snake = snake(0, 0)
        self.object = object(0, 0)
        self.move = 0
        self.area = pygame.Rect(0, 0, 1280, 720)
        self.object.x = random.randrange(30, 1240, 30)
        self.object.y = random.randrange(30, 680, 30)
        self.score = 0
        self.serpent_corp = 30
        self.snake.position_tete_x.append(1)
        self.snake.position_tete_y.append(1)
        self.compteur_3 = 0
        self.yep = 0

    def handling_events(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
        keys= pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.move = 1
            self.yep = 0
        if keys[pygame.K_RIGHT]:
            self.move = 2
            self.yep = 0
        if keys[pygame.K_UP]:
            self.move = 3
            self.yep = 0
        if keys[pygame.K_DOWN]:
            self.move = 4
            self.yep = 0
        if keys[pygame.K_SPACE]:
            self.move = 5

        if self.move == 5 :
            time.sleep(self.snake.speed)
            self.pause = True
            while self.pause == True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.pause = False
                            self.move = 0
                            self.yep = 1
                            self.running = True
                self.screen.fill((0,0,0))

                pygame.display.flip()

        if self.move == 1 :
            self.snake.x -= self.snake.distance
            time.sleep(self.snake.speed)
        if self.move == 2:
            self.snake.x += self.snake.distance
            time.sleep(self.snake.speed)
        if self.move == 3:
            self.snake.y -= self.snake.distance
            time.sleep(self.snake.speed)
        if self.move == 4:
            self.snake.y += self.snake.distance
            time.sleep(self.snake.speed)

        if self.score >= 5:
            self.snake.speed = 0.04

        if self.score >= 30:
            self.snake.speed = 0.02



    def update(self):
        self.snake.position_tete_x.pop(0)
        self.snake.position_tete_y.pop(0)
        self.compteur_2 = 0
        self.compteur_4 = self.compteur_3 - 1
        if self.yep == 0:
            while self.compteur_3 >= 1 and self.compteur_2 <= self.compteur_4:
                if self.snake.y == self.snake.position_tete_y[self.compteur_2] and self.snake.x == self.snake.position_tete_x[self.compteur_2]:
                    self.running = False
                self.compteur_2 += 1

        self.snake.position_tete_x.append(self.snake.x)
        self.snake.position_tete_y.append(self.snake.y)

        if self.object.y == self.snake.y and self.object.x == self.snake.x:
            pygame.mixer.music.load('./sound/touch.mp3')
            pygame.mixer.music.play()
            self.score += 1
            self.compteur_3 += 1
            self.object.x = random.randrange(30, 1240, 30)
            self.object.y = random.randrange(30, 680, 30)
            self.snake.position_tete_x.append(self.snake.x)
            self.snake.position_tete_y.append(self.snake.y)

        if self.snake.x > 1280 or self.snake.x < 0 or self.snake.y > 720 or self.snake.y < 0:
            self.running = False

    def display(self):
        self.screen.fill("#065306")
        self.object.draw(self.screen)
        self.compteur_2 = 0
        while self.compteur_2 != self.compteur_3:
            pygame.draw.rect(self.screen, (0,255,0), (self.snake.position_tete_x[self.compteur_2], self.snake.position_tete_y[self.compteur_2], self.serpent_corp, self.serpent_corp))
            self.compteur_2 = self.compteur_2 + 1
        self.snake.draw(self.screen)
        pygame.draw.rect(self.screen, (255,255,255), (0, 0, 1280, 720),3)
        self.create_message('big', '{}'.format(str(self.score)), (10, 10, 100, 50), (0,0,0))
        pygame.display.flip()

    def create_message(self, font, message, message_rectangle, color):
        if font == "small":
            font = pygame.font.SysFont('Lato', 20, False)

        if font == "moyen":
            font = pygame.font.SysFont('Lato', 30, False)

        if font == "big":
            font = pygame.font.SysFont('Lato', 40, True)

        self.message = font.render(message, True, color)

        self.screen.blit(self.message, message_rectangle)

    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            #self.create_message()

pygame.init()
screen = pygame.display.set_mode((1280, 720))
game = Game(screen)
game.run()

pygame.quit()