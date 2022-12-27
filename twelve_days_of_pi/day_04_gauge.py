from machine import ADC, Pin
import time

potentiometer = ADC(Pin(27))

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


knob_percentage = 0
while True:
    knob_percentage = potentiometer.read_u16() / 65000
    if knob_percentage < 0.1:
        set_all(all_leds, 0)
    elif knob_percentage < 0.34:
        set_all([red], 1)
        set_all([amber, green], 0)
    elif knob_percentage < 0.67:
        set_all([red, amber], 1)
        set_all([green], 0)
    elif knob_percentage < 0.99:
        set_all(all_leds, 1)
    else:
        blink(all_leds)
