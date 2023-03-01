from microbit import *
import time

# Lists
collision_blocks = []

# Integers
row = 0
column = 2
wait_speed = 750

# Functions
def summon(light_level):
    display.set_pixel(column, row, light_level)

# Startup
display.set_pixel(column, row, 9)

while True:
    coordinates = int(str(column) + str(row))

    if button_a.is_pressed():
        summon(0)
        if coordinates - 10 not in collision_blocks:
            column -= 1
        summon(9)

    if button_b.is_pressed():
        summon(0)
        if coordinates + 10 not in collision_blocks:
            column += 1
        summon(9)

    sleep(wait_speed)
    
    if row < 4 and coordinates + 1 not in collision_blocks:
        summon(0)
        row += 1
        summon(9)
    else:
        collision_blocks.append(coordinates)
        row = 0
        column = 2
        summon(9)