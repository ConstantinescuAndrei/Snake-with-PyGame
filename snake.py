import pygame

def move_snake(snake_block, snake_list, color, dis):
    for x in snake_list:
        pygame.draw.rect(dis, color, [x[0], x[1], snake_block, snake_block])

def check_collide(snake_list, snake_head):
    for x in snake_list[:-1]:
        if x == snake_head:
            return True
    return False

def grow_snake(snake_list, snake_head, length_of_snake, x, y):
    snake_head.append(x)
    snake_head.append(y)
    snake_list.append(snake_head)

    if len(snake_list) > length_of_snake:
            del snake_list[0]

def check_boundaries(x, y, dis_width, dis_height):
    if x >= dis_width or x < 0 or y >= dis_height or y < 0:
        return True
    return False