# MicroPython

import pyb                                              # Necessary to use the pyb library

# Set pin PA0 as an output and verify that you can turn the LED on and off.

# Configuring and controlling a digital output pin. Turning it on and off.

# LED code
### Uncomment below code, and cocmment out PWM code to run###
# pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)      # Sets the pin PA0 to output, and push pull and creates an object pinC0 to call it by.
# pinA0.value(1)                                          # Turns the pin on
# pinA0.value(0)                                          # Turns the pin off
# 
# # Alternatively can use the below code to PC0 on and off.
# pinA0.high ()
# pinA0.low ()

# PWM Code #

### Uncomment code below and comment out LED code above to run ###

# Modify the PWM code you’ve tried in Lab 0 to control the LED’s brightness. You need to look on the STM32L476RG Nucleo Arduino Pins diagram on Canvas to see which timer and channel must be used. The purple boxes showing PWMx/y numbers indicate that you must use Timer x and Channel y for a given pin.
# Because the LED will be on when the PWM signal is a logic zero, you must set the timer channel to mode pyb.Timer.PWM_INVERTED to control LED brightness.
    
# Creating a PWM (kind of analog)


pinA0 = pyb.Pin(pyb.Pin.board.PA0, pyb.Pin.OUT_PP)     # Sets the pin PA0 to output, and push pull and creates an object pinA0 to call it by.
tim2 = pyb.Timer(2, freq=20000)                        # Sets timer 2 to a frequency of 20000 Hz and  creates an object, tim2, to call it by
ch2 = tim2.channel(1, pyb.Timer.PWM_INVERTED, pin=pinA0)        # Sets channel 1 for timer 2 to generate a PWM on PA0 and creates an object, ch2, to call it by.
ch2.pulse_width_percent(50)                            # Sets duty cycle


    