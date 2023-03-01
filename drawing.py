from microbit import *
from random import randint

# Lists

collision_blocks = []
active_pixels = []

# Integers
row = 0
column = 2
pixel_x = 0
pixel_y = 0
random_block = randint(1, 3)
down_speed = 750


# Blocks
def blocks(light_level):
    global row, column, random_block, coordinates
    display.set_pixel(column, row, light_level)
    
# Startup
blocks(9)

while True:
    coordinates = int(str(row) + str(column))
    if button_a.was_pressed():
        blocks(0)
        if coordinates - 10 not in collision_blocks:
            column -= 1
        blocks(9)

    if button_b.was_pressed():
        blocks(0)
        if coordinates + 10 not in collision_blocks:
            column += 1
        blocks(9)

    sleep(down_speed) 

    if row < 4 and coordinates + 1 not in collision_blocks:
        blocks(0)
        row += 1 
        blocks(9)
    if row >= 4 or coordinates + 1 in collision_blocks:
        collision_blocks.append(active_pixels)
        row = 0
        column = 2
        random_block = randint(1, 3)
        blocks(9)