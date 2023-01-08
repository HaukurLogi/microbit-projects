from microbit import *
import time

collision_blocks = [0]
collision_blocks = []
row = 0
column = 2
down_speed = 1
display.set_pixel(column, row, 9)

def on_button_pressed_a():
    global column
    display.set_pixel(column, row, 0)
    if coordinates - 10 not in collision_blocks:
        column -= 1
    display.set_pixel(column, row, 9)
button_a(on_button_pressed_a)

def on_button_pressed_b():
    global column
    display.set_pixel(column, row, 0)
    if coordinates + 10 not in collision_blocks:
        column += 1
    display.set_pixel(column, row, 9)
button_b(on_button_pressed_b)

while True:
    coordinates = int(str(column) + str(row))
    time.sleep(1)
    if row < 4 and coordinates + 1 not in collision_blocks:
            display.set_pixel(column, row, 0)
    row += 1
    display.set_pixel(column, row, 9)

    if row == 5 or coordinates + 1 in collision_blocks:
        collision_blocks[len(collision_blocks)] = coordinates
        print(collision_blocks)
        row = 0
        column = 2
        display.set_pixel(column, row, 9)