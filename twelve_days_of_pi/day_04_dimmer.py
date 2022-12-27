from machine import ADC, Pin, PWM
import time

potentiometer = ADC(Pin(27))

red = PWM(Pin(18))
amber = PWM(Pin(19))
green = PWM(Pin(20))
all_leds = [red, amber, green]
for led in all_leds:
    led.freq(1000)


reading = 0
while True:
    reading = potentiometer.read_u16()
    reading = 0 if reading < 1000 else reading
    print(reading)
    
    for led in all_leds:
        led.duty_u16(reading)
        
    time.sleep(0.0001)
