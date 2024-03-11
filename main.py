import sys
import gpio_control
import interface as gui
import RPi.GPIO as GPIO
import threading
import time
from RpiMotorLib import RpiMotorLib

# Pins for Stepper motor driver iron
GPIO_iron_direction = 22
GPIO_iron_step = 25
GPIO_iron_EN = 24

mymotortest = RpiMotorLib.A4988Nema(GPIO_iron_direction, GPIO_iron_step, (21,21,21), "A4988")
GPIO.setup(GPIO_iron_EN, GPIO.OUT)
GPIO.output(GPIO_iron_EN, GPIO.LOW)

def exit_software():
    # Quit the software and destroy the gui instance
    gui.master.destroy()
    sys.exit()


def power_button():
    # Toggled by the power button and change internal on/off state
    global turning_on, time_started, time_running
    time_started = time.time()
    time_running = time.time() - time_started
    turning_on = not turning_on


def power_off_check():
    # Make sure everything is turned off when the machine needs to shut down
    global turning_on, time_running, time_started, bool_gas, bool_iron

    if not turning_on:  # turn off the system
        if bool_fan:
            gui.FANbutton["state"] = "normal"

        # Turn off gas and iron
        gpio_control.gpio_gas(False)
        bool_gas = False
        bool_iron = False
        #print("turn off gas")
        #print("turn off iron")
        gui.OnLabel.config(text="Machine turned OFF", fg="red")
        gui.PowerButton.config(text="Power on")


def stepper_motor_control():
    global bool_iron
    while True:
        if bool_iron:
            mymotortest.motor_go(False, "1/8", 100, .0035, False, .001)
            time.sleep(0.001)

def power_on_check():
    # Initiate the turning on process when running
    global turning_on, time_running, time_started, bool_fan, bool_gas, bool_ignition, bool_iron

    if turning_on:  # turn on the system
        if time_running < 6:  # First 6 seconds are starting up
            gui.OnLabel.config(text="Machine turning ON", fg="green", font=gui.large_font)
        gui.FANbutton["state"] = "disabled"
        gui.PowerButton.config(text="Power off")

        if not bool_fan: # Fan should start running first
            print("turn on fan")
            gpio_control.gpio_fan(True)
            bool_fan = True
        if time_running > 2 and not bool_gas:  # Fan is running 2 seconds before gas comes in
            print("turn on gas")
            gpio_control.gpio_gas(True)
            bool_gas = True
        if 4 < time_running < 4.25 and not bool_iron and not bool_ignition:  # quickly turn on ignition
            # Turn on ignition and iron
            print("turn on ignition")
            print("turn on iron")
            gpio_control.gpio_ignition(True)
            bool_ignition = True
            bool_iron = True # Turns on the extra thread for stepper motor
        if time_running > 6 and bool_ignition:
            print("turn off ignition")
            gpio_control.gpio_ignition(False)
            bool_ignition = False
            gui.OnLabel.config(text="Machine turned ON", fg="green")


def turn_off_fan():
    # Turn off the fan when the machine is not running
    global turning_on, bool_fan
    if not turning_on:
        print("turn off fan")
        gpio_control.gpio_fan(False)
        bool_fan = False
        gui.FANbutton["state"] = "disabled"


def update_stats():
    # Turn off the demo burner if it has been burning more than 60 seconds
    global turning_on, time_running, time_started
    # do things
    if turning_on:
        time_running = time.time() - time_started
        if time_running > 60:
            turning_on = False


# initializing
turning_on = False
time_started = time.time()
time_running = 0
bool_fan = False
bool_gas = False
bool_ignition = False
bool_iron = False
motor_thread = threading.Thread(target=stepper_motor_control)
motor_thread.daemon = True
motor_thread.start()
print("init thread iron")


# Define button functioning
gui.PowerButton["command"] = power_button
gui.FANbutton["command"] = turn_off_fan
#gui.Exitbutton["command"] = exit_software


# Main loop
while True:
    # Turn on/off stuff
    power_on_check()
    power_off_check()
    update_stats()

    # Update window
    gui.master.update_idletasks()
    gui.master.update()

    time.sleep(0.1)
