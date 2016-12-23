#!/bin/bash

#install python
apt-get --yes --force-yes install python3 python3-pip
#install uinput
pip install python-uinput

#install git
apt-get --yes --force-yes install git
#clone git
git clone https://github.com/RBEGamer/Python-Gamepad-Input.git

