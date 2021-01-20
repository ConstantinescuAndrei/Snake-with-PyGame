import pygame
import time
import random
import snake
import food
pygame.init()

white=(255, 255, 255)
black=(0, 0, 0)
yellow=(255, 255, 102)
red=(213, 50, 80)
green=(0, 255, 0)
blue=(50, 153, 213)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake game")

snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def your_score(score):
    value = score_font.render("Your score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0  

    snake_list = []
    length_of_snake = 1 

    foodx, foody = food.positionOfFood(dis_width, dis_height, snake_block)

    while not game_over:

        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.key == pygame.K_q:
                    game_over = True
                    game_close = False
                if event.key == pygame.K_c:
                    gameLoop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over=True
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        
        if snake.check_boundaries(x1, y1, dis_width, dis_height):
             game_close = True
        
        x1 = x1 + x1_change
        y1 = y1 + y1_change
        dis.fill(blue)
        
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        
        snake_head = []
        snake.grow_snake(snake_list, snake_head, length_of_snake, x1, y1)

        if snake.check_collide(snake_list, snake_head): 
            game_close=True

        snake.move_snake(snake_block, snake_list, black, dis)
        your_score(length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = food.positionOfFood(dis_width, dis_height, snake_block)
            length_of_snake = length_of_snake + 1
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()
    
gameLoop()