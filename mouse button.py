import RPi.GPIO as GPIO
import time
from pymouse import PyMouse

# Initialize GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)

# Initialize PyMouse
m = PyMouse()

try:
    while True:
        if GPIO.input(16) != 0:
            # Simulate a left mouse click at coordinates (300, 275)
            m.click(300, 275, 1)  # 1 indicates left button click
            time.sleep(0.2)  # Add a small delay to prevent repeat clicks
finally:
    GPIO.cleanup()
