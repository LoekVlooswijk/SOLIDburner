import RPi.GPIO as GPIO
GPIO.setwarnings(False)

GPIO_fan = 17
GPIO_gas = 18
GPIO_ignition = 19
GPIO_iron = 20

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_ignition, GPIO.OUT)
GPIO.setup(GPIO_gas, GPIO.OUT)
GPIO.setup(GPIO_fan, GPIO.OUT)
GPIO.setup(GPIO_iron, GPIO.OUT)