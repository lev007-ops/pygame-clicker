import time
import pygame
from random import randint
from time import sleep
pygame.init()


class Button():
    SIZE_X = 60
    SIZE_Y = 130

    def __init__(self, window, xcor, ycor,  *args, size_x=60, size_y=130):
        self.xcor = xcor
        self.ycor = ycor
        self.color = args
        self.window = window
        self.SIZE_X = size_x
        self.SIZE_Y = size_y

        self.rect = pygame.Rect(xcor, ycor, self.SIZE_X, self.SIZE_Y)

    def draw_rect(self):
        pygame.draw.rect(self.window, (self.color), self.rect)

    def set_color(self, *args):
        self.color = args

    def is_collide(self, x, y):
        return self.rect.collidepoint(x, y)


class Game():

    font1 = pygame.font.Font(None, 40)

    def play():  # sourcery no-metrics
        window = pygame.display.set_mode((500, 500))

        # bg = pygame.image.load("amogus.png")
        clock = pygame.time.Clock()
        run = True

        # (255,215,0)

        area1 = Button(window, 50, 170, (218, 165, 32))
        area2 = Button(window, 160, 170, (218, 165, 32))
        area3 = Button(window, 270, 170, (218, 165, 32))
        area4 = Button(window, 390, 170, (218, 165, 32))
        font1 = pygame.font.Font(None, 40)
        exit_button = Button(
            window, 200, 400, (218, 165, 32), size_x=100, size_y=50)

        buttons = [area1, area2, area3, area4]
        q_clik = 0

        whait = 0

        check = 0
        whait_q = True
        start_time = time.time()
        while run:

            window.fill((255, 140, 0))
            # window.blit(bg, (0, 0))
            for button in buttons:
                button.draw_rect()

            # sleep(5)
            if whait == 0:

                q_clik = randint(0, 3)

                for button in buttons:
                    button.set_color((218, 165, 32))
                buttons[q_clik].set_color((255, 215, 0))
                whait = 12
                whait_q = True

                # sleep(0.2)
                # buttons[q_clik].set_color((218,165,32))

            exit_button.draw_rect()
            text = font1.render('Счёт:', True, (255, 255, 255))
            text2 = font1.render(str(check), True, (255, 255, 255))
            window.blit(text, (400, 15))
            window.blit(text2, (430, 45))
            if check == 5:
                window.fill((255, 140, 0))
                f = font1.render('Победа!!!', True, (255, 255, 255))
                window.blit(f, (130, 200))
                pygame.display.update()
                sleep(3)
                return True

            clock.tick(10)

            new_titme = int(time.time() - start_time)

            if new_titme == 15:
                window.fill((255, 140, 0))
                f = font1.render(
                    f'Ты проиграл со счётом {check}!', True, (255, 255, 255))
                window.blit(f, (130, 200))
                pygame.display.update()
                sleep(3)
                return True

            time_text = font1.render('Время:', True, (255, 255, 255))
            time_text2 = font1.render(str(new_titme), True, (255, 255, 255))
            window.blit(time_text, (50, 15))
            window.blit(time_text2, (85, 45))

            exit_text = font1.render('Выход', True, (255, 255, 255))
            window.blit(exit_text, (205, 410))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    run = False
                if e.type == pygame.MOUSEBUTTONDOWN:
                    x, y = e.pos

                    if buttons[q_clik].is_collide(x, y):
                        if whait_q:
                            buttons[q_clik].set_color((54, 191, 120))
                            check += 1
                            whait = 12
                            whait_q = False
                    elif exit_button.is_collide(x, y):
                        run = False

                    elif whait_q:
                        for i in buttons:
                            if i.is_collide(x, y):

                                check -= 1
                                whait = 12
                                i.set_color((191, 81, 54))
                                whait_q = False
            whait -= 1

            pygame.display.update()
