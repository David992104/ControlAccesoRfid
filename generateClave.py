import random

def generate():
    simbols = ['a','b', 'c', 'd', 'f', 'g', 
    'h','i', 'j', 'k', 'l', 'm', 
    'n','o', 'p', 'q', 'r', 's', 
    't','u', 'v', 'w', 'x', 'y', 
    'z','1', '2', '3', '4', '5', 
    '6','7', '8', '9', '0' ]
    clave = ""
    for x in range(10):
        clave += random.choice(simbols)
    
    return clave
