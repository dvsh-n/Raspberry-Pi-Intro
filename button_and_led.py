import RPi.GPIO as GPIO
import time

BUTTON_PIN = 26
LED_PIN = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(BUTTON_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    state = GPIO.input(BUTTON_PIN)

    if state == 1:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()