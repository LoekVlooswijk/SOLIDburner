import tkinter as tk

import RPi.GPIO as GPIO
from time import sleep, time

GPIO_fan = 17
GPIO_gas = 18
GPIO_ignition = 19
GPIO_iron = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_ignition, GPIO.OUT)
GPIO.setup(GPIO_gas, GPIO.OUT)
GPIO.setup(GPIO_fan, GPIO.OUT)
GPIO.setup(GPIO_iron, GPIO.OUT)

master = tk.Tk()
master.title("Demo Burner Control")
#master.geometry("300x100")
master.attributes('-fullscreen', True)
master.rowconfigure(0, weight=1)
master.rowconfigure(1, weight=1)
master.rowconfigure(2, weight=1)
master.rowconfigure(3, weight=1)
master.columnconfigure(0,weight=1)

power_state = False
time_started = time()

def power_button():
    global power_state
    global time_started
    if power_state: # turn off the system
        # GPIO.output(GPIO21, power_state)
        FANbutton["state"] = "normal"
        power_state = False
        ONlabel = tk.Label(master, text="Turned OFF", fg="red")
        ONlabel.grid(row=0, column=0)
        ONbutton.config(text="Power on")
        print("turn off gas")
        print("turn off iron")

    else: #turn on the system
        # GPIO.output(GPIO21, power_state)
        power_state = True
        FANbutton["state"] = "disabled"
        ONlabel = tk.Label(master, text="Turned ON", fg="green")
        ONlabel.grid(row=0, column=0)
        ONbutton.config(text="Power off")
        time_started = time()
        print("turn on fan")
        sleep(2)
        print("turn on gas")
        sleep(2)
        print("turn on ignition")
        print("turn on iron")
        sleep(2)
        print("turn off ignition")


def turn_off_fan():
    global power_state
    if power_state == False:
        print("turn off fan")


ONbutton = tk.Button(master, text="Power on", bg="blue", command=power_button)
ONlabel = tk.Label(master, text="Turned OFF", fg="red")
ONlabel.grid(row=0, column=0, sticky="NSEW")
ONbutton.grid(row=1, column=0, sticky="NSEW")

FANbutton = tk.Button(master, text="Fan off", bg="blue", command=turn_off_fan)
FANbutton.grid(row=2, column=0, sticky="NSEW")

Exitbutton = tk.Button(master, text="Exit", bg="red", command=master.destroy)
Exitbutton.grid(row=3, column=0, sticky="NSEW")

def update():
    global power_state
    global time_started
    # do things
    if power_state:
        time_running = time() - time_started
        if time_running > 15:
            power_state = True
            power_button()
    #master.after(1000, update)


#master.after(0, update)  # begin updates
master.mainloop()

