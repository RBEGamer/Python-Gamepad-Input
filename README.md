# Python-Gamepad-Input
This is a small pythonsnipped for the Adafruit SuperGamePI, to map RPI-GPIO switches to the keyboard.
This script maps 10 GPIO Switches and one (X,Y) analog joystick. 
For reading the analog input of the joystick i used the ADS1115 ADC converter ic.

# FEATURES
* Designed for the SuperGamePi from Adafruit or other RPI-Based GameBoy
* Sample KEYS : up,down,left,right (digital-pad), start,select, rb,lb, X, Y, A, B
* One Joystick input
* GPIO for RasperryPI 3
* using UINPUT for sending keystrokes

# HARDWARE
* 10 pcb push buttons
* jumperwires
* ADS1115 (https://www.adafruit.com/product/1085)

# SETUP HARDWARE
* Connect all buttons to the GPIO (edit the right GPIO numbers)
* Buttons connected to ground, the pullup is active
* Connect the ADS1115 to the RPI I2C Bus
* Connect to the the middle pin of each pot to the first and second input of the ADS1115
* Connect the left pot pins to ground and 3.3V of the RPI

# SETUP SOFTWARE
* Download the files located at /sry to your RPI
* Download the ADS1115 libary from Adafruit (https://github.com/adafruit/Adafruit_Python_ADS1x15)
* Run /src/gpio-js_driver.py as sudo and/or add it as starup (rc.local other other)
* Have FUN

