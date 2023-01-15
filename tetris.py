from microbit import *
import time

# Lists
collision_blocks = []

# Integers
row = 0
column = 2
coordinates = int(str(row) + str(column))
down_speed = 750

# Blocks
normal_block = display.set_pixel(column, row, 9)
half_box_block = display.set_pixel(column, row, 9), display.set_pixel(column + 1, row, 9), display.set_pixel(column, row - 1, 9)

# Startup
display.set_pixel(column, row, 9)

while True:
    if button_a.is_pressed():
        display.set_pixel(column, row, 0)
        if coordinates - 10 not in collision_blocks:
            column -= 1
        display.set_pixel(column, row, 9)

    if button_b.is_pressed():
        display.set_pixel(column, row, 0)
        if coordinates + 10 not in collision_blocks:
            column += 1
        display.set_pixel(column, row, 9)

    time.sleep_ms(down_speed)

    if row < 4 and coordinates + 1 not in collision_blocks:
        display.set_pixel(column, row, 0)
        row += 1
        display.set_pixel(column, row, 9)

    if row == 4 or coordinates + 1 in collision_blocks:
        collision_blocks.append(coordinates)
        row = 0
        column = 2
        display.set_pixel(column, row, 9)