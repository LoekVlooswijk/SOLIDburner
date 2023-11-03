import RPi.GPIO as GPIO
from time import sleep, time
from RpiMotorLib import RpiMotorLib

GPIO_pins = (14,15,18)
direction = 20
step = 21

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(direction, GPIO.OUT)
#GPIO.setup(step, GPIO.OUT)
#for pin in GPIO_pins:
#    GPIO.setup(pin, GPIO.OUT)

mymotortest = RpiMotorLib.A4988Nema(direction,step, GPIO_pins, "A4988")

print("starting")
while True:
    mymotortest.motor_go(True, "Full", 600, .004, False, .05)
    sleep(1)
    print("motor")

    
print("finished")

