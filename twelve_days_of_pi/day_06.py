from machine import ADC, Pin
import time

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)
all_leds = [red, amber, green]

light_sensor = ADC(Pin(26))


def set_all(leds_to_set, to_set, delay=None, reverse_order=False):
    if reverse_order:
        leds_to_set = reversed(leds_to_set)

    for led in leds_to_set:
        led.value(to_set)
        if delay:
            time.sleep(delay)


while True:
    light = light_sensor.read_u16()
    light_percent = round(light/65535*100, 2)

    print(f"{light_percent}%")
    
    time.sleep(0.5)
    
    if light_percent < 10:
        set_all(all_leds, 0)
    elif light_percent < 30:
        set_all([red], 1)
        set_all([amber, green], 0)
    elif light_percent < 60:
        set_all([red, amber], 1)
        set_all([green], 0)
    else:
        set_all(all_leds, 1)
