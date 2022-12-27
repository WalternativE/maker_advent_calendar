from machine import Pin, PWM
import time

tilt = Pin(26, Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(Pin(13))
buzzer.freq(1000)

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)
all_leds = [red, amber, green]


def set_all(leds_to_set, to_set, delay=None, reverse_order=False):
    if reverse_order:
        leds_to_set = reversed(leds_to_set)

    for led in leds_to_set:
        led.value(to_set)
        if delay:
            time.sleep(delay)


def blink(leds_to_blink, blink_duration=0.5, delay=None, alternate=False):
    set_all(leds_to_blink, 1, delay=delay)
    time.sleep(blink_duration)

    set_all(leds_to_blink, 0, delay=delay, reverse_order=alternate)
    time.sleep(blink_duration)


while True:
    time.sleep(0.01)
    
    if tilt.value() == 1:
        print('I tilted')
        
        blink(all_leds, blink_duration=0.1)
        
        
