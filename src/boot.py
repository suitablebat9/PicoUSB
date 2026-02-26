import time
import board
import storage
import digitalio
import microcontroller

mode = digitalio.DigitalInOut(board.GP25)
mode.direction = digitalio.Direction.INPUT
mode.pull = digitalio.Pull.UP

led = digitalio.DigitalInOut(board.GP12)
led.direction = digitalio.Direction.OUTPUT
led.value = True

storage.remount("/", readonly=False)
m = storage.getmount("/")
m.label = "PicoUSB"
storage.remount("/", readonly=True)
storage.enable_usb_drive()

time.sleep(0.1) #wait a bit so the button gets pulled up

if mode.value:
    storage.disable_usb_drive()
else:
    time.sleep(0.1) #check again after 100ms to see if the button is still pressed
    if mode.value:
        storage.disable_usb_drive()
    else:
        storage.enable_usb_drive()
        microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
        microcontroller.reset()
    

# in case you screw up and disable usb drive without the ability to enable it, to enter safe mode write in shell:
# import microcontroller
# microcontroller.on_next_reset(microcontroller.RunMode.SAFE_MODE)
# microcontroller.reset()