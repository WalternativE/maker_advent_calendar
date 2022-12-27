from machine import Pin, PWM
import time, sys

# application states
state_beam_unbroken = 0
state_beam_broken = 1

# musical notes
a_5 = 880
a_6 = 1760

beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)
all_leds = [red, amber, green]

buzzer = PWM(Pin(13))


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
    

def play_note(note, duration=0.5, duty=1000):
    buzzer.freq(note)
    buzzer.duty_u16(duty)
    time.sleep(duration)
    buzzer.duty_u16(0)


def start_sequence():
    play_note(a_5, duration=0.5)
    time.sleep(0.5)
    play_note(a_5, duration=0.5)
    time.sleep(0.5)
    play_note(a_5)
    time.sleep(0.5)
    play_note(a_6)


print('Ready!')
start_sequence()
print('Go!')

start = time.time()
state = state_beam_unbroken
counter = 0
goal = 230
goal_perc = 0

seconds_elapsed = 0
while seconds_elapsed < 31:
    time.sleep(0.001)
    
    goal_perc = counter / goal
    if goal_perc < 1/3:
        set_all(all_leds, 0)
    elif goal_perc < 2/3:
        set_all([red], 1)
        set_all([amber, green], 0)
    elif goal_perc < 1:
        set_all([red, amber], 1)
        set_all([green], 0)
    else:
        set_all(all_leds, 1)
    
    if state == state_beam_unbroken:
        if beam.value() == 0:
            print('Beam broken')
            state = state_beam_broken
            counter += 1
    elif state == state_beam_broken:
        if beam.value() == 1:
            print('Beam unbroken')
            state = state_beam_unbroken
            
    seconds_elapsed = time.time() - start
    
print(f'Finished with {counter} taps.')
for _ in range(5):
    blink(all_leds)
