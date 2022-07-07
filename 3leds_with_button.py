import RPi.GPIO as GPIO
import time

BUTTON_PIN = 26
LED1_PIN = 17
LED2_PIN = 27
LED3_PIN = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)
GPIO.setup(LED3_PIN, GPIO.OUT)

curr_state = 0
counter = 0

while True:
    time.sleep(0.01)
    count = False  

    if counter == 0:
        GPIO.output(LED1_PIN, GPIO.HIGH)
        GPIO.output(LED2_PIN, GPIO.LOW)
        GPIO.output(LED3_PIN, GPIO.LOW)
    elif counter == 1:
        GPIO.output(LED2_PIN, GPIO.HIGH)
        GPIO.output(LED1_PIN, GPIO.LOW)
        GPIO.output(LED3_PIN, GPIO.LOW)
    elif counter == 2:
        GPIO.output(LED3_PIN, GPIO.HIGH)
        GPIO.output(LED1_PIN, GPIO.LOW)
        GPIO.output(LED2_PIN, GPIO.LOW)
    
    curr_state = GPIO.input(BUTTON_PIN)
    
    while curr_state == GPIO.HIGH:
        time.sleep(0.01)
        curr_state = GPIO.input(BUTTON_PIN)
        count = True

    if count:
        if counter == 2:
            counter = 0
        else:
            counter += 1
    
    print(counter)

GPIO.cleanup()