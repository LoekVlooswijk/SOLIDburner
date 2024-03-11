import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

# Relay for main fan for air flow
GPIO_fan = 17

# Gas valve (normally closed)
GPIO_gas = 26

# Relay for ignition
GPIO_ignition = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_ignition, GPIO.OUT)
GPIO.setup(GPIO_gas, GPIO.OUT)
GPIO.setup(GPIO_fan, GPIO.OUT)

#GPIO.setup(GPIO_iron_in1, GPIO.OUT)
#GPIO.setup(GPIO_iron_in2, GPIO.OUT)
#GPIO.setup(GPIO_iron_enable, GPIO.OUT)
#PWM_iron = GPIO.PWM(GPIO_iron_enable, 1000)
#GPIO.output(GPIO_iron_in2, GPIO.LOW)
#PWM_iron.start(25)


def gpio_fan(power):
    if power:  # Start fan
        GPIO.output(GPIO_fan, GPIO.HIGH)
    else:  # Stop fan
        GPIO.output(GPIO_fan, GPIO.LOW)
        
# def gpio_iron(power):
    # global bool_iron
    # if power:  # Start motor
        # bool_iron = True
        # motor_thread = threading.Thread(target=stepper_motor_control)
        # motor_thread.daemon = True
        # motor_thread.start()
    # else:  # Stop motor
        # bool_iron = False
        


def gpio_ignition(power):
    if power:  # spark ignition
        GPIO.output(GPIO_ignition, GPIO.HIGH)
    else:  # Stop ignition
        GPIO.output(GPIO_ignition, GPIO.LOW)


def gpio_gas(power):
    if power:  # Open gas valve
        GPIO.output(GPIO_gas, GPIO.HIGH)
    else:  # Close gas valve
        GPIO.output(GPIO_gas, GPIO.LOW)
