# PicoUSB

Repository for PicoUSB - RP2040 based, affordable, easy to use and easy to program Bad USB

- [PicoUSB](#picousb)
  - [Setup](#setup)
  - [Operation](#operation)
  - [Important Files](#important-files)

![PicoUSB-3](https://github.com/TomBrlek/PicoUSB/assets/137766608/e64d61c2-e8db-4887-aa5e-6456fb3bd157)

You just got an empty PicoUSB? Here's how to program it:

## Setup

1. Download the CircuitPython file.
2. Insert PicoUSB into your USB drive while holding the "Boot" button. (Opens it in a bootloader mode. The first time you do this you don't have to hold the "Boot" button)
3. Copy `CircuitPython.uf2` file to the USB and wait for few seconds or a minute for it to finish setting up. (will close and reopen the explorer, be patient)
4. Download/Clone the contents of this repository.
5. Open the USB device in explorer and copy/paste everything from `./src/` into it. (Replace all)

That is it! Modify `pico_usb.txt` to change the functionality. See below to know what to do next.

([Video Tutorial](https://youtu.be/jKH6WgFiaB0))

## Operation

- Inserting the PicoUSB while not holding any buttons will not show as a USB drive and will execute the "bad usb" code found in the pico_usb.txt.
- Inserting it while holding the "Mode" button will not execute any "bad usb" code and will show as a USB drive. This way you can freely edit the code.
- If you insert it while holding the "Boot" button, it will open in bootloader mode. This is usually only used the first time the device is set up and never again.

## Important Files

> [!CAUTION]
> Changing any python can result in **permanently bricking your device**. Be very careful when modifying `boot.py` as disabling the USB drive without a failsafe could render the device useless!
> Be careful when writing your own micropython scripts! The developers are not responsible if you brick your own device this way!

- payload.txt - here is where your executable pseudo-code is located.
- layout.txt - here is where you select your keyboard layout.
- code.py - interpreter that executes your pesudo code. Free to modify. (1)
- boot.py - this code executes before the USB is recognised. Free to modify. (1)

**payload.txt API:**

The payload.txt is where you put your payload (I know shocker). It uses regular ducky script you can find online.
