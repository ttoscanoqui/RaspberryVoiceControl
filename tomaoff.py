import RPi.GPIO as gpio
import os

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)

mytext='apagando toma'
os.system("pico2wave -l es-ES -w L.wav \""+mytext+"\"")
os.system("aplay L.wav")

gpio.setup(35,gpio.OUT)
gpio.output(35,False)
