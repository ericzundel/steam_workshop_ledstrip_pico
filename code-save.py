# Modified for LED Workshop STEAM Workshop day 2023 at Charles R. Drew Charter School
#
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
# SPDX-License-Identifier: MIT

"""Programming a Neopixel strip using CircuitPython"""
import time
import board
from rainbowio import colorwheel
import neopixel

pixel_pin = board.GP2
num_pixels = 10

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=.2, auto_write=False)

def color_chase(color, wait):
    for i in range(num_pixels):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while True:


    print("RED")
    pixels.fill(RED)
    pixels.show()
    # Increase or decrease to change the speed of the solid color change.
    time.sleep(1)
    print("GREEN")
    pixels.fill(GREEN)
    pixels.show()
    time.sleep(1)
    print("BLUE")
    pixels.fill(BLUE)
    pixels.show()
    time.sleep(1)

    print("Color Chase")
    color_chase(RED, 0.1)  # Increase the number to slow down the color chase
    color_chase(YELLOW, 0.1)
    color_chase(GREEN, 0.1)
    color_chase(CYAN, 0.1)
    color_chase(BLUE, 0.1)
    color_chase(PURPLE, 0.1)

    print("Rainbow Cycle")
    rainbow_cycle(.02)  # Increase the number to slow down the rainbow
