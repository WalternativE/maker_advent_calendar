import time
from machine import Pin, ADC
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)
potentiometer = ADC(Pin(26))
button = Pin(15, Pin.IN, Pin.PULL_DOWN)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
pink = (255, 20, 147)
gb_violet = (35, 2, 46)
colors = [
    red, green, blue,
    yellow, pink, gb_violet,
]

max_delay = 2.0
color_change_index = 0


def clamp_running_index():
    if color_change_index > len(colors) - 1:
        return 0
    else:
        return color_change_index


def read_scaled_delay():
    delay_perc = potentiometer.read_u16() / 65535
    clipped_delay_perc = 0.01 if delay_perc < 0.01 else delay_perc
    
    return clipped_delay_perc * max_delay


while True:
    color = colors[color_change_index]
    for i in range(15):
        strip[i] = color
        
        delay = read_scaled_delay()
        time.sleep(delay)
        strip.write()
        
        if button() == 1:
            print('button pressed')
            color_change_index += 1
            color_change_index = clamp_running_index()
            color = colors[color_change_index]
        
    color_change_index += 1
    color_change_index = clamp_running_index()
