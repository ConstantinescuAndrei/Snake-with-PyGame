import pygame
import random

def positionOfFood(dis_width, dis_height, snake_block):
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    return foodx, foody