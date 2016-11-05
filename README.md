# Python-Gamepad-Input
This is a small pythonsnipped for the Adafruit SuperGamePI, to map RPI-GPIO switches to the keyboard.
This script maps 10 GPIO Switches and one (X,Y) analog joystick. FOr reading the analog input of the joystick i used the ADS1 ADC converter ic.

# FEATURES
* Designed for the SuperGamePi from Adafruit or other RPI-Based GameBoy
* Sample KEYS : up,down,left,right (digital-pad), start,select, rb,lb, X, Y, A, B
* One Joystick input
* GPIO for RasperryPI 3
* using UINPUT for sending keystrokes

# SETUP
* Connect all buttons to the GPIO (edit the right GPIO numbers)
* Buttons connected to ground, the pullup is active
* Connect the ADS1 to the RPI I2C Bus
* Run the script with sudo and/or add it as starup

