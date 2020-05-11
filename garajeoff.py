import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

import os

mytext='Apagando garaje '
os.system("pico2wave -l es-ES -w L.wav \""+mytext+"\"")
os.system("aplay L.wav")

gpio.setup(36,gpio.OUT)
gpio.output(36,False)

