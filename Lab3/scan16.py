import time
from machine import Pin

while True:
    # Forward direction (GP0 to GP15)
    for i in range(16):
        led = Pin(i, Pin.OUT)
        led.on()
        time.sleep(0.1)
        led.off()

    # Backward direction (GP15 to GP0)
    for i in range(16, -1, -1):
        led = Pin(i, Pin.OUT)
        led.on()
        time.sleep(0.1)
        led.off()
