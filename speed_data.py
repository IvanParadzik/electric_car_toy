import pygame
from settings import Settings
import socket
import pygame.locals
import codecs
import time
import os
import sys
from numpy import interp
import math
import json



s = socket.socket()  # Create a socket object
port = 50001 # Reserve a port for your service every new transfer wants a new port or you must wait.

s.connect(('192.168.0.25', port))



old_speed = [0]
while True:
    speed = s.recv(1024)
    new_speed = codecs.decode(speed)
    try:
        final_speed = [int(new_speed)]

    except:
       continue



    with open('speed.txt', 'w') as speed_wheel:
        lines = {}
        lines["speed"] = final_speed
        json.dump(lines, speed_wheel)
