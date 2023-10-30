from time import *
import interface

state = "idle"

while True:
    sleep(30)
    match state:
        case 'idle':
            # set variables for idle state
            # equipment off