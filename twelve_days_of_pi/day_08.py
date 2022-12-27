import onewire, ds18x20, time
from machine import Pin

sensor_pin = Pin(26, Pin.IN)
sensor = ds18x20.DS18X20(onewire.OneWire(sensor_pin))

roms = sensor.scan()
print(f'{len(roms)} ROMs to process')

while True:
    sensor.convert_temp()
    time.sleep(1.5)
    
    for rom in roms:
        print(f'Temperature: {sensor.read_temp(rom)} °C')
        time.sleep(5)
