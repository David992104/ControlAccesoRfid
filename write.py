#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from read import readid

reader = SimpleMFRC522()

def writeClave(clave):
    try:
        reader.write(clave)
        print('Clave guardada ' + clave)
        
    finally:
        GPIO.cleanup()


