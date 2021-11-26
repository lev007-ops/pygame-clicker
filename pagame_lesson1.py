import pygame
from random import choice
pygame.init()

window = pygame.display.set_mode((900, 900))



run = True
clock = pygame.time.Clock()
font1 = pygame.font.Font(None, 22)
sprite1 = pygame.Rect(450, 450, 200, 100)
sprite2 = pygame.Rect(450, 650, 200, 100)
qtext = 'Хочешь задать вопрос?'
atext = 'Ответ'

q = ['как дела?', 'что делаешь?', 'когда дедлайн?']
a = ['хорошо пока код работает', 'разбираюсь с закачиком', 'сегодня!!!!!!']

while run:
    window.fill((0, 255, 255))

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_q:
                qtext = choice(q)
            if e.key == pygame.K_a:
                atext = choice(a)

    clock.tick(10)

    pygame.draw.rect(window, (0, 0, 0), sprite1)
    pygame.draw.rect(window, (0, 0, 0), sprite2)
    qust = font1.render(qtext, True, (255, 255, 255))
    window.blit(qust, (460, 500))
    ans = font1.render(atext, True, (255, 255, 255))
    window.blit(ans, (460, 695))
    pygame.display.update()