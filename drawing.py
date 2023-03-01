from microbit import *

walls = [-1, -11, -12, -13, -14, -15, 15, 25, 35, 45, 55, 60, 61, 62, 63, 64, 65]

delay = 1000
column = 2
row = 0

horizontal_direction = accelerometer.get_x()
vertical_direction = accelerometer.get_y()


while True:

    coordinates = int(str(column) + str(row))
    display.set_pixel(column, row, 9)

    if horizontal_direction < 200 and coordinates + 10 not in walls:
        sleep(delay)
        column -= 1

    if horizontal_direction > 200 and coordinates - 10 not in walls:
        sleep(delay)
        column += 1

