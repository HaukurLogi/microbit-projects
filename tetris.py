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
        if row > 1:
            display.set_pixel(column, (row - 2), light_level)
        display.set_pixel(column, row, light_level)
        display.set_pixel(column, (row - 1), light_level)    

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

    # Checks for any pixels that are turned on
    for pixels in range(25):
        if display.get_pixel(pixel_x, pixel_y) == 9:
            active_pixels.append(int(str(pixel_x) + str(pixel_y)))
            if pixel_x == 4:
                pixel_x = 0
                pixel_y += 1
            if pixel_x == 4 and pixel_y == 4:
                pixel_x = 0
                pixel_y = 0 

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