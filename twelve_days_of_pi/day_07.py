from machine import Pin, PWM
import time

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)
all_leds = [red, amber, green]

pir = Pin(26, Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(Pin(13))
buzzer.duty_u16(0)

def set_all(leds_to_set, to_set, delay=None, reverse_order=False):
    if reverse_order:
        leds_to_set = reversed(leds_to_set)

    for led in leds_to_set:
        led.value(to_set)
        if delay:
            time.sleep(delay)


def alarm(times=5):
    buzzer.duty_u16(10000)
    
    for _ in range(times):
        buzzer.freq(5000)
        set_all(all_leds, 1)
        time.sleep(1)
        
        buzzer.freq(500)
        set_all(all_leds, 0)
        time.sleep(1)
        
    buzzer.duty_u16(0)


print('Warming up...')
time.sleep(10)
print('Sensor active')

while True:
    time.sleep(0.01)
    if pir.value() == 1:
        print('I SEE YOU')
        alarm(times=2)
        
        print('Sensor active')
