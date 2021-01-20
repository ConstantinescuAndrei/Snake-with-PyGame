import pygame
import map_colision

white = (255, 255, 255)



def first_map(dis_width, dis_height, dis, snake_block):

    #Top-Left corner wall
    vertical_line(dis, 100, 100, 200, snake_block)
    horizontal_line(dis, 100, 100, 200, snake_block)

    #Bottom-Left corner wall
    vertical_line(dis, 100, 400, 500, snake_block)
    horizontal_line(dis, 100, 500, 200, snake_block)

    #Top-Right corner wall
    vertical_line(dis, 700, 100, 200, snake_block)
    horizontal_line(dis, 700, 100, 600, snake_block)

    #Bottom-Right corner wall
    vertical_line(dis, 700, 400, 500, snake_block)
    horizontal_line(dis, 700, 500, 600, snake_block)

def vertical_line(dis, x_coordinate, y_coordinate, max_y_coordinate, snake_block):
    for i in range(y_coordinate, max_y_coordinate, snake_block):
        pygame.draw.rect(dis, (113, 75, 205), [x_coordinate, i, snake_block, snake_block])

def horizontal_line(dis, x_coordinate, y_coordinate, max_x_coordinate, snake_block):
    if x_coordinate < max_x_coordinate:
        for i in range(x_coordinate, max_x_coordinate, snake_block):
            pygame.draw.rect(dis, (113, 75, 205), [i, y_coordinate, snake_block, snake_block])
    else:
        for i in range(max_x_coordinate, x_coordinate, snake_block):
            pygame.draw.rect(dis, (113, 75, 205), [i, y_coordinate, snake_block, snake_block])

def check_snake_collision(level, snake_head):
    x = snake_head[0]
    y = snake_head[1]
    return map_colision.find_level(level, x, y)
