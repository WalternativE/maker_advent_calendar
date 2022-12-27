from machine import Pin
import time

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)
all_leds = [red, amber, green]


def check_button_press(button, handler):
    if button.value() == 1:
        handler()
        
        return True
    return False


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
    
    
def toggle_leds(leds_to_toggle):
    for led in leds_to_toggle:
        led.toggle()


while True:
    time.sleep(0.15)
    
    if check_button_press(button1, lambda: print('Button 1 pressed')):
        #blink([green], blink_duration=1)
        green.toggle()
    elif check_button_press(button2, lambda: print('Button 2 pressed')):
        #blink([amber], blink_duration=1)
        amber.toggle()
    elif check_button_press(button3, lambda: print('Button 3 pressed')):
        #blink([red], blink_duration=1)
        red.toggle()
