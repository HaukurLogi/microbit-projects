from microbit import *
from random import randint

# Lists
collision_blocks = []

# Integers
row = 0
column = 2
random_block = randint(1, 3)
coordinates = 0
down_speed = 750


# Blocks
def blocks(light_level):
    global row, column, random_block

    # Arrow block
    if random_block == 1:
        display.set_pixel(column, row, light_level)
        display.set_pixel((column + 1), row, light_level)
        if row > 0:
            display.set_pixel(column, (row - 1), light_level)
    # Cube
    elif random_block == 2:
        display.set_pixel(column, row, light_level)
    # Long block
    else: 
        if row > 0:
            display.set_pixel(column, (row - 1), light_level)
        display.set_pixel(column, row, light_level)
        display.set_pixel(column, (row + 1), light_level)

# Startup
blocks(9)

while True:
    if button_a.is_pressed():
        blocks(0)
        if coordinates - 10 not in collision_blocks:
            column -= 1
        blocks(9)

    if button_b.is_pressed():
        blocks(0)
        if coordinates + 10 not in collision_blocks:
            column += 1
        blocks(9)

    sleep(down_speed)

    if row < 4 and coordinates + 1 not in collision_blocks:
        blocks(0)
        row += 1
        blocks(9)

    if row == 5 or coordinates + 1 in collision_blocks:
        collision_blocks.append(coordinates)
        row = 0
        column = 2
        random_block = randint(1, 3)
        blocks(9)