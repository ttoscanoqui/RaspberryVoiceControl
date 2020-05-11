import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

import os

mytext='Apagando sala '
os.system("pico2wave -l es-ES -w L.wav \""+mytext+"\"")
os.system("aplay L.wav")

gpio.setup(37,gpio.OUT)
gpio.output(37,False)
