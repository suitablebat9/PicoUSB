import supervisor
import time
import digitalio
from board import *
import board
from duckyinpython import *

# sleep at the start to allow the device to be recognized by the host computer
time.sleep(.5)

led = digitalio.DigitalInOut(board.GP12)
led.direction = digitalio.Direction.OUTPUT

progStatus = getProgrammingStatus()
print("progStatus", progStatus)

if not progStatus:
    print("Finding payload")
    payload = selectPayload()
    print("Running", payload)
    runScript(payload, led)
    print("Done")

    led.value = True
    # prevent script from ending
    while True:
        time.sleep(1)

else:
    print("Update your payload")
