import RPi.GPIO as gpio
import os

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

mytext='apagando todo'
os.system("pico2wave -l es-ES -w L.wav \""+mytext+"\"")
os.system("aplay L.wav")

gpio.setup(3, gpio.OUT)
servo1= gpio.PWM(3, 100)

servo1.start(10)
dutyCycle = ((float(0) * 0.01) + 0.5) * 10
servo1.ChangeDutyCycle(dutyCycle)

gpio.setup(33,gpio.OUT)
gpio.output(33,False)

gpio.setup(35,gpio.OUT)
gpio.output(35,False)

gpio.setup(36,gpio.OUT)
gpio.output(36,False)

gpio.setup(37,gpio.OUT)
gpio.output(37,False)

