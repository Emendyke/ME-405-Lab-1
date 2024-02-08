"""! @file motor_driver.py
"""

''' 
   \brief     ME 405 Week 5 Lab 1
   \details   This program controls a DC motor with PWM control for varying duty cycles. 
   \author    Emily Mendyke, Jenna Mast
   \version   1.0
   \date      2/08/2024
   \Todo      Add to github
'''

# ME 405 Week 4 Lab 1

import pyb
import time


class MotorDriver:
    """! 
    This class implements a motor driver for an ME405 kit. 
    """

    def __init__ (self, en_pin, in1pin, in2pin, timer):
        """! 
        Creates a motor driver by initializing GPIO
        pins and turning off the motor for safety. 
        @param en_pin : setting enable pin MotorDriver object
        @param in1pin : MotorDriver's first pin object
        @param in2pin : Motordriver's second pin object
        @param timer : MotorDriver's timer object
        @param ch1 : location where timer PWM is channeled to in1pin
        @param ch2 : location where timer PWM is channeled to in2pin
        """
        self.en_pin = en_pin
        self.ch1 = timer.channel(1, pyb.Timer.PWM, pin=in1pin)
        self.ch2 = timer.channel(2, pyb.Timer.PWM, pin=in2pin)
        
        print ("Creating a motor driver")
        

    def set_duty_cycle (self, level):
        """!
        This method sets the duty cycle to be sent
        to the motor to the given level. Positive values
        cause torque in one direction, negative values
        in the opposite direction.
        @param level A signed integer holding the duty
               cycle of the voltage sent to the motor 
        """
        level = int(level)  #signed integer holding duty cycle of the voltage
        if level==0: # for when level is 0
            self.ch1.pulse_width_percent(0)
            self.ch2.pulse_width_percent(0)
            self.en_pin.low()   #disables motor
        elif level<0: # movement of motor for when value of level is negative
            print (f"Setting duty cycle to {level}")
            self.en_pin.high()
            self.ch1.pulse_width_percent(abs(level))
            self.ch2.pulse_width_percent(0)
        else level>0: # movement of motor for when value of level is positive
            print (f"Setting duty cycle to {level}")
            self.en_pin.high()
            self.ch1.pulse_width_percent(0)
            self.ch2.pulse_width_percent(abs(level))
                
        
        
if __name__ == "__main__"

    #Test Motor

    # all pin objects created, for enable, in1pin, and in2pin respectively
    pinA10 = pyb.Pin(pyb.Pin.board.PA10, pyb.Pin.OUT_PP) 
    pinB4 = pyb.Pin(pyb.Pin.board.PB4, pyb.Pin.OUT_PP) 
    pinB5 = pyb.Pin(pyb.Pin.board.PB5, pyb.Pin.OUT_PP)

    #creating timer object channel 3
    tim3 = pyb.Timer(3, freq=20000)

    moe = MotorDrivere(pinA10, pinB4, pinB5, tim3)

    moe.set_duty_cycle(50)

    time.sleep(5)

    moe.set_duty_cycle(-42)

    time.sleep(5)

    motor.set_duty_cycle(0)
