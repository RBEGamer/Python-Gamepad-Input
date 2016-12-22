
#C 2015 Marcel Ochsendorf
import uinput
import time
import RPi.GPIO as GPIO
import subprocess
import  signal, sys


def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
print 'Press Ctrl+C to exit'

gpio_A = 27
gpio_B = 22
gpio_LEFT = 23
gpio_RIGHT = 3
gpio_DOWN = 4
gpio_UP = 17
gipo_START = 18
gpio_SELECT = 14

GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio_A, GPIO.IN, pull_up_down=GPIO.PUD_UP) #A
GPIO.setup(gpio_B, GPIO.IN, pull_up_down=GPIO.PUD_UP) #B
GPIO.setup(gpio_LEFT, GPIO.IN, pull_up_down=GPIO.PUD_UP) #LEFT
GPIO.setup(gpio_RIGHT, GPIO.IN, pull_up_down=GPIO.PUD_UP) #RIGHT
GPIO.setup(gpio_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP) #DOWN
GPIO.setup(gpio_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP) #UP
GPIO.setup(gpio_START, GPIO.IN, pull_up_down=GPIO.PUD_UP) #START
GPIO.setup(gpio_SELECT, GPIO.IN, pull_up_down=GPIO.PUD_UP) #SELECT





#subprocess.call(["sudo", "shutdown", "-h","now"])



device = uinput.Device([uinput.KEY_UP,uinput.KEY_DOWN,uinput.KEY_LEFT,uinput.KEY_RIGHT,uinput.KEY_X, uinput.KEY_ENTER,uinput.KEY_J,uinput.KEY_K, uinput.KEY_L, uinput.KEY_H, uinput.KEY_I, uinput.KEY_O, uinput.KEY_Y,uinput.KEY_M, uinput.KEY_A, uinput.KEY_B,uinput.KEY_C, uinput.KEY_V, uinput.KEY_N,uinput.ABS_X, uinput.ABS_Y])

state_A = False
state_B = False
state_LEFT = False
state_RIGHT = False
state_DOWN = False
state_UP = False
state_START = False
state_SELECT = False



while True:
  
  if (not state_A) and (not GPIO.input(gpio_A)):  # Fire button pressed
    state_A = True
    #print("B pressed")
    device.emit(uinput.KEY_A, 1) # Press Left Ctrl key
  if fire and GPIO.input(gpio_A):  # Fire button released
    stat_A = False
    device.emit(uinput.KEY_A, 0) # Release Left Ctrl key

  if (not state_B) and (not GPIO.input(gpio_B)):  # Fire button pressed
    state_B = True
    #print("B pressed")
    device.emit(uinput.KEY_B, 1) # Press Left Ctrl key
  if stat_B and GPIO.input(gpio_B):  # Fire button released
    state_B = False
    device.emit(uinput.KEY_B, 0) # Release Left Ctrl key


  if (not state_START) and (not GPIO.input(gpio_START)):  # Fire button pressed
    state_START = True
    #print("B pressed")
    device.emit(uinput.KEY_ENTER, 1) # Press Left Ctrl key
  if state_START and GPIO.input(gpio_START):  # Fire button released
    state_START = False
    device.emit(uinput.KEY_ENTR, 0) # Release Left Ctrl key

  if (not state_SELECT) and (not GPIO.input(gpio_SLECT)):  # Fire button pressed
    state_SELECT = True
    #print("B pressed")
    device.emit(uinput.KEY_C, 1) # Press Left Ctrl key
  if state_SELECT and GPIO.input(gpio_SELECT):  # Fire button released
    state_SELECT = False
    device.emit(uinput.KEY_C, 0) # Release Left Ctrl key


  if (not state_LEFT) and (not GPIO.input(gpio_LEFT)):  # Fire button pressed
    state_LEFT = True
    #print("B pressed")
    device.emit(uinput.KEY_LEFT, 1) # Press Left Ctrl key
  if state_LEFT and GPIO.input(gpio_LEFT):  # Fire button released
    state_LEFT = False
    device.emit(uinput.KEY_LEFT, 0) # Release Left Ctrl key
    
  if (not state_RIGHT) and (not GPIO.input(gpio_RIGHT)):  # Fire button pressed
    state_RIGHT = True
    #print("B pressed")
    device.emit(uinput.KEY_RIGHT, 1) # Press Left Ctrl key
  if state_RIGHT and GPIO.input(gpio_RIGHT):  # Fire button released
    state_RIGHT = False
    device.emit(uinput.KEY_RIGHT, 0) # Release Left Ctrl key    

  if (not state_DOWN) and (not GPIO.input(gpio_DOWN)):  # Fire button pressed
    state_DOWN = True
    #print("B pressed")
    device.emit(uinput.KEY_DOWN, 1) # Press Left Ctrl key
  if state_DOWN and GPIO.input(gpio_DOWN):  # Fire button released
    state_DOWN = False
    device.emit(uinput.KEY_DOWN, 0) # Release Left Ctrl key  
    
  if (not state_UP) and (not GPIO.input(gpio_UP)):  # Fire button pressed
    state_UP = True
    #print("B pressed")
    device.emit(uinput.KEY_UP, 1) # Press Left Ctrl key
  if state_UP and GPIO.input(gpio_UP):  # Fire button released
    state_UP = False
    device.emit(uinput.KEY_UP, 0) # Release Left Ctrl key  
  time.sleep(.04)


  #N ist frei
  
