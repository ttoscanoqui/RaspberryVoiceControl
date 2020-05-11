import time
import RPi.GPIO as gpio
import os

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)


mytext='abriendo puerta'
os.system("pico2wave -l es-ES -w L.wav \""+mytext+"\"")
os.system("aplay L.wav")

gpio.setup(3, gpio.OUT)
servo1= gpio.PWM(3, 100)

servo1.start(10)
dutyCycle = ((float(90) * 0.01) + 0.5) * 10
servo1.ChangeDutyCycle(dutyCycle)

