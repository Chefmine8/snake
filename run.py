#import les librairies nécessaire.
import pygame
import random
import time
from datetime import datetime
from object import object
from golden_ball import golden
from snack import snack
from snake import snake

class Game:
    def __init__(self, screen):
        #déclaration de toute les variables.
        self.screen = screen
        self.pause = False
        self.running = True
        self.snake = snake(0, 0)
        self.object = object(0, 0)
        self.golden = golden(0, 0)
        self.snack = snack(0, 0)
        datetime.now()
        self.time_second = float(datetime.now().strftime('%S'))
        self.time_second_new = float(datetime.now().strftime('%S'))
        self.s1 = 0
        self.time_min_print = 0
        self.time_heure_print = 0
        self.snake.position_tete_x = []
        self.snake.position_tete_y = []
        self.move = 0
        self.area = pygame.Rect(0, 0, 1280, 720)
        self.object.x = random.randrange(30, 1240, 30)
        self.object.y = random.randrange(30, 680, 30)
        self.snack.x = random.randrange(30, 1240, 30)
        self.snack.y = random.randrange(30, 680, 30)
        self.score = 0
        self.serpent_corp = 30
        self.compteur_3 = 0
        self.start = 1
        self.yep = 0
        self.f = open('./option.txt', "r")
        self.best = int(self.f.read())
        self.f.close()
        self.score_2 = 0


    def handling_events(self):
        #Gere le déplacement et gere la pause.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(self.time_s, self.time_m, self.time_h)
                self.running = False
        keys= pygame.key.get_pressed()

        if keys[pygame.K_BACKSPACE]:
            
            print(self.time_s, self.time_m, self.time_h)
            self.running = False


        if self.move != 2:
            if keys[pygame.K_LEFT]:
                self.move = 1
                self.yep = 0

        if self.move != 1:
            if keys[pygame.K_RIGHT]:
                self.move = 2
                self.yep = 0

        if self.move != 4:
            if keys[pygame.K_UP]:
                self.move = 3
                self.yep = 0

        if self.move != 3:
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
                    if event.type == pygame.QUIT:
                        self.sleep = False
                        self.running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            self.pause = False
                            self.move = 0
                            self.yep = 1
                            self.running = True
                self.screen.fill((0,0,0))

                pygame.display.flip()


        if self.move == 1 :
            self.snake.angle = pygame.transform.rotate(self.snake.image, 180)
            self.snake.x -= self.snake.distance
            time.sleep(self.snake.speed)
        if self.move == 2:
            self.snake.angle = pygame.transform.rotate(self.snake.image, 0)
            self.snake.x += self.snake.distance
            time.sleep(self.snake.speed)
        if self.move == 3:
            self.snake.angle = pygame.transform.rotate(self.snake.image, 90)
            self.snake.y -= self.snake.distance
            time.sleep(self.snake.speed)
        if self.move == 4:
            self.snake.angle = pygame.transform.rotate(self.snake.image, 270)
            self.snake.y += self.snake.distance
            time.sleep(self.snake.speed)


    def update(self, difficulty):
        #Recupere les coordoné de la pomme.
        self.x_o = self.object.x
        self.y_o = self.object.y
        
        #Permet de géré le chrono.
        self.time_second = float(datetime.now().strftime('%S'))
        if self.time_second == 0:
            self.time_second_new = float(datetime.now().strftime('%S'))

        if self.time_second > self.time_second_new:
            self.s1 += 1
            self.time_second_new = float(datetime.now().strftime('%S'))

        if self.s1 == 60:
            self.time_min_print += 1
            self.s1 = 0

        if self.time_min_print == 60:
            self.time_min_print = 0
            self.time_heure_print += 1

        self.time_s = str(self.s1)
        self.time_m = str(self.time_min_print)
        self.time_h = str(self.time_heure_print)

        if not self.snake.position_tete_x:
            print()
        else:
            self.snake.position_tete_x.pop(0)
            self.snake.position_tete_y.pop(0)

        self.compteur_2 = 0
        self.compteur_4 = self.compteur_3 - 1
        if self.yep == 0:
            while self.compteur_3 >= 1 and self.compteur_2 <= self.compteur_4:
                if self.snake.y == self.snake.position_tete_y[self.compteur_2] and self.snake.x == self.snake.position_tete_x[self.compteur_2]:
                    self.__init__(screen)
                    print(self.time_h, self.time_m, self.time_s)
                self.compteur_2 += 1

        self.snake.position_tete_x.append(self.snake.x)
        self.snake.position_tete_y.append(self.snake.y)

        if self.start == 2 or self.start == 1:
            self.start += 1
            self.compteur_3 += 1
            self.snake.position_tete_x.append(self.snake.x)
            self.snake.position_tete_y.append(self.snake.y)
            self.move = 2

        #Permet de manger la 1er pomme.
        if self.object.y == self.snake.y and self.object.x == self.snake.x:
            pygame.mixer.music.load('./sound/eat.mp3')
            pygame.mixer.music.play()
            self.score += 1
            print(self.score, self.snake.speed)
            self.compteur_3 += 1
            self.object.x = random.randrange(30, 1240, 30)

            if self.x_o == self.object.x:
                self.object.x = random.randrange(30, 1240, 30)

            self.object.y = random.randrange(30, 680, 30)

            if self.y_o == self.object.y:
                self.object.y = random.randrange(30, 680, 30)

            self.snake.position_tete_x.append(self.snake.x)
            self.snake.position_tete_y.append(self.snake.y)
            self.start = 0
            if self.best < self.score:
                self.f = open('./option.txt', "w")
                self.f.write(str(self.score))
                self.f.close()

            if self.score_2 < self.score:
                if self.score < 5:
                    self.snake.speed = self.snake.speed - 0.01
                    self.score_2 += 1
                elif self.score < 12:
                    self.snake.speed = self.snake.speed - 0.002
                    self.score_2 += 1
                else:
                    return 'nop'

        #Permet de manger la 2e pomme.
        if self.snack.y == self.snake.y and self.snack.x == self.snake.x:
            pygame.mixer.music.load('./sound/eat.mp3')
            pygame.mixer.music.play()
            self.score += 1
            print(self.score, self.snake.speed)
            self.compteur_3 += 1
            self.snack.x = random.randrange(30, 1240, 30)

            if self.x_o == self.snack.x:
                self.snake.x = random.randrange(30, 1240, 30)

            self.snack.y = random.randrange(30, 680, 30)

            if self.y_o == self.snack.y:
                self.snack.y = random.randrange(30, 680, 30)

            self.snake.position_tete_x.append(self.snake.x)
            self.snake.position_tete_y.append(self.snake.y)
            self.start = 0
            if self.best < self.score:
                self.f = open('./option.txt', "w")
                self.f.write(str(self.score))
                self.f.close()

            if self.score_2 < self.score:
                if self.score < 5:
                    self.snake.speed = self.snake.speed - 0.01
                    self.score_2 += 1
                elif self.score < 12:
                    self.snake.speed = self.snake.speed - 0.002
                    self.score_2 += 1
                else:
                    return 'nop'
                
        #Permet de manger la pomme doré, cela est possible uniquement en mode hard. 
        if difficulty == "hard" and self.golden.y == self.snake.y and self.golden.x == self.snake.x:
            pygame.mixer.music.load('./sound/eat.mp3')
            pygame.mixer.music.play()
            self.score += 1
            print(self.score, self.snake.speed)
            self.compteur_3 += 10
            for i in range(10):
                self.snake.position_tete_x.append(self.snake.x)
                self.snake.position_tete_y.append(self.snake.y)

            self.start = 0
            if self.best < self.score:
                self.f = open('./option.txt', "w")
                self.f.write(str(self.score))
                self.f.close()

            for i in range(9):
                if self.score_2 < self.score:
                    if self.score < 5:
                        self.snake.speed = self.snake.speed - 0.01
                        self.score_2 += 1
                        self.score += 1
                    elif self.score < 12:
                        self.snake.speed = self.snake.speed - 0.002
                        self.score_2 += 1
                        self.score += 1
                    else:
                        self.score+=1

        if self.snake.x > 1280 or self.snake.x < -10 or self.snake.y > 710 or self.snake.y < -10:
            print(self.time_h, self.time_m, self.time_s)
            self.__init__(screen)

    #Permet de tout afficher.
    def display(self, difficuly):
        self.screen.fill("#065306")
        self.object.draw(self.screen)
        if difficulty == "hard":
            self.golden.draw(self.screen) #Affiche la pomme doré uniquement si 
        self.snack.draw(self.screen)
        self.compteur_2 = 0
        while self.compteur_2 != self.compteur_3:
            self.snake.position_x = self.snake.position_tete_x[self.compteur_2]
            self.snake.position_y = self.snake.position_tete_y[self.compteur_2]
            pygame.draw.rect(self.screen, (0, 255, 0), (self.snake.position_x, self.snake.position_y, self.serpent_corp, self.serpent_corp))
            self.compteur_2 = self.compteur_2 + 1
        self.snake.draw(self.screen)
        pygame.draw.rect(self.screen, (255,255,255), (0, 0, 1280, 720),3)
        self.create_message('big', 'Score :{}'.format(str(self.score)), (10, 10, 100, 50), (0,0,0))
        self.create_message('big', 'Best score :{}'.format(str(self.best)), (10, 50, 100, 50), (0, 0, 0))
        self.create_message('big', 'Time :{}'.format(str(self.time_h)), (520, 10, 50, 500), (0,0,0))
        self.create_message('big', '{}'.format(str(self.time_m)), (670, 10, 50, 500), (0, 0, 0))
        self.create_message('big', '{}'.format(str(self.time_s)), (720, 10, 50, 500), (0, 0, 0))
        pygame.display.flip()
    
    #Permet de gerer l'affichage des textes.
    def create_message(self, font, message, message_rectangle, color):
        if font == "small":
            font = pygame.font.SysFont('Lato', 20, False)

        if font == "moyen":
            font = pygame.font.SysFont('Lato', 30, False)

        if font == "big":
            font = pygame.font.SysFont('Lato', 40, True)

        self.message = font.render(message, True, color)

        self.screen.blit(self.message, message_rectangle)

    #Execute tout ce qui est nessaicere au bon démarage.
    def run(self):
        while self.running:
            self.handling_events()
            self.update(difficulty)
            self.display(difficulty)

difficulty = input("hard or easy ? ") #Sélectionne entre difficile et facile.

#Créé la fenetre
pygame.init()
screen = pygame.display.set_mode((1280, 720)) #
pygame.display.set_caption('Snake') #Attribue un nom à la fenetre
game = Game(screen)
game.run()

pygame.quit()
