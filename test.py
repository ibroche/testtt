from machine import Pin
import time
led = Pin(25, Pin.OUT) #Built-in LED Pico
#led = Pin("LED", Pin.OUT) #Built-in LED Pico W
try:
    while True:
        led.value(1) #Set led turn on
        time.sleep(0.6) #Sleep 0.5s
        led.value(0) # Setled turn off
        time.sleep(0.5) #Sleep 0.5s
except:
    pass
