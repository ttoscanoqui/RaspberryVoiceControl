import RPi.GPIO as gpio
import os

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

mytext='encendiendo todo '
os.system("pico2wave -l es-ES -w L.wav \""+mytext+"\"")
os.system("aplay L.wav")

gpio.setup(33,gpio.OUT)
gpio.output(33,True)

gpio.setup(35,gpio.OUT)
gpio.output(35,True)

gpio.setup(36,gpio.OUT)
gpio.output(36,True)

gpio.setup(37,gpio.OUT)
gpio.output(37,True)

gpio.setup(3, gpio.OUT)
servo1= gpio.PWM(3, 100)

servo1.start(10)
dutyCycle = ((float(90) * 0.01) + 0.5) * 10
servo1.ChangeDutyCycle(dutyCycle)
