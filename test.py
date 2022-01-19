from phue import Bridge
import random
import time
b = Bridge('192.168.0.101') # Enter bridge IP here.

#If running for the first time, press button on bridge and run with b.connect() uncommented
b.connect()

lights = b.get_light_objects()

def handleStepDown(light):
    i = 120
    while i > 0:
        light.brightness = i
        i -= 5
        time.sleep(0.5)

def handleStepUp(light):
    i = 0
    while i < 120:
        light.brightness = i
        i += 5
        time.sleep(0.5)

while True:
    for light in lights:
	    light.xy = [random.random(),random.random()]
    handleStepUp(light)
    handleStepDown(light)

        
