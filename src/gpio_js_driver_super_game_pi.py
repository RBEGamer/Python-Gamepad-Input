
#C 2015 Marcel Ochsendorf
import uinput
import time
import RPi.GPIO as GPIO
import subprocess
import  signal, sys
from Adafruit_ADS1x15 import ADS1x15


def signal_handler(signal, frame):
        print 'You pressed Ctrl+C!'
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)
#print 'Press Ctrl+C to exit'


ADS1115 = 0x01	# 16-bit ADC
gain = 4096  # +/- 4.096V
sps = 64  # 250 samples per second
adc = ADS1x15(ic=ADS1115)
ads_threshhold = 1000
adc_divider = 1 #1000
adc_x = 0
adc_x_cal = 1.6
adc_x_cal = adc.readADCSingleEnded(0, gain, sps) / adc_divider
adc_y  = 0
adc_y_cal = 1.6
adc_y_cal = adc.readADCSingleEnded(1, gain, sps) / adc_divider

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) #B
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Y
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) #X
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) #A
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # JS0 BTN

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) #START
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP) #TOUCHSCREEN TAP

GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) #SELECT

GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP) #RSB
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) #LSB



#subprocess.call(["sudo", "shutdown", "-h","now"])



device = uinput.Device([uinput.KEY_UP,uinput.KEY_DOWN,uinput.KEY_LEFT,uinput.KEY_RIGHT,uinput.KEY_X, uinput.KEY_ENTER,uinput.KEY_J,uinput.KEY_K, uinput.KEY_L, uinput.KEY_H, uinput.KEY_I, uinput.KEY_O, uinput.KEY_Y,uinput.KEY_M, uinput.KEY_A, uinput.KEY_B,uinput.KEY_C, uinput.KEY_V, uinput.KEY_N,uinput.ABS_X, uinput.ABS_Y])

fire = False
up = False
down = False
left = False
right = False
js0btn = False

start = False
select = False
touch = False

js0x = 0
js0y = 0

js0xs = True
js0ys = True
js0ysu = True
js0xsu = True


adc_y_up = False
adc_y_down = False

adc_x_up = False
adc_x_down = False

rsb = False
lsb = False

while True:
  adc_x = adc_x_cal -(adc.readADCSingleEnded(0, gain, sps) / adc_divider)
  adc_x = adc_x*-1

  if -200 <= adc_x <= 200:
   adc_x_up = False
   adc_x_down = False
  elif adc_x > 200:
   adc_x_up = True
   adc_x_down = False
  elif adc_x <= -200:
   adc_x_up = False
   adc_x_down = True



  adc_y = adc_y_cal -(adc.readADCSingleEnded(1, gain, sps) / adc_divider)
  adc_y = adc_y*-1

  if -200 <= adc_y <= 200:
   adc_y_up = False
   adc_y_down = False
  elif adc_y > 200:
   adc_y_up = True
   adc_y_down = False
  elif adc_y <= -200:
   adc_y_up = False
   adc_y_down = True




  #if js0y != adc_y:
   #device.emit(uinput.ABS_Y, int(adc_y))
   #js0y = adc_y





  if (not js0ys) and adc_y_up:  # Fire button pressed
    js0ys = True
    #print("js0 y up")
    device.emit(uinput.KEY_UP, 1) # Press Left Ctrl key
  elif js0ys and (not adc_y_up):  # Fire button released
    js0ys = False
    device.emit(uinput.KEY_UP, 0) # Release Left Ctrl key
    #print("js0 y up release")
  elif (not js0y) and adc_y_down:  # Fire button pressed
    js0y = True
    #print("js0 y down")
    device.emit(uinput.KEY_DOWN, 1) # Press Left Ctrl key
  elif js0y and (not adc_y_down):  # Fire button released
    js0y = False
    device.emit(uinput.KEY_DOWN, 0) # Release Left Ctrl key
    #print("js0 y down release")


  if (not js0xs) and adc_x_up:  # Fire button pressed
    js0xs = True
    #print("js0 x right")
    device.emit(uinput.KEY_RIGHT, 1) # Press Left Ctrl key
  elif js0xs and (not adc_x_up):  # Fire button released
    js0xs = False
    device.emit(uinput.KEY_RIGHT, 0) # Release Left Ctrl key
    #print("js0 x right release")
  elif (not js0x) and adc_x_down:  # Fire button pressed
    js0x = True
    #print("js0 x left")
    device.emit(uinput.KEY_LEFT, 1) # Press Left Ctrl key
  elif js0x and (not adc_x_down):  # Fire button released
    js0x = False
    device.emit(uinput.KEY_LEFT, 0) # Release Left Ctrl key
    #print("js0 x left release")






  if (not fire) and (not GPIO.input(17)):  # Fire button pressed
    fire = True
    #print("B pressed")
    device.emit(uinput.KEY_B, 1) # Press Left Ctrl key
  if fire and GPIO.input(17):  # Fire button released
    fire = False
    device.emit(uinput.KEY_B, 0) # Release Left Ctrl key


  if (not up) and (not GPIO.input(18)):  # Up button pressed
    up = True
    #print("Y pressed")
    device.emit(uinput.KEY_Y, 1) # Press Up key
  if up and GPIO.input(18):  # Up button released
    up = False
    device.emit(uinput.KEY_Y, 0) # Release Up key


  if (not down) and (not GPIO.input(27)):  # Down button pressed
    down = True
    #print("X pressed")
    device.emit(uinput.KEY_X, 1) # Press Down key
  if down and GPIO.input(27):  # Down button released
    down = False
    device.emit(uinput.KEY_X, 0) # Release Down key


  if (not left) and (not GPIO.input(22)):  # Left button pressed
    left = True
    #print("A pressed")
    device.emit(uinput.KEY_A, 1) # Press Left key
  if left and GPIO.input(22):  # Left button released
    left = False
    device.emit(uinput.KEY_A, 0) # Release Left key

  if (not js0btn) and (not GPIO.input(23)):  # Left button pressed
    js0btn = True
    #print("JS0 pressed")
    device.emit(uinput.KEY_C, 1) # Press Left key
  if js0btn and GPIO.input(23):  # Left button released
    js0btn = False
    device.emit(uinput.KEY_C, 0) # Release Left key


  if (not start) and (not GPIO.input(24)):  # Left button pressed
    start = True
    #print("start pressed")
    device.emit(uinput.KEY_V, 1) # Press Left key
  if start and GPIO.input(24):  # Left button released
    start = False
    device.emit(uinput.KEY_V, 0) # Release Left key

  if (not touch) and (not GPIO.input(25)):  # Left button pressed
    touch = True
    #print("touch pressed")
    device.emit(uinput.KEY_ENTER, 1) # Press Left key
  if touch and GPIO.input(25):  # Left button released
    touch = False
    device.emit(uinput.KEY_N, 0) # Release Left key

  if (not lsb) and (not GPIO.input(16)):  # Left button pressed
    lsb = True
    #print("lsb pressed")
    device.emit(uinput.KEY_I, 1) # Press Left key
  if lsb and GPIO.input(16):  # Left button released
    lsb = False
    device.emit(uinput.KEY_I, 0) # Release Left key

  if (not rsb) and (not GPIO.input(20)):  # Left button pressed
    rsb = True
    #print("rsb pressed")
    device.emit(uinput.KEY_O, 1) # Press Left key
  if rsb and GPIO.input(20):  # Left button released
    rsb = False
    device.emit(uinput.KEY_O, 0) # Release Left key

  if (not select) and (not GPIO.input(21)):  # Left button pressed
    select = True
    #print("select pressed")
    device.emit(uinput.KEY_M, 1) # Press Left key
  if select and GPIO.input(21):  # Left button released
    select = False
    device.emit(uinput.KEY_M, 0) # Release Left key
  time.sleep(.04)


  #N ist frei
  
