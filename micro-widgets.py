from microbit import *
import music

module = 1
modules = 2

while True:
    # Inputs
    if button_a.is_pressed():
        if module >= 2:
            display.clear()
            module -= 1 
    if button_b.is_pressed():
        if module < modules:
            display.clear()
            module += 1

    # Temperature
    if module == 1:
        display.scroll(temperature())

    # Rick Roll
    if module == 2:
        display.show(Image.MUSIC_QUAVER)
        rickroll = ["C4:3", ":3", "D4:3", ":3", "G3:2", ":3", "D4:3", ":3", "E4:3", ":3", "G4:1", "F4:1", "E4:1", "C4:3", ":3", "D4:3", ":3", "G3:3"]
        music.play(rickroll)
        sleep(2000)
