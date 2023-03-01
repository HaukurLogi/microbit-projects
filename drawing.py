from microbit import *

walls = [0-1, 01, 02, 03,]

delay = 1000
column = 2
row = 0

horizontal_direction = accelerometer.get_x()
vertical_direction = accelerometer.get_y()


while True:
    sleep(delay)

    coordinates = int(str(column) + str(row))
    display.set_pixel(column, row)

    if horizontal_direction in range(-2, -1) and coordinates - 10 :
        column -= 1
