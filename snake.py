import time
import sys
import pygame
from pygame.locals import *
import random

pygame.init()
RED = (213, 50, 80)
White=(255,255,255)
BackGreen= (0, 255, 0)
GREEN = (23, 87, 50)
BLACK = (0, 0, 0)
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
block_size = 10
snake_speed = 15
font = pygame.font.SysFont("bahnschrift", 25)

def Your_score(score):
    value = font.render("Ton score est : " + str(score), True, BLACK)
    win.blit(pygame.image.load("menu.png").convert(), (155, 155))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_KP0:
                sys.exit()
            if event.key == K_KP1:
                gameLoop()

def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, GREEN, [x[0], x[1], block_size, block_size])

def gameLoop():
    game_over = False
    game_close = False
    x1, y1 = WIDTH / 2, HEIGHT / 2
    x1_change, y1_change = 0, 0
    snake_List = []
    Longueur_du_snake = 1
    pommex, pommey = round(random.randrange(0, WIDTH - block_size) / 10.0) * 10.0, round(random.randrange(0, HEIGHT - block_size) / 10.0) * 10.0
    while game_over == False:
        while game_close == True:
            win.fill(White)
            Your_score(Longueur_du_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        win.fill(BackGreen)
        pygame.draw.rect(win, RED, [pommex, pommey, block_size, block_size])
        snake_tete = []
        snake_tete.append(x1)
        snake_tete.append(y1)
        snake_List.append(snake_tete)
        if len(snake_List) > Longueur_du_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_tete:
                game_close = True
        our_snake(block_size, snake_List)
        pygame.display.update()
        if x1 == pommex and y1 == pommey:
            pommex, pommey = round(random.randrange(0, WIDTH - block_size) / 10.0) * 10.0, round(random.randrange(0, HEIGHT - block_size) / 10.0) * 10.0
            Longueur_du_snake += 1
        pygame.time.Clock().tick(snake_speed)
    pygame.quit()
    quit()

gameLoop()