#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)

reader = SimpleMFRC522()

def readid():
	id, text = reader.read()
	return id

def read():
	id,text = reader.read()
	return tex

