import pygame
from fast_clicker import Game, Button

pygame.init()
window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
run = True
font1 = pygame.font.Font(None, 30)
button = Button(window, 200, 200, (218, 165, 32), size_x=100, size_y=100)
while run:
    window.fill((255, 140, 0))
    text = font1.render('Играть', True, (255, 255, 255))
    button.draw_rect()
    window.blit(text, (220, 250))
    clock.tick(10)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            x, y = e.pos
            if button.is_collide(x, y):
                window.fill((255, 140, 0))
                pygame.display.update()
                if not Game.play():
                    run = False
    pygame.display.update()

